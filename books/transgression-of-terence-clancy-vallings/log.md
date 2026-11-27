# The Transgression of Terence Clancy — Harold Vallings (1893)

IA: `transgressionoft02vall` (Vol. I, 338 scans), `transgressionoft01vall` (Vol. II, 290 scans), `transgressionoft03vall` (Vol. III, 310 scans) — University of Illinois Urbana-Champaign, 500 ppi (938 scans total; note IA Vol. I/II identifier swap).
Eligibility: re-checked 2026-11-26 via web search and `ia.py meta`: 1893 London Richard Bentley & Son first edition (3 vols.); only POD facsimile reprints (Hansebooks, Forgotten Books); no free digital reading edition elsewhere; no post-1914 trade/scholarly print edition; published before 1914 (Rule 5 met; biographical dates 1857–1940).

## Status
Stage reached: Published v1 (`books/transgression-of-terence-clancy-vallings/`, 2026-11-26).

## Page map
- **Vol. I (`p0000`–`p0337`, printed pp. 1–313, Chapters I–XV):** `p0000`–`p0004` outer/board/endpapers · `p0005` half-title · `p0006` blank · `p0007` title page (`Vol. I.`) · `p0008` blank · `p0009`–`p0325` body pp. 1–313 (excluding duplicate scans `p0132`–`p0133` [dups of pp. 122–123] and blurry/hand-occluded duplicates `p0322`–`p0323` [dups of pp. 310–311]) · `p0326`–`p0337` flyleaves/endpapers/back board/cards.
- **Vol. II (`p1000`–`p1289`, printed pp. 1–270, Chapters I–XII):** `p1000`–`p1004` outer/board/endpapers · `p1005` half-title · `p1006` blank · `p1007` title page (`Vol. II.`) · `p1008` blank · `p1009`–`p1278` body pp. 1–270 · `p1279`–`p1289` flyleaves/endpapers/back board/cards.
- **Vol. III (`p2000`–`p2309`, printed pp. 1–286, Chapters I–XII):** `p2000`–`p2004` outer/board/endpapers · `p2005` half-title · `p2006` blank · `p2007` title page (`Vol. III.`) · `p2008` blank · `p2009`–`p2298` body pp. 1–286 (excluding motion-blurred first scans `p2152`–`p2153` [replaced by `p2154`–`p2155`] and duplicate scans `p2284`–`p2285` [dups of pp. 272–273]; note `p2294`–`p2295` are the sole, legible scans of pp. 282–283 despite IA scandata `Delete` flags) · `p2299`–`p2309` flyleaves/endpapers/back board/cards.
- **Active leaves:** 881 page files (875 transcribed + 6 blank versos: `p0006`, `p0008`, `p1006`, `p1008`, `p2006`, `p2008`).
- Scan check: all 24 contact sheets and full-size sample leaves checked 2026-11-26; problems: none missing; 8 duplicate/re-shot leaves excluded; `p2294`–`p2295` verified legible.

## Decisions
- Front cloth boards are blind-stamped without lettering; Volume I’s red-and-black title page (`p0007`) is used as `images/cover.jpg`.
- Repeating generic printer’s stock insect headpieces/tailpieces and title-page device are omitted from the text; repeating drop-title headers above `# Chapter I.` on `p0009`, `p1009`, `p2009` are omitted so Volume I’s title page opens cleanly.
- All 39 chapter openings use full capitals after the 2-line drop cap (verified on scan).
- 435 pages (mostly Volumes II–III) hit automated recitation blocks during direct drafting and were drafted via `tools/ocr_fallback.py` (local Tesseract + Gemini Pro JSONL corrections), then checked by Gemini Flash second-pass verification and blind Pro spot-judging; 3 fallback pages (`p1179`, `p1209`, `p2054`) were included in the blind sampled audit.

## Runs
| Stage | Date | Model | Pages | Notes |
|---|---|---|---|---|
| Draft | 2026-11-26 | Gemini Pro (+ `ocr_fallback.py`) | 875 | 440 direct + 435 via `ocr_fallback.py` (incl. `p1223` caught as wrong-page draft by Flash); normalized |
| Second pass | 2026-11-26 | Gemini Flash | 875 | 60 corrections applied, 0 skipped; caught `p1223` wrong-page draft and printed typos |
| Blind judge | 2026-11-26 | Gemini Pro | 32 (34 spots) | 17 Flash / 16 Pro / 1 manual; 31 scan spots visually verified; full `_djvu.txt` word-stream diff showed 0 dropped lines |
| Blind audit | 2026-11-26 | Gemini Pro | 6 (`p0069`, `p0091`, `p1179`, `p1209`, `p2054`, `p2228`) | 28/29 planted errors caught (97% recall), 0 real errors (3 direct + 3 fallback pages across all 3 vols.) |

## Versions
| Version | Date | Preflight stamp | Audit | Notes |
|---|---|---|---|---|
| 1 | 2026-11-26 | `preflight PASS: transgression-of-terence-clancy-vallings v1 — 0 to fix, 0 waived — tools@34616f1 2026-11-27` | 6 pp, 28/29 (97%), 0 real errors | First publication; 3 vols. combined into 1 digital edition; 21 `[[corr]]` marks; 0 `〓` |
