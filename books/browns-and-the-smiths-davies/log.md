# The Browns and the Smiths — Christiana Jane Davies (1863)

IA: `brownssmithsintw01davi` (Vol. I, 328 leaves) and `brownssmithsintw02davi` (Vol. II, 334 leaves), University of Illinois Urbana-Champaign, 500 ppi.
Eligibility: checked 2026-11-26 (`data/queue.json`, blog_2021 #21): original English novel (1863, 2 vols.), complete UIUC `_jp2.zip` scans for both volumes, not on Project Gutenberg, Standard Ebooks, Wikisource, Faded Page, Celebration of Women Writers, VWWP, or Online Books Page; no post-1914 print edition; author Christiana Jane Davies (née Douglas, 1822–1887).

## Status
Stage reached: Published (`v2`) | Next step: none.

## Page map
- **Volume I (`p0000`–`p0327`)**:
  - `p0000` hidden delete; `p0001` untitled cloth cover; `p0002`–`p0004` pastedown (UIUC bookplate) & blank flyleaf (omitted).
  - `p0005` half-title (`THE BROWNS AND THE SMITHS.`); `p0006` blank verso; `p0007` title page (`VOL. I.`); `p0008` printer’s imprint verso (`R. Gardner`).
  - `p0009`–`p0319` = printed pp. [1]–311 (offset `+8`), Chapters I–XVI (`p0009`, `p0028`, `p0058`, `p0082`, `p0099`, `p0109`, `p0135`, `p0172`, `p0194`, `p0208`, `p0219`, `p0232`, `p0253`, `p0268`, `p0287`, `p0301`), ending `END OF VOL. I.` on `p0319` (printed p. 178 misnumbered `176` on `p0186`).
  - `p0320`–`p0322` blank flyleaf/pastedown & back cover; `p0323`–`p0327` hidden cards (omitted).
- **Volume II (`p1000`–`p1333`)**:
  - `p1000` hidden delete; `p1001` untitled cloth cover; `p1002`–`p1004` pastedown & blank flyleaf (omitted; no half-title in Vol. II).
  - `p1005` title page (`VOL. II.`); `p1006` printer’s imprint verso.
  - `p1007`–`p1315` = printed pp. [1]–309 (offset `+6`), Chapters I–XIII (`p1007`, `p1029`, `p1053`, `p1067`, `p1093`, `p1116`, `p1142`, `p1164`, `p1177`, `p1200`, `p1227`, `p1253` [printed `CHAPTER IX.` for `XII.`], `p1287`), ending `REQUIESCAT IN PACE.` on `p1315`.
  - `p1316` blank verso; `p1317`–`p1324` Hurst and Blackett publisher’s advertisements (8 unnumbered pages, transcribed for JSON only).
  - `p1325`–`p1333` blank pastedown, back cover, and trailing cards (omitted).
- **Illustrations / ornaments**: none in either volume; `images/cover.jpg` cropped from Vol. I title page `p0007` (`599×1000`, visually verified; cloth covers `p0001` and `p1001` have no lettering).
- **Scan check (2026-11-26)**: all 17 contact sheets and 28 sample full-page leaves visually checked; 0 missing, blurred, clipped, or folded leaves; harmless pencil margin notes on `p0009`, `p0028`, `p1007`, `p1109`, `p1123`, `p1199`, `p1323` omitted.

## Decisions
- Combined two-volume novel into a single digital edition opening with Volume I’s title page (`p0007`), keeping Volume I’s half-title (`p0005`), Volume II’s title page (`p1005`–`p1006`), and Volume II’s publisher advertisements (`p1317`–`p1324`) in the JSON only, and grouping each volume’s chapters under `Volume I` (`before: p0009`) and `Volume II` (`before: p1007`) Part headings (Tom, 2026-11-26).
- Credited Christiana Jane Davies (`1822–1887`), noting in `notes_on_text` that the 1863 edition was published anonymously (“By the Author of ‘Anne Dysart,’ ‘Onwards,’ &c., &c.”).
- Added `"keep_hyphens": ["p0014"]` (`man-servant`, matching hyphenated `maid-servants` in the novel).
- Marked 25 scan-verified unmistakable printer’s errors with `[[corr printed|corrected]]`: `p0028` `Thoms`→`Thomas`, `p0043` `keenlyh erself`→`keenly herself`, `p0055` `uumbers`→`numbers`, `p0076` `her`→`her.`, `p0087` `six`→`six.`, `p0096` `impatience.”`→`impatience.`, `p0162` `humble,`→`humble`, `p0176` `then`→`than`, `p0202` `Ye—yes,”`→`“Ye—yes,”`, `p0203` `wicked`→`wicked.`, `p0206` `Clara!’”`→`Clara!”`, `p0211` `from, it`→`from it,`, `p0245` `thens he`→`then she`, `p0257` `detestable.”`→`detestable.`, `p0259` `now,`→`now.`, `p0264` `her.`→`her,`, `p1109` `Egdar`→`Edgar` and `provoking`→`provoking.`, `p1123` `ihsufficient`→`insufficient`, `p1181` `“It`→`It`, `p1193` `aud`→`and`, `p1236` `if`→`it`, `p1243` `lectures.`→`lectures.”`, `p1253` `# Chapter IX.`→`# Chapter XII.`, and `p1317` `William,”`→`William,`. Magnified crops confirmed `countenance` (`p0054`, thin-topped `n`) and broken-tailed commas on `p0211` (`please, Miss`) and `p1167` (`astonishment, he`).

## Runs
| Stage | Date | Model | Pages | Notes |
|---|---|---|---|---|
| Draft | 2026-11-26 | `gemini-pro` | 635 (`p0005`–`p0319`, `p1005`–`p1324`) | 12 batches; 0 recitation blocks (`ocr_fallback.py` not needed); 0 `〓` marks |
| Verify | 2026-11-26 | `gemini-flash` | 635 | 12 batches; 39 changes applied (`0` unapplied, `0` outliers) -> 31 spots on 14 pages |
| Judge | 2026-11-26 | `gemini-pro` (blind A/B) | 14 (31 spots) | `verified`: 28, `draft`: 1, `neither`: 2; scan crops overturned 1 false misprint (`p0054` `countenance`) and settled 2 ad `<sc>` lines (`p1320`, `p1322`) |
| Audit | 2026-11-26 | `gemini-pro` (blind) | 6 (`p0080`, `p0138`, `p0198`, `p1110`, `p1193`, `p1318`) | Planted-error recall `28/30` (`93%`); `0` candidate real errors (`candidates.tsv` empty) |

## Versions
| Version | Date | Preflight stamp | Audit | Notes |
|---|---|---|---|---|
| 1 | 2026-11-26 | `preflight PASS: browns-and-the-smiths-davies v1 — 0 to fix, 0 waived … tools@b293dbc 2026-11-26` | 6 pages (`p0080`, `p0138`, `p0198`, `p1110`, `p1193`, `p1318`), recall `28/30` (`93%`), `0` real errors | First publication |
| 2 | 2026-11-26 | `preflight PASS: browns-and-the-smiths-davies v2 — 0 to fix, 0 waived … tools@d9cf8f1 2026-11-26` | Carried from v1 (no page text changed; compiler rebuild) | Fixed page-break hyphen joining inside italic tags (`p0009`–`p0010`, *ad nauseam*; GitHub #2) |
