---
name: digitize-novel
description: Transcribe a qualifying 1700–1914 English novel from its Internet Archive scan(s), combine multi-volume works into a single digital volume, verify via multi-pass Gemini Pro + Flash + preflight + blind sampled audit, and publish on the Forgotten Novels site (HTML, EPUB, ODT, JSON).
---

# Digitize a novel

Follow `notes/workflow.md` stage by stage. Rules: `GEMINI.md`. Editorial & structural conventions: `notes/style.md` and `notes/book-json.md`.

## 1. Before spending model calls

1. Re-verify eligibility (`notes/selection.md` §“Before starting”). Mark the novel’s row in `data/queue.json` `"in progress"` with `"started": "YYYY-MM-DD"`.
2. Fetch once from IA (`tools/ia.py fetch`) into `/tmp/novels/<slug>/src` (or `src-v1`, `src-v2`, `src-v3` for multi-volume novels), prepare working greyscale leaves (`tools/prep_pages.py`, using `--offset 1000`, `--offset 2000`… for Volumes II, III…), and generate contact sheets (`tools/contact_sheets.py`).
3. **Inspect EVERY contact sheet** and at least a dozen full-size leaves across the novel (via `view_file` or a `pro` subagent). Any missing, duplicated, clipped, or unreadable text page stops work until patched from another scan of the same edition (`source.extra_leaves`) or rejected.
4. Write the complete leaf/page map in `wip/<slug>/log.md`; pack and upload the working leaves to Tom’s Google Drive folder **“19C Novels”** (`tools/drive_cache.py pack` + `tools/drive_cache.py upload`); extract `--full` colour leaves for `images/cover.jpg` (cover if title is clearly readable, else Vol. I title page) and any illustrations/ornaments (`tools/crop_image.py`). Commit and push `wip/<slug>/`.

## 2. Multi-pass transcription & verification

1. **Draft (`Model: "pro"`):** run `tools/ocr_batch.py prepare-draft` (leaving out colour cards, blank endpapers, and untitled outer boards via `--pages`) and launch parallel **Gemini Pro** subagents (`invoke_subagent` with `Model: "pro"`). If any page hits a recitation block, run `tools/ocr_fallback.py` immediately (never retry or type refused pages in the session). Run `tools/ocr_batch.py check-draft` and `tools/normalize.py wip/<slug>/draft`. Commit and push.
2. **Second pass (`Model: "flash"`):** run `tools/ocr_batch.py prepare-verify` and launch parallel **Gemini Flash** subagents (`invoke_subagent` with `Model: "flash"`). Run `tools/ocr_batch.py apply-verify` and `tools/normalize.py wip/<slug>/verify`.
3. **Review & blind judge (`Model: "pro"`):** run `tools/review.py wip/<slug>/draft wip/<slug>/verify --out wip/<slug>/spots.json`. Check every unapplied correction, length outlier, and `[[cont]]` change against the scan. Run `tools/judge.py --prepare` and launch a fresh **Gemini Pro** subagent (`Model: "pro"`) on `wip/<slug>/judge/tasks/INSTRUCTIONS.md`, then `tools/judge.py --apply` and `tools/normalize.py wip/<slug>/judge`. Copy `judge/p*.txt` to `wip/<slug>/pages/`.
4. **Scan-crop spot checks:** inspect every item in `judge/report.txt`, plus `preflight.py`’s observe lists (`misprints`, `rare-forms`, `missing-stop`, `accents`, `italic-brackets`, `openings`, `joins`, `hyphen-joins`) and special pages (title page, verse, foreign phrases, footnotes) on scan crops (`tools/crop_spot.py`).

## 3. Structure, multi-volume handling, and metadata

- **Single vs. multi-volume:**
  - Single volume: `divisions` marks Volume I / the book’s title page as `{"at": "pNNNN", "kind": "titlepage"}`, plus `contents`, `preface`, `advertisements`, etc.
  - Multi-volume (“three-decker”): Volume I’s title page is `{"at": "p00NN", "kind": "titlepage"}`; Volumes II, III… title pages and front matter are `{"at": "p10NN", "kind": "front", "reading": false}` (kept in JSON only); Volumes I, II, III… appear as `part` divisions (either from their printed half-title/`# Volume I` pages via `divisions` or via `"parts": [{"before": "p00NN", "title": "Volume I"}, …]`), keeping each volume’s own chapter numbering underneath!
- **Metadata (`book.json`):** `setting`, `period` (when the story takes place), `volumes`, plain factual `summary` (60–150 words, no praise, serial commas, curly quotes), `omitted_from_reading`, `notes_on_text`.

## 4. Preflight, blind sampled audit, and publish

1. Run `python3 tools/preflight.py wip/<slug>` — fix every real issue in `pages/` or `book.json` until all enforced checks pass (`0 to fix`).
2. Run `python3 tools/audit_sample.py --pages-dir wip/<slug>/pages --images $B/pages --out wip/<slug>/audit --rules prompts/transcribe.md --prepare` and invoke a fresh **Gemini Pro** subagent (`Model: "pro"`) strictly on `wip/<slug>/audit/blind/INSTRUCTIONS.md`. Then run `audit_sample.py ... --score`, inspect every reported candidate on the scan, fix any real transcription error or mark any unmistakable printer’s error (`[[corr printed|corrected]]`), and record `"audit"` in `book.json`.
3. Re-run `python3 tools/preflight.py wip/<slug>` -> must end `PASS`.
4. Visually inspect built HTML pages (title page, book index page, several chapter openings, display controls).
5. Run `python3 tools/publish.py <slug>` and `python3 tools/carousel.py add <slug> --kind cover|title|page`.
6. Record the run in `books/<slug>/log.md` and `notes/metrics.md`, run `tools/run_tests.sh` and `tools/ledger.py check`, commit, push, merge to `main`, and verify the GitHub Pages + GitHub Releases deployment succeeded.
