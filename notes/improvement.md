# How the method is improved

Every novel should leave the pipeline cleaner and sharper than it found it.

## In every session

- Turn any transcription miss or structural slip immediately into (1) a `preflight.py` check (starting in `observe`), (2) a regression test in `tests/test_tools.py`, or (3) a concise rule in `prompts/` or `notes/lessons.md` — in that order of preference.
- Record every published version in `notes/metrics.md`.
- Keep `RESUME.md` and `notes/workflow.md` aligned with actual practice.

## Review sessions (every fifth published novel, or when `metrics.md` shows a recurring issue)

1. **Error analysis:** tabulate audit candidates, scan-overturned judge spots, and errata by category (misread letter, modernized spelling, italic/small-caps tags, dialogue punctuation, chapter/volume structure, crops). Address the top category with a tool check, test, or prompt refinement.
2. **Stage evaluation:** check `metrics.md` — how many real catches did the Gemini Flash second pass make, how often did the scan overturn the Gemini Pro judge, and what was the audit recall?
3. **Preflight checks:** promote `observe` checks whose alarms are consistently real and clean; refine noisy ones (always with tests).
4. **Carousel & live site check:** run `python3 tools/carousel.py check`, verify `cover.jpg` readability, add thumbnails (`carousel.py add`), and verify the live site’s HTML structure, links, downloads, and accessibility.

## Review log

| Date | Novels covered | Findings and changes |
|---|---|---|
| 2026-11-26 | set-up | Adapted pipeline, renderers, preflight checks, website, and test suite from `travel-books` for 1700–1914 English novels (`Forgotten Novels`); added multi-volume `parts` and `--offset` support, `gdrive` caching in “19C Novels”, `ocr_batch.py` + `ocr_fallback.py` for Gemini Pro/Flash subagents, and `italic-brackets` observe check from 2026-11-25 Gemini benchmark. |
| 2026-11-27 | 5 novels (`browns-and-the-smiths-davies` v2, `by-the-cornish-sea-isabell` v1, `story-of-a-life-sherer` v1, `transgression-of-terence-clancy-vallings` v2, `middle-aged-lover-fitzgerald` v1) | **Metrics across 5 novels (3,510 transcribed leaves):** Flash second pass applied 203 corrections across all 5 books (catching wrong-page draft `p1223`, missing paragraph breaks, unclosed tags, and `[[cont]]` slips); blind Pro judge adjudicated 116 spots (`38` Pro / `75` Flash / `3` manual), with magnified scan crops overturning the judge twice (`browns` `p0054` thin-topped `n`, `middle-aged-lover` `p1273` uniform small caps); blind sampled audits totaled `152/159` planted-error recall (`95.6%`) across 32 pages (incl. 8 fallback pages) and `0` real residual errors; 2 post-publication errata (`browns` v2 inline-tag hyphen join, `terence-clancy` v2 missing `[[cont]]` on `p1152` caught during this review). **Changes (with 3 regression tests, 21/21 OK):** extended `quote-balance` to flag unclosed `“` when the next block does not continue a quotation; added `lowercase-after-stop` observe check (`0` false alarms across all 5 books); added skipped-patch `WARNING` to `ocr_fallback.py apply`. **Site/carousel check:** all 5 books pass `preflight.py`, `carousel.py check` clean (5/5), GitHub Pages and all 5 GitHub Releases live. |

## Candidate checks for next review

- **Word-stream completeness check (`_djvu.txt` vs. `pages/`):** consider a lightweight helper script (never copying text from `_djvu.txt`) to flag runs of ≥ 8 words present in `_djvu.txt` and missing from `pages/` during Stage 4, formalizing the manual check that caught a dropped page-end line on *The Story of a Life* (`p0277`).
- **Promote `italic-brackets` or `lowercase-after-stop`:** evaluate false-alarm rates after 10 published novels before promoting any `observe` check to `enforce`.
