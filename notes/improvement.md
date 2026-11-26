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
| 2026-11-26 | set-up | Adapted pipeline, renderers, preflight checks, website, and test suite from `travel-books` for 1700–1914 English novels (`Forgotten Novels`); added multi-volume `parts` and `--offset` support, `gdrive` CLI caching in “19C Novels”, `ocr_batch.py` + `ocr_fallback.py` for Gemini Pro/Flash subagents, and `italic-brackets` observe check from 2026-11-25 Gemini benchmark. |
