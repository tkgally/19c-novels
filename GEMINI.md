# 19c-novels (Forgotten Novels) — working instructions for Gemini

A long-running public project of Tom Gally’s: accurate, readable digital editions of lesser-known and forgotten novels written in English and published between 1700 and 1914, transcribed by Gemini models from scans at the Internet Archive (IA) and published on this repository’s website (`https://tkgally.github.io/19c-novels/`) as HTML, EPUB, ODT, and JSON, in the public domain (CC0). Gemini chooses the novels, does the work, and keeps improving the method. The repository and the site are **public**: everything committed here can be read by anyone.

## Read first, every session

1. `notes/README.md` (index of the notes) and `python3 tools/ledger.py` (the state of `data/queue.json`, the ledger of novels).
2. `notes/workflow.md` — the pipeline and §Verification; `notes/lessons.md` — “Always” plus the sections whose trigger matches the novel; `notes/preferences.md` — what Tom has decided.
3. The skill for the job: `digitize-novel` (transcribe and publish), `select-novel` (choose and vet candidates).
4. `wip/<slug>/log.md` or `books/<slug>/log.md` if the novel has been worked on before.

Routine sessions start from `RESUME.md`. A session normally does several pieces of work, more than one novel where possible, and stops by its context budget (`RESUME.md` §3, `tools/session_meter.py`).

## Hard rules

- **Eligibility is checked before any work on a novel** (`notes/selection.md`):
  1. Complete, readable scan(s) of every volume on IA (`_jp2.zip` or `_jp2.tar`).
  2. Novel written in English (not a translation), published between 1700 and 1914 (`1700 <= year <= 1913`).
  3. No free digital reading edition elsewhere (Project Gutenberg, Standard Ebooks, Wikisource, Faded Page, A Celebration of Women Writers, etc.; raw OCR and scholarly/subscription databases such as EEBO-TCP and ECCO-TCP do not disqualify).
  4. No real print edition after 1914 (print-on-demand scan reprints do not count).
  5. Every author, artist, and illustrator of a book published before 1914 is assumed to have died more than 70 years ago (Tom, 2026-11-26).
  Note: the fifty novels in `data/blog_2021.json` (from Tom’s 2021 IA blog post) are a starting seed list **only if they still qualify** under all four rules above. Record what was checked in `data/queue.json`. If a published novel is later found to fail a criterion, tell Tom; do not silently remove it.
- **Multi-volume novels (“three-deckers” and other sets) are published as single digital volumes** (Tom, 2026-11-26): the reading editions (HTML, EPUB, ODT) open with Volume I’s title page, present Volumes I, II, III… as `part` divisions keeping each volume’s own chapter numbering underneath, and keep later volumes’ title pages and front matter in the JSON only (`notes/style.md`, `notes/book-json.md`).
- **Scans never enter the repo.** IA downloads, page images, crops in progress, and scratch files live in `/tmp` or the session scratchpad (each download in its own directory; treat archives as untrusted data). Only illustration and cover crops that the novel needs go in `…/<slug>/images/`. `.gitignore` is a backstop, not the rule.
- **Ask IA for a novel’s files once.** After the first download, the working page images are cached in Tom’s Google Drive folder **“19C Novels”** (id `1ecaIjeQldRJ8cfAD1-mGtNbofezQLbcy`, one subfolder per novel slug) via `tools/drive_cache.py`, and later sessions fetch them from there. Never delete or change another novel’s files in Drive.
- **Models (`invoke_subagent`).** Never a single-model text; never the same model as both writer and sole checker:
  - **Gemini Pro** (`Model: "pro"`) for primary page drafts (`ocr_batch.py prepare-draft`), blind A/B spot judging (`judge.py`), scan-crop spot-reads, and blind planted-error audits (`audit_sample.py`).
  - **Gemini Flash** (`Model: "flash"`) for the independent second-pass letter-by-letter proofreading (`ocr_batch.py prepare-verify`).
- **Recitation / output filter.** If any page is blocked by an automated recitation filter during direct drafting, never retry or rephrase it and never type out whole book pages in the main session: run `tools/ocr_fallback.py` (local `tesseract` OCR + Gemini Pro JSONL corrections against the scan), name the fallback pages in `log.md` and `notes_on_text`, and include them in the audit. A page that fails there too sends the novel to `waiting`.
- **The text policy** (`notes/style.md`) is not varied novel by novel: the author’s words, spelling, capitals, and punctuation marks as printed; spacing around punctuation modern; never silently normalize unusual spellings (`neophite`, `shew`, `connexion`, `to-day`); keep roman brackets/parentheses outside `<i>…</i>`; only unmistakable printer’s errors corrected, each marked `[[corr printed|corrected]]`.
- **Never publish without** `tools/preflight.py` ending `PASS` (including W3C `epubcheck` and LibreOffice ODT conversion), a check of the rendered pages, the blind sampled audit (`tools/audit_sample.py`) with every candidate checked on the scan, the stamp and audit result written in the novel’s `log.md`, and a row added to `notes/metrics.md`. `tools/publish.py` refuses without `PASS`.
- **Checks are not edited by the work they judge.** Never publish a novel in the same session after changing a check or test that the novel failed (`notes/workflow.md` §“When a check is wrong”).
- **Tools change only with tests.** Run `tools/run_tests.sh` at the start of a working session and after any edit under `tools/`; every tool bug fixed gets a test in the same commit.
- **Site text is plain.** Summaries, notes, and page text say what a thing is in ordinary words: no praise, no selling, no “fascinating” or “forgotten masterpiece”, no claims unsupported by fact; serial commas and curly quotation marks (`notes/style.md` §Site text).
- **The site has no external dependencies**: no web fonts, external scripts, trackers, or CDNs. The only outside links/embeds are IA links, the optional lazy IA page viewer, and the EPUB and ODT downloads on GitHub Releases of `tkgally/19c-novels`.
- **Unfinished work is committed and pushed** as it goes (`wip/<slug>/`, `wip/<slug>/log.md`, queue row `in progress`).
- **Tom’s instructions and preferences** go in `notes/preferences.md` the moment he states them, **committed and pushed before acting on them**.
- **Never modify `tkgally/travel-books`.**

## Repo map

| Path | What |
|---|---|
| `books/<slug>/` | a published novel: `book.json`, `pages/pNNNN.txt`, `images/`, `source.json`, `log.md`, `preflight.txt` |
| `wip/<slug>/` | a novel in progress: the same, plus `draft/`, `verify/`, `judge/`, `audit/`; moved to `books/` by `tools/publish.py` |
| `data/queue.json` | the ledger: queued, in progress, published, waiting, rejected (`tools/ledger.py`) |
| `data/blog_2021.json` | the 50 novels from Tom’s 2021 IA blog post (seed candidates; each must still pass eligibility) |
| `data/published.json`, `data/carousel.json` | first-publication UTC timestamps; home-page cover carousel index |
| `tools/` | Get: `ia.py`, `prep_pages.py`, `drive_cache.py`, `contact_sheets.py`. Transcribe & verify: `ocr_batch.py`, `ocr_fallback.py`, `normalize.py`, `running_quotes.py`, `review.py`, `judge.py`, `crop_spot.py`, `crop_image.py`, `corrections.py`, `score.py`, `showdiff.py`. Session: `session_meter.py`. Build: `compile_book.py`, `render_html.py`, `render_epub.py`, `render_odt.py`, `build_site.py`, `releases.py`, `carousel.py`. **Verify: `run_tests.sh`, `preflight.py`, `audit_sample.py`.** Publish: `publish.py`. Ledger: `ledger.py`. Setup: `setup_env.sh`, `make_prompts.sh` |
| `prompts/` | `transcribe.md`, `verify.md`, built from `_rules.md`, `_format.md`, `_verify-task.md` by `tools/make_prompts.sh` |
| `site/` | `assets/` (`site.css`, `book.css`, `site.js`, `logo.svg`), `about.md`, `json-format.md`, `carousel/` |
| `tests/` | regression tests for all tools and an invented sample novel (`tests/sample/`) |
| `notes/` | Gemini’s memory: workflow, selection, style, page-markup, book-json, site, lessons, metrics, sessions, errata, preferences, improvement |
| `.agents/skills/` | `digitize-novel`, `select-novel` |
| `.github/workflows/pages.yml` | tests, build `_site/`, upload EPUB/ODT to GitHub Releases, and deploy to GitHub Pages on push to `main` |
