#!/usr/bin/env python3
"""How full the session's context window is, and how long the session has run.

  session_meter.py            a few lines: tokens in the context now, the share of the window, whether the
                              conversation has been summarized (compacted), start time, and hours elapsed
  session_meter.py --row      the same as the first cells of a row for notes/sessions.md

Supports Antigravity brain transcripts (~/.gemini/jetski/brain/.../.system_generated/logs/transcript.jsonl)
as well as JSONL transcripts passed via --transcript. When no transcript is yet written to disk, prints the
fallback notice referenced in RESUME.md §3.
"""
import argparse, datetime, glob, json, os, sys

WINDOW = 1_000_000
DROP = 0.6


def find_transcript(home=None, app_dir=None):
    app = app_dir or os.environ.get("ANTIGRAVITY_APP_DATA_DIR") or os.path.join(home or os.path.expanduser("~"), ".gemini", "jetski")
    hits = glob.glob(os.path.join(app, "brain", "**", ".system_generated", "logs", "transcript.jsonl"), recursive=True)
    if not hits:
        base = os.path.join(home or os.path.expanduser("~"), ".claude", "projects")
        hits = glob.glob(os.path.join(base, "*", "*.jsonl"))
    return max(hits, key=os.path.getmtime) if hits else None


def read(path):
    sizes, marks, first, last, approx_chars = [], 0, None, None, 0
    with open(path, encoding="utf-8", errors="replace") as f:
        for line in f:
            approx_chars += len(line)
            try:
                d = json.loads(line)
            except ValueError:
                continue
            if not isinstance(d, dict):
                continue
            ts = d.get("timestamp") or d.get("created_at") or d.get("createdAt")
            if isinstance(ts, str):
                try:
                    t = datetime.datetime.fromisoformat(ts.replace("Z", "+00:00"))
                    first = first or t
                    last = t
                except ValueError:
                    pass
            if d.get("isSidechain"):
                continue
            if d.get("isCompactSummary") or d.get("subtype") == "compact_boundary":
                marks += 1
            u = d.get("usage") or ((d.get("message") or {}).get("usage") if isinstance(d.get("message"), dict) else None)
            if isinstance(u, dict):
                n = sum(int(u.get(k) or 0) for k in (
                    "input_tokens", "cache_creation_input_tokens", "cache_read_input_tokens", "output_tokens",
                    "promptTokenCount", "candidatesTokenCount", "cachedContentTokenCount",
                ))
                if n:
                    sizes.append(n)
    drops = sum(1 for a, b in zip(sizes, sizes[1:]) if a > 20_000 and b < a * DROP)
    tokens = sizes[-1] if sizes else (approx_chars // 4)
    peak = max(sizes) if sizes else tokens
    return {"tokens": tokens, "peak": peak, "compactions": max(marks, drops), "start": first, "end": last}


def window(arg=None):
    v = arg or os.environ.get("NOVELS_CONTEXT_WINDOW")
    try:
        return int(v) if v else WINDOW
    except ValueError:
        return WINDOW


def report(m, win, now=None):
    now = now or datetime.datetime.now(datetime.timezone.utc)
    pct = round(100 * m["tokens"] / win) if win else 0
    start = m["start"]
    hours = (now - start).total_seconds() / 3600 if start else 0.0
    return {"tokens": m["tokens"], "window": win, "percent": pct, "compactions": m["compactions"],
            "start": start.strftime("%Y-%m-%d %H:%M") if start else "?", "now": now.strftime("%H:%M"),
            "hours": round(hours, 1)}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--transcript"); ap.add_argument("--window"); ap.add_argument("--row", action="store_true")
    a = ap.parse_args(argv)
    path = a.transcript or find_transcript()
    if not path or not os.path.exists(path):
        print("session_meter: no transcript found; use the rule in RESUME.md for a session without a meter")
        return 2
    r = report(read(path), window(a.window))
    if a.row:
        print(f"| {r['start']} | {r['now']} | {r['hours']} | {r['tokens']:,} ({r['percent']}%) | {r['compactions']} |")
    else:
        print(f"context: {r['tokens']:,} of {r['window']:,} tokens ({r['percent']}%)   summarized: {r['compactions']} time(s)")
        print(f"session: started {r['start']} UTC, now {r['now']} UTC, {r['hours']} h")
    return 0


if __name__ == "__main__":
    sys.exit(main())
