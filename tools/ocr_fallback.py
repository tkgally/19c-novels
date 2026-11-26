#!/usr/bin/env python3
"""Tesseract + model-corrections fallback for pages refused by an output/recitation filter.

  ocr_fallback.py prepare --images IMG_DIR --draft DRAFT_DIR [--pages p0012,p0013] [--prompt prompts/verify.md]
  ocr_fallback.py apply   --draft DRAFT_DIR

Why: if a model refuses to emit a full page verbatim (recitation filter), local `tesseract` produces the initial
rough page text in `DRAFT_DIR/_fallback/pNNNN.raw.txt` and a Gemini Pro subagent proofreads it against the scan
emitting ONLY JSONL `{"find": ..., "replace": ...}` patches to `DRAFT_DIR/_fallback/pNNNN.corr`. `apply` then
produces `DRAFT_DIR/pNNNN.txt` and records the pages in `DRAFT_DIR/fallback.json` so they are named in
`notes_on_text` and included in the audit.
"""
import argparse, json, os, re, subprocess, sys
from pathlib import Path

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import corrections, normalize  # noqa: E402


def raw_to_markup(raw):
    """Turn raw Tesseract output into basic page-markup paragraphs (`[[page ?]]` + one line per paragraph)."""
    paras, cur = [], []
    for ln in raw.splitlines():
        s = ln.strip()
        if not s:
            if cur:
                paras.append( cur_join(cur) )
                cur = []
        else:
            cur.append(s)
    if cur:
        paras.append(cur_join(cur))
    body = "\n\n".join(paras) if paras else "[[blank]]"
    return normalize.norm_page("[[page ?]]\n\n" + body + "\n")


def cur_join(lines):
    out = lines[0]
    for nxt in lines[1:]:
        if out.endswith("-") and nxt[:1].islower():
            out = out[:-1] + nxt
        else:
            out = out + " " + nxt
    return out


def refused_pages(draft_dir):
    log_p = os.path.join(draft_dir, "log.jsonl")
    if not os.path.exists(log_p):
        return []
    out = []
    for ln in open(log_p, encoding="utf-8"):
        if ln.strip():
            d = json.loads(ln)
            if d.get("error") and not os.path.exists(os.path.join(draft_dir, d["page"] + ".txt")):
                out.append(d["page"])
    return sorted(set(out))


def cmd_prepare(a):
    pages = [p.strip() for p in a.pages.split(",") if p.strip()] if a.pages else refused_pages(a.draft)
    if not pages:
        print("ocr_fallback: no refused pages to process")
        return
    fb_dir = os.path.join(a.draft, "_fallback")
    os.makedirs(fb_dir, exist_ok=True)
    prompt_abs = os.path.abspath(a.prompt)
    task_lines = [
        "# OCR Fallback Corrections Task",
        "",
        f'Read `{prompt_abs}`. Each page below was first read by local Tesseract OCR (`*.raw.txt`), so running heads, page numbers, italics, small capitals, `[[cont]]`, headings, and misread letters need to be corrected against the scan image (`view_file`) using ONLY JSONL `{{"find": ..., "replace": ...}}` lines written to `*.corr`.',
        "",
    ]
    for stem in pages:
        img = next((os.path.abspath(os.path.join(a.images, stem + ext))
                    for ext in (".jpg", ".jpeg", ".png")
                    if os.path.exists(os.path.join(a.images, stem + ext))), None)
        if not img:
            sys.exit(f"ocr_fallback: no image for {stem}")
        raw_p = os.path.abspath(os.path.join(fb_dir, stem + ".raw.txt"))
        corr_p = os.path.abspath(os.path.join(fb_dir, stem + ".corr"))
        if not os.path.exists(raw_p):
            res = subprocess.run(["tesseract", img, "-", "--psm", "4", "-l", "eng"], capture_output=True, text=True, check=True)
            Path(raw_p).write_text(raw_to_markup(res.stdout), encoding="utf-8")
        task_lines.append(f"- `{stem}`: image `{img}` | raw `{raw_p}` -> write `{corr_p}`")
    tpath = os.path.abspath(os.path.join(fb_dir, "task.md"))
    Path(tpath).write_text("\n".join(task_lines) + "\n", encoding="utf-8")
    print(f"ocr_fallback prepare: {len(pages)} page(s) ready -> {tpath}")


def cmd_apply(a):
    fb_dir = os.path.join(a.draft, "_fallback")
    if not os.path.isdir(fb_dir):
        print("ocr_fallback apply: nothing in _fallback")
        return
    raws = sorted(f[:-8] for f in os.listdir(fb_dir) if f.endswith(".raw.txt"))
    done = []
    for stem in raws:
        corr_p = os.path.join(fb_dir, stem + ".corr")
        if not os.path.exists(corr_p):
            sys.exit(f"ocr_fallback apply: missing {corr_p}")
        rtext = open(os.path.join(fb_dir, stem + ".raw.txt"), encoding="utf-8").read()
        ctext = open(corr_p, encoding="utf-8").read()
        out, n_app, _ = corrections.apply(rtext, ctext)
        open(os.path.join(a.draft, stem + ".txt"), "w", encoding="utf-8").write(normalize.norm_page(out))
        done.append(stem)
    fb_json = os.path.join(a.draft, "fallback.json")
    prev = json.load(open(fb_json, encoding="utf-8")) if os.path.exists(fb_json) else []
    merged = sorted(set(prev) | set(done))
    json.dump(merged, open(fb_json, "w", encoding="utf-8"), indent=1)
    print(f"ocr_fallback apply: wrote {len(done)} page(s) to {a.draft}; fallback.json={merged}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("prepare"); p.add_argument("--images", required=True); p.add_argument("--draft", required=True); p.add_argument("--pages"); p.add_argument("--prompt", default=os.path.join(HERE, "..", "prompts", "verify.md")); p.set_defaults(f=cmd_prepare)
    p = sub.add_parser("apply"); p.add_argument("--draft", required=True); p.set_defaults(f=cmd_apply)
    a = ap.parse_args()
    a.f(a)


if __name__ == "__main__":
    main()
