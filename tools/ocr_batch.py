#!/usr/bin/env python3
"""Batch preparation and application for Gemini Pro (draft) and Gemini Flash (second-pass verify) subagents.

  ocr_batch.py prepare-draft  --images IMG_DIR --prompt prompts/transcribe.md --out DRAFT_DIR [--pages RANGE] [--batch-size 25]
  ocr_batch.py check-draft    --images IMG_DIR --out DRAFT_DIR [--pages RANGE]
  ocr_batch.py prepare-verify --images IMG_DIR --draft DRAFT_DIR --prompt prompts/verify.md --out VERIFY_DIR [--batch-size 25]
  ocr_batch.py apply-verify   --draft DRAFT_DIR --out VERIFY_DIR
"""
import argparse, json, os, re, sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import corrections  # noqa: E402


def parse_page_range(spec):
    """Parse '1-10,15,20-25' or 'p0001-p0010' into a set of ints."""
    want = set()
    for part in spec.split(","):
        part = part.strip()
        if not part:
            continue
        nums = [int(x) for x in re.findall(r"\d+", part)]
        if "-" in part and len(nums) == 2:
            want.update(range(nums[0], nums[1] + 1))
        elif len(nums) == 1:
            want.add(nums[0])
    return want


def list_images(img_dir, pages_spec=None):
    imgs = sorted(f for f in os.listdir(img_dir) if re.fullmatch(r"p\d+[a-z]?\.(jpg|jpeg|png)", f))
    if pages_spec:
        want = parse_page_range(pages_spec)
        imgs = [f for f in imgs if int(re.search(r"\d+", f).group(0)) in want]
    return imgs


def chunked(seq, size):
    return [seq[i:i + size] for i in range(0, len(seq), size)]


def cmd_prepare_draft(a):
    os.makedirs(os.path.join(a.out, "batches"), exist_ok=True)
    prompt_abs = os.path.abspath(a.prompt)
    imgs = list_images(a.images, a.pages)
    todo = []
    for f in imgs:
        stem = os.path.splitext(f)[0]
        out_txt = os.path.join(a.out, stem + ".txt")
        if not (os.path.exists(out_txt) and os.path.getsize(out_txt) > 0):
            todo.append((stem, os.path.abspath(os.path.join(a.images, f)), os.path.abspath(out_txt)))
    batches = chunked(todo, a.batch_size)
    manifest = []
    for idx, batch in enumerate(batches, 1):
        bname = f"batch-{idx:02d}.md"
        bpath = os.path.abspath(os.path.join(a.out, "batches", bname))
        lines = [
            f"# Draft Transcription Batch {idx} ({len(batch)} pages)",
            "",
            f"1. First read the transcription rules and markup specification in `{prompt_abs}`.",
            "2. For each page listed below, inspect the scan image directly with `view_file` (do NOT use IA's `_djvu.txt` or OCR files; transcribe strictly from the visual scan) and write the exact page-markup transcription to its output `.txt` file using `write_to_file`.",
            "3. Watch carefully for two known pitfalls: NEVER modernize or normalize unusual/old spellings (e.g. keep `neophite`, `shew`, `connexion`, `to-day` exactly as printed), and keep roman parentheses/brackets OUTSIDE `<i>…</i>` tags.",
            f"4. If the platform blocks outputting any page due to a recitation/content filter, do NOT retry or rephrase that page; instead append `{{\"page\": \"<stem>\", \"error\": \"recitation\"}}` to `{os.path.abspath(os.path.join(a.out, 'log.jsonl'))}` and continue to the next page.",
            "",
            "## Pages in this batch",
            "",
        ]
        for stem, img_p, out_p in batch:
            lines.append(f"- `{stem}`: image `{img_p}` -> write `{out_p}`")
        Path(bpath).write_text("\n".join(lines) + "\n", encoding="utf-8")
        manifest.append({"batch": idx, "file": bpath, "pages": [x[0] for x in batch]})
    Path(os.path.join(a.out, "batches", "manifest.json")).write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"prepare-draft: {len(todo)} todo of {len(imgs)} pages -> {len(batches)} batch(es) in {os.path.join(a.out, 'batches')}")


def cmd_check_draft(a):
    imgs = list_images(a.images, a.pages)
    done, missing = [], []
    for f in imgs:
        stem = os.path.splitext(f)[0]
        p = os.path.join(a.out, stem + ".txt")
        if os.path.exists(p) and os.path.getsize(p) > 0:
            done.append(stem)
        else:
            missing.append(stem)
    log_p = os.path.join(a.out, "log.jsonl")
    logged = set()
    refused = []
    if os.path.exists(log_p):
        for ln in open(log_p, encoding="utf-8"):
            if ln.strip():
                d = json.loads(ln)
                logged.add(d.get("page"))
                if d.get("error"):
                    refused.append(d["page"])
    with open(log_p, "a", encoding="utf-8") as lf:
        for stem in done:
            if stem not in logged:
                lf.write(json.dumps({"page": stem, "model": "gemini-pro", "cost": 0.0}) + "\n")
    print(f"check-draft: {len(done)}/{len(imgs)} complete; missing={missing}; refused={refused}")
    if missing:
        sys.exit(1)


def cmd_prepare_verify(a):
    os.makedirs(os.path.join(a.out, "batches"), exist_ok=True)
    prompt_abs = os.path.abspath(a.prompt)
    drafts = sorted(f[:-4] for f in os.listdir(a.draft) if re.fullmatch(r"p\d+[a-z]?\.txt", f))
    todo = []
    for stem in drafts:
        corr_p = os.path.join(a.out, stem + ".corr")
        if os.path.exists(corr_p) and os.path.getsize(corr_p) > 0:
            continue
        img_p = next((os.path.abspath(os.path.join(a.images, stem + ext))
                      for ext in (".jpg", ".jpeg", ".png")
                      if os.path.exists(os.path.join(a.images, stem + ext))), None)
        if img_p:
            todo.append((stem, img_p, os.path.abspath(os.path.join(a.draft, stem + ".txt")), os.path.abspath(corr_p)))
    batches = chunked(todo, a.batch_size)
    manifest = []
    for idx, batch in enumerate(batches, 1):
        bname = f"batch-{idx:02d}.md"
        bpath = os.path.abspath(os.path.join(a.out, "batches", bname))
        lines = [
            f"# Second-Pass Verification Batch {idx} ({len(batch)} pages)",
            "",
            f"1. Read `{prompt_abs}` carefully.",
            "2. For each page below, view the scan image (`view_file`) AND view the draft `.txt` file (`view_file`), comparing every word, letter, punctuation mark, italic/small-caps tag, heading, paragraph join (`[[cont]]`), and footnote against the scan.",
            "3. Write ONLY the corrections output to the `.corr` file: either the single word `NONE` if the draft matches the scan under the rules, or one JSON object per line: `{\"find\": \"exact unique substring from draft\", \"replace\": \"corrected text\"}`.",
            "4. Never modernize old spellings (`shew`, `connexion`, `to-day`), and never pull roman brackets/parentheses inside `<i>…</i>`.",
            "",
            "## Pages in this batch",
            "",
        ]
        for stem, img_p, draft_p, corr_p in batch:
            lines.append(f"- `{stem}`: image `{img_p}` | draft `{draft_p}` -> write `{corr_p}`")
        Path(bpath).write_text("\n".join(lines) + "\n", encoding="utf-8")
        manifest.append({"batch": idx, "file": bpath, "pages": [x[0] for x in batch]})
    Path(os.path.join(a.out, "batches", "manifest.json")).write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"prepare-verify: {len(todo)} todo of {len(drafts)} draft pages -> {len(batches)} batch(es) in {os.path.join(a.out, 'batches')}")


def cmd_apply_verify(a):
    os.makedirs(a.out, exist_ok=True)
    drafts = sorted(f[:-4] for f in os.listdir(a.draft) if re.fullmatch(r"p\d+[a-z]?\.txt", f))
    missing, total_applied, total_skipped = [], 0, 0
    recs = []
    for stem in drafts:
        corr_p = os.path.join(a.out, stem + ".corr")
        if not os.path.exists(corr_p):
            missing.append(stem)
            continue
        dtext = open(os.path.join(a.draft, stem + ".txt"), encoding="utf-8").read()
        raw = open(corr_p, encoding="utf-8").read()
        vtext, n_app, sk = corrections.apply(dtext, raw)
        open(os.path.join(a.out, stem + ".txt"), "w", encoding="utf-8").write(vtext)
        total_applied += n_app
        total_skipped += len(sk)
        recs.append({"page": stem, "model": "gemini-flash", "corrections": n_app, "skipped": sk, "cost": 0.0})
    with open(os.path.join(a.out, "log.jsonl"), "w", encoding="utf-8") as lf:
        for r in recs:
            lf.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"apply-verify: {len(recs)}/{len(drafts)} pages written, {total_applied} corrections applied, {total_skipped} skipped; missing={missing}")
    if missing:
        sys.exit(1)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("prepare-draft"); p.add_argument("--images", required=True); p.add_argument("--prompt", required=True); p.add_argument("--out", required=True); p.add_argument("--pages"); p.add_argument("--batch-size", type=int, default=25); p.set_defaults(f=cmd_prepare_draft)
    p = sub.add_parser("check-draft"); p.add_argument("--images", required=True); p.add_argument("--out", required=True); p.add_argument("--pages"); p.set_defaults(f=cmd_check_draft)
    p = sub.add_parser("prepare-verify"); p.add_argument("--images", required=True); p.add_argument("--draft", required=True); p.add_argument("--prompt", required=True); p.add_argument("--out", required=True); p.add_argument("--batch-size", type=int, default=25); p.set_defaults(f=cmd_prepare_verify)
    p = sub.add_parser("apply-verify"); p.add_argument("--draft", required=True); p.add_argument("--out", required=True); p.set_defaults(f=cmd_apply_verify)
    a = ap.parse_args()
    a.f(a)


if __name__ == "__main__":
    main()
