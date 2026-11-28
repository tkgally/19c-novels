# Country Houses — Charlotte Trimmer Moore (1832)

IA: `countryhouses01moor`, `countryhouses02moor`, `countryhouses03moor` (University of Illinois Urbana-Champaign; 1,114 leaves total at 500 ppi: 338 + 380 + 396).
Eligibility: re-checked 2026-11-27: original English novel published anonymously in 1832 (London: Saunders and Otley, 3 vols., first edition). Front flyleaf provenance note on `p0008` by Robert Henry Hobart Cust identifies the author as his great-grandmother Mrs. Richard Moore (née Charlotte Trimmer, 1763–1836, eldest daughter of Sarah Trimmer). Complete 500 ppi UIUC scans with `_jp2.zip` for all three volumes. No free digital reading edition on Project Gutenberg, Standard Ebooks, Wikisource, Faded Page, Celebration of Women Writers, VWWP, or Penn Online Books Page. No post-1914 reset print edition (only POD scan reprints). Charlotte Trimmer Moore (1763–1836) died >70 years ago (Rule 5 met).

## Status
Stage reached: Stage 4 complete (Flash verify, blind Pro judge, full scan-crop & 89-errata review, 227 `[[corr]]` marks, preflight 1 to fix = audit only) | Next step: Stage 5 blind sampled audit (7 pp incl. fallback `p2046`–`p2047`), HTML visual check, and publish.

## Page map
- **Volume I (`p0000`–`p0337`, 338 leaves):** `p0000` cradle · `p0001` plain dark library cover · `p0002` UIUC bookplate · `p0003`–`p0010` flyleaves (`p0008` Cust provenance note + presentation inscription `Miss Wylde from The Author` + Cust bookplate; `p0009` Cust ownership note) · `p0011` title page (`cover.jpg`, Burns epigraph) · `p0012` imprint verso (`B. BENSLEY, PRINTER, ANDOVER.`) · `p0013` blank errata recto (call no.) · `p0014` `ERRATA TO VOL. I.` (29 entries) · `p0015`–`p0326` body pp. [1]–312 (Ch. I–VIII pp. [1]–132, `p0146` blank verso; `EASTER HOLIDAYS, AT STOKE PARK.` Ch. I–XI pp. [133]–312, `END OF VOL I.` + colophon) · `p0327`–`p0337` flyleaves, back board, calibration cards.
- **Volume II (`p1000`–`p1379`, 380 leaves):** `p1000` cradle · `p1001` plain dark library cover · `p1002` UIUC bookplate · `p1003`–`p1010` flyleaves (`p1008` inscription + Cust bookplate; `p1009` Cust note) · `p1011` title page (`VOL. II.`) · `p1012` imprint verso · `p1013` blank errata recto · `p1014` `ERRATA TO VOL. II.` (31 entries) · `p1015`–`p1367` body pp. [1]–353 (`EASTER HOLIDAYS` Ch. XII–XIII pp. [1]–55, `p1070` blank verso `[56]`; `COUNTRY HOUSES.` / `CHAPTER I. / WINDING UP.` through Ch. XVII pp. [57]–353, `END OF VOL. II.` + colophon) · `p1368`–`p1379` blank verso, flyleaves, back board, calibration cards.
- **Volume III (`p2000`–`p2395`, 396 leaves):** `p2000`–`p2001` cradle & plain dark library cover · `p2002` UIUC bookplate · `p2003`–`p2008` flyleaves (`p2006` inscription + Cust bookplate; `p2007` Cust note) · `p2009` title page (`VOL. III.`) · `p2010` imprint verso · `p2011` blank errata recto · `p2012` `ERRATA TO VOL. III.` (29 entries) · `p2013`–`p2071` body pp. [1]–59 (Ch. XVIII–XX + `THE CONCLUSION.`) · `p2072` blank verso (`[60]`) · `p2073`–`p2377` body pp. [61]–365 (`COUNTRY HOUSES.` / `CHAPTER I. / OLD MAIDS AND BAS BLUES` through Ch. XII) · `p2378`–`p2384` `POSTSCRIPT.` pp. [366]–372 (`THE END.` + colophon) · `p2385`–`p2395` flyleaves, back board, calibration cards.

Scan check: all 28 contact sheets (`sheet-01.jpg`–`sheet-28.jpg`) and 115+ full-size leaves across all three volumes checked 2026-11-27 by two Gemini Pro inspectors; zero pagination jumps, zero duplicate leaves, zero missing/clipped/illegible body leaves.

## Decisions
- Volume I cover (`p0001`) is a plain dark library rebinding; Volume I title page (`p0011`) used for `images/cover.jpg`.
- Transcribe 1,043 printed leaves + 6 blank leaves (`p0013`, `p0146`, `p1013`, `p1070`, `p2011`, `p2072`) = 1,049 leaves total.
- No illustrations or pictorial ornaments in the printed book (only a swelled diamond rule on `p2375`).
- Printed errata lists (`p0014`, `p1014`, `p2012`; 89 entries total): 84 verified entries applied via `[[corr printed|corrected]]`; 5 entries (`Vol. I p. 305 l. 13`, `Vol. II p. 216 l. 24`, `Vol. III p. 131 l. 8`, `p. 190 l. 7`, `p. 279 l. 10`) do not match errors in this copy and were left unapplied. Errata leaves marked `reading: false` (JSON only).
- Repeated page-top `COUNTRY HOUSES.` drop-titles removed above `# Chapter I.`/`# Chapter XVIII.` (`p0015`, `p0147`, `p1071`, `p2013`, `p2073`), and `p0147` styled with `[[subtitle]] Easter Holidays, at Stoke Park.` to match the other three Chapter I restarts without leaking onto the preceding division.
- Two pages (`p2046`, `p2047`) triggered a recitation filter during direct Pro drafting and were drafted via `tools/ocr_fallback.py` (local `tesseract` + Pro JSONL corrections against scan, 0 skipped patches); both were verified by Flash and included in the Stage 5 audit.
- Magnified scan crops overturned 6 blind-judge verdicts (`p0141` `intreating`, `p0326` `B.`, `p1012` `B. Bensley, Printer, Andover.`, `p1186` `in`, `p2155` `scissars!`, `p2189` `c’es defendu`).

## Runs
| Stage | Date | Model | Pages | Notes |
|---|---|---|---|---|
| 1. Fetch & inspect | 2026-11-27 | Gemini Pro | 1,114 leaves | All 28 contact sheets + 115+ sample leaves verified clean; zero defects; cached to Drive |
| 2. Draft | 2026-11-27 | Gemini Pro | 1,043 + 6 blank | 42 batches, 2 fallback pages (`p2046`, `p2047` via `ocr_fallback.py`, 0 skipped patches), normalized |
| 3. Verify & judge | 2026-11-27 | Gemini Flash + Pro | 1,049 | 70 Flash changes (`0` skipped, `0` length outliers); 36 judge spots on 33 pp (`11` draft / `24` verified / `1` `neither`); 0 dropped lines in full `_djvu.txt` word-stream diff |
| 4. Scan crops & preflight | 2026-11-27 | Gemini Pro | 3 vols (100+ crops) | Applied 84/89 printed errata + 143 additional compositor typo/quote `[[corr]]` marks (227 total); overturned 6 judge spots (`p0141`, `p0326`, `p1012`, `p1186`, `p2155`, `p2189`); resolved all `[[cont]]`, `〓`, `quote-balance`, `verse-joins`, and `lowercase-after-stop` issues |

## Versions
| Version | Date | Preflight stamp | Audit | Notes |
|---|---|---|---|---|
