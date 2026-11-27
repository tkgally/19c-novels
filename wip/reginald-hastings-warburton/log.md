# Reginald Hastings: Or, A Tale of the Troubles in 164— — Eliot Warburton (1850)

IA: `reginaldhastings01warb`, `reginaldhastings02warb`, `reginaldhastings03warb` (University of Illinois Urbana-Champaign; 1,032 leaves total at 500 ppi: 368 + 342 + 322).
Eligibility: re-checked 2026-11-27: original English historical novel published in 1850 (London: Henry Colburn, 3 vols., first edition). Complete 500 ppi UIUC scans with `_jp2.zip` for all three volumes. No free digital reading edition on Project Gutenberg, Standard Ebooks, Wikisource, Faded Page, or Penn Online Books Page (scan images only). No post-1914 reset print edition (only POD scan reprints). Eliot Warburton (1810–1852) died >70 years ago (Rule 5 met).

## Status
Stage reached: Stages 3–4 complete (Flash verify, blind Pro judge, 64 magnified scan crops + 18 full-page spot-reads, word-stream diff, 42 `[[corr]]` marks, preflight 0 structural issues pending audit) | Next step: Stage 5 blind planted-error audit (`audit_sample.py`) and publication.

## Page map
- **Volume I (`p0000`–`p0367`, 368 leaves):** `p0000` cradle · `p0001` library cover (no printed title) · `p0002`–`p0006` marbled endpapers & UIUC circulation slip · `p0007` title page (`cover.jpg`) · `p0008` imprint verso (`Schulze & Co.`) · `p0009` Dedication (`To the Rev. Walter Halliday, of Glenthorne`) · `p0010` blank verso (IA card) · `p0011`–`p0014` Introduction (pp. [v]–viii, dated March 20, 1850) · `p0015`–`p0019` body pp. [1]–5 · `p0020`–`p0021` Delete (blurry duplicates of pp. 6–7) · `p0022`–`p0355` body pp. 6–339 (`END OF VOL. I.` + colophon) · `p0356` back ad (Colburn novels) · `p0357`–`p0367` flyleaves, marbled endpapers, back board, calibration cards.
- **Volume II (`p1000`–`p1341`, 342 leaves):** `p1000`–`p1008` cradle, covers, marbled endpapers, UIUC slip, IA card · `p1009` half-title · `p1010` blank verso · `p1011` title page · `p1012` imprint verso · `p1013`–`p1097` body pp. [1]–85 · `p1098`–`p1099` Delete (uncropped duplicates of pp. 86–87) · `p1100`–`p1329` body pp. 86–315 (`END OF VOL. II.` + colophon with printed `Printsd`) · `p1330` back ad (*The Crescent and the Cross*) · `p1331`–`p1341` flyleaves, marbled endpapers, back board, calibration cards.
- **Volume III (`p2000`–`p2321`, 322 leaves):** `p2000`–`p2006` cradle, cover, marbled endpapers, UIUC slip, IA card · `p2007` title page · `p2008` imprint verso · `p2009`–`p2059` body pp. [1]–51 · `p2060`–`p2061` Delete (blurry/hand-obscured duplicates of pp. 50–51) · `p2062`–`p2310` body pp. 52–300 (`THE END.` + colophon) · `p2311`–`p2321` flyleaves, marbled endpapers, back board, calibration cards.

Scan check: all 26 contact sheets (`sheet-01.jpg`–`sheet-26.jpg`) and 40+ full-size leaves across all three volumes checked 2026-11-27 by Gemini Pro inspector; text continuous across all three Delete pairs (`p0019`→`p0022`, `p1097`→`p1100`, `p2059`→`p2062`); zero missing, clipped, or illegible body leaves.

## Decisions
- Volume I cover is a plain UIUC library rebinding; Volume I title page (`p0007`) used for `images/cover.jpg`.
- Transcribe 968 printed leaves (`p0007`–`p0009`, `p0011`–`p0019`, `p0022`–`p0356`, `p1009`, `p1011`–`p1097`, `p1100`–`p1330`, `p2007`–`p2059`, `p2062`–`p2310`) plus 2 blank versos (`p0010`, `p1010`).
- Preserve printed chapter-numbering irregularity in Volume I (`p0253` restarts at `CHAPTER XV.`, skips `XIX`, ends `CHAPTER XXI.`) and document in `notes_on_text`.
- Magnified scan crops overturned 3 blind-judge readings (`p1321` `countenance`, `p2178` & `p2179` `portress`) plus `p0334` `mêlée` and `p2205` `upon` (broken descender on `p`). Extended `quote-balance` caught 2 missed `[[cont]]` continuations (`p0200`, `p0202`) and 10 compositor quotation-mark errors.

## Runs
| Stage | Date | Model | Pages | Notes |
|---|---|---|---|---|
| 1. Fetch & inspect | 2026-11-27 | Gemini Pro | 1,032 leaves | All 26 contact sheets + sample leaves verified clean; 6 Delete duplicates confirmed continuous |
| 2. Draft | 2026-11-27 | Gemini Pro | 968 + 2 blank | 39 batches, 0 recitation blocks, normalized |
| 3. Verify & judge | 2026-11-27 | Gemini Flash + Pro | 970 | 46 Flash changes (`0` skipped, `0` length outliers); 37 judge spots on 31 pp (`11` draft / `25` verified / `1` `neither`); 0 dropped lines in full `_djvu.txt` word-stream diff |
| 4. Scan crops & preflight | 2026-11-27 | Gemini Pro | 64 crops + 18 pp | Overturned 3 judge spots (`p1321`, `p2178`, `p2179`), fixed `p0066` false split, added `[[cont]]` on `p0200`/`p0202`, marked 42 `[[corr]]` printer errors, verified front matter & Fraktur epigraphs (`p1088`, `p2210`) |

## Versions
| Version | Date | Preflight stamp | Audit | Notes |
|---|---|---|---|---|
