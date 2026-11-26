#!/usr/bin/env python3
"""Blind third-reading judge of every spot where the Pro draft and Flash verifier disagree on words or punctuation.

  judge.py --spots spots.json --verified VERIFIED_DIR --images PAGES_DIR --out JUDGE_DIR --prepare
        Writes blind A/B spot prompts in JUDGE_DIR/tasks/ (shuffled per spot so the Gemini Pro judge subagent
        does not know which reading is the draft's and which is the verifier's).
  judge.py --spots spots.json --verified VERIFIED_DIR --images PAGES_DIR --out JUDGE_DIR [--apply]
        Reads JUDGE_DIR/raw/pNNNN.txt verdicts, unblinds A/B, applies choices safely (preserving images and
        paired moves), and writes JUDGE_DIR/pNNNN.txt, verdicts.jsonl, and report.txt.
"""
import argparse, hashlib, json, os, re, sys
from pathlib import Path

TASK = """You are checking a transcription of one scanned page of a novel printed in English before 1914.
Open the page image `{img}` with `view_file` first. Do NOT inspect `draft/` or `verify/` directories.

Two transcriptions of this page disagree at the numbered spots below. For each spot, find the place on the scan
(the context shows the surrounding words; ⏎ marks a paragraph break) and decide which reading is what is PRINTED,
letter for letter and mark for mark. The printed text wins even where it looks like a misprint or an old spelling;
do not prefer the more modern or more usual form. Ignore differences of spacing, straight or curly quotes, and
line-end hyphenation.

{spots}

Write ONLY one JSON object per spot, one per line, to `{out_raw}`:
{{"n": 1, "is": "A" | "B" | "neither", "print": "what the scan shows at this spot (same span as the readings)", "sure": "high" | "medium" | "low"}}
"""


def labels(page, n):
    """True if reading A is the draft's for this spot (stable pseudo-random)."""
    return int(hashlib.sha1(f"{page}:{n}".encode()).hexdigest(), 16) % 2 == 0


def parse(reply):
    out = {}
    for ln in (reply or "").splitlines():
        ln = ln.strip().strip("`").rstrip(",")
        if ln.startswith("{"):
            try:
                d = json.loads(ln)
                out[int(d["n"])] = d
            except (ValueError, KeyError, TypeError):
                pass
    return out


def moves(spots):
    def piece(long, short):
        return long.replace(short, "", 1).strip() if short and short in long and len(long) > len(short) else ""
    out = []
    for s in spots:
        gone = piece(s["find"], s["replace"])
        if len(gone) < 20:
            continue
        for t in spots:
            if t is not s and gone in t["replace"] and gone not in t["find"]:
                out.append((s["n"], t["n"]))
    return out


HEADING_LINE = re.compile(r"(?m)^#")
IMAGE_LINE = re.compile(r"\[\[image:[^\]]*\]\]")
KEEP_LINE = re.compile(r"\[\[image:[^\]]*\]\]|\[\[caption\]\][^\n]*")


def dropped_images(spot, spots):
    out = []
    for m in KEEP_LINE.findall(spot.get("find", "")):
        if m in spot.get("replace", ""):
            continue
        if any(m in t.get("replace", "") for t in spots if t is not spot):
            continue
        out.append(m)
    return out


def apply(verified_text, spots, verdicts, page):
    rows, text = [], verified_text

    def side(s):
        v = verdicts.get(s["n"])
        if v is None or v.get("is") not in ("A", "B"):
            return None
        return "draft" if (v["is"] == "A") == labels(page, s["n"]) else "verified"

    split = set()
    for a, b in moves(spots):
        sa, sb = (side(next(s for s in spots if s["n"] == k)) for k in (a, b))
        if sa != sb:
            split |= {a, b}
    for s in spots:
        v = verdicts.get(s["n"])
        a_is_draft = labels(page, s["n"])
        if v is None:
            rows.append(("unanswered", s, None)); continue
        choice = v.get("is")
        who = "neither" if choice not in ("A", "B") else ("draft" if (choice == "A") == a_is_draft else "verified")
        if s["n"] in split:
            rows.append(("move judged both ways: verified kept", s, v)); continue
        if who != "draft" and dropped_images(s, spots):
            if text.count(s["replace"]) == 1 and s["replace"]:
                text = text.replace(s["replace"], s["find"]); who = "draft kept: the verifier dropped a picture"
            else:
                who = "the verifier dropped a picture (could not undo: edit by hand)"
        if who == "draft":
            if text.count(s["replace"]) == 1:
                text = text.replace(s["replace"], s["find"])
            else:
                who = "draft (could not undo: edit by hand)"
        rows.append((who, s, v))
    return text, rows


def must_look(who, sure, spot):
    if HEADING_LINE.search(spot.get("find", spot.get("draft", ""))) or HEADING_LINE.search(spot.get("replace", spot.get("verified", ""))):
        return True
    if IMAGE_LINE.search(spot.get("find", spot.get("draft", ""))) or IMAGE_LINE.search(spot.get("replace", spot.get("verified", ""))):
        return True
    return who != "verified" or sure != "high"


def prepare_tasks(spots, images_dir, out_dir):
    tdir = os.path.join(out_dir, "tasks")
    rdir = os.path.join(out_dir, "raw")
    os.makedirs(tdir, exist_ok=True)
    os.makedirs(rdir, exist_ok=True)
    todo = []
    for page in sorted(spots):
        raw = os.path.abspath(os.path.join(rdir, page + ".txt"))
        if os.path.exists(raw) and os.path.getsize(raw) > 0:
            continue
        img = next((os.path.abspath(os.path.join(images_dir, page + e))
                    for e in (".jpg", ".jpeg", ".png")
                    if os.path.exists(os.path.join(images_dir, page + e))), None)
        if not img:
            sys.exit(f"judge: no image for {page}")
        lines = []
        for s in spots[page]:
            d, v = s["draft"], s["verified"]
            A, B = (d, v) if labels(page, s["n"]) else (v, d)
            lines.append(f"Spot {s['n']}. Context: …{s['context']}…\n  A: {A!r}\n  B: {B!r}")
        tfile = os.path.abspath(os.path.join(tdir, page + ".md"))
        Path(tfile).write_text(TASK.format(img=img, spots="\n\n".join(lines), out_raw=raw), encoding="utf-8")
        todo.append((page, tfile, raw))
    idx_file = os.path.abspath(os.path.join(tdir, "INSTRUCTIONS.md"))
    idx_lines = [
        f"# Blind Judge Tasks ({len(todo)} pages)",
        "",
        "For each task file below, read the task file, inspect ONLY the referenced scan image with `view_file` (do NOT read `draft/`, `verify/`, or `spots.json`), and write the JSONL verdicts to the specified `raw/pNNNN.txt` file.",
        "",
    ] + [f"- `{pg}`: task `{tf}` -> write `{rf}`" for pg, tf, rf in todo]
    Path(idx_file).write_text("\n".join(idx_lines) + "\n", encoding="utf-8")
    print(f"judge --prepare: {len(todo)} of {len(spots)} page(s) need judging -> {idx_file}")


def apply_verdicts(spots, verified_dir, out_dir, model="gemini-pro"):
    os.makedirs(os.path.join(out_dir, "raw"), exist_ok=True)
    tally, rep, allv = {}, [], []
    for f in sorted(os.listdir(verified_dir)):
        if not re.fullmatch(r"p\d+[a-z]?\.txt", f):
            continue
        page = f[:-4]
        text = open(os.path.join(verified_dir, f), encoding="utf-8").read()
        if page in spots:
            raw = os.path.join(out_dir, "raw", page + ".txt")
            verdicts = parse(open(raw, encoding="utf-8").read()) if os.path.exists(raw) else {}
            text, rows = apply(text, spots[page], verdicts, page)
            for who, s, v in rows:
                tally[who] = tally.get(who, 0) + 1
                allv.append({"page": page, "n": s["n"], "who": who, "draft": s["draft"], "verified": s["verified"], "judge": v})
                sure = (v or {}).get("sure", "")
                if must_look(who, sure, s):
                    rep.append(f"{page} #{s['n']} [{who}{', sure: ' + sure if sure else ''}] draft {s['draft']!r} | verified {s['verified']!r}"
                               + (f" | judge reads {v.get('print')!r}" if v else ""))
        open(os.path.join(out_dir, f), "w", encoding="utf-8").write(text)
    with open(os.path.join(out_dir, "verdicts.jsonl"), "w", encoding="utf-8") as fo:
        for v in allv:
            fo.write(json.dumps(v, ensure_ascii=False) + "\n")
    log_p = os.path.join(out_dir, "log.jsonl")
    if not os.path.exists(log_p):
        with open(log_p, "w", encoding="utf-8") as lf:
            for page in sorted(spots):
                lf.write(json.dumps({"page": page, "model": model, "cost": 0.0}) + "\n")
    head = f"judge {model}: {sum(tally.values())} spots on {len(spots)} pages: {tally}"
    open(os.path.join(out_dir, "report.txt"), "w", encoding="utf-8").write(head + "\n" + "\n".join(rep) + "\n")
    print(head)
    print(f"{len(rep)} spots to look at on the scan: {os.path.join(out_dir, 'report.txt')}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--spots", required=True); ap.add_argument("--verified", required=True)
    ap.add_argument("--images", required=True); ap.add_argument("--out", required=True)
    ap.add_argument("--model", default="gemini-pro")
    ap.add_argument("--prepare", action="store_true", help="write blind A/B task prompts for a Gemini Pro judge subagent")
    ap.add_argument("--apply", action="store_true", help="apply raw verdicts and write judged page files")
    a = ap.parse_args()
    spots = json.load(open(a.spots, encoding="utf-8"))
    if a.prepare:
        prepare_tasks(spots, a.images, a.out)
    else:
        apply_verdicts(spots, a.verified, a.out, a.model)


if __name__ == "__main__":
    main()
