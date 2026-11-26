# By the Cornish Sea — John Isabell (1885)

IA: `bycornishsea01isab` (Vol. I, 318 leaves) and `bycornishsea02isab` (Vol. II, 358 leaves), University of Illinois Urbana-Champaign, 500 ppi.
Eligibility: checked 2026-11-26 (`data/queue.json`, blog_2021 #27): original English novel (1885, London: Sampson Low, Marston, Searle, & Rivington, 2 vols.), complete UIUC `_jp2.zip` scans for both volumes, not on Project Gutenberg, Standard Ebooks, Wikisource, Faded Page, or VWWP (Online Books Page links only to HathiTrust scans); no post-1914 print edition; author Rev. John Isabell (1851–1921).

## Status
Stage reached: Published (`v1`) | Next step: none.

## Page map
- **Volume I (`p0000`–`p0317`, 318 leaves)**:
  - `p0000` spine/delete; `p0001` plain embossed cloth cover (no lettering); `p0002` UIUC bookplate pastedown; `p0003`–`p0004` blank flyleaf (omitted; no half-title).
  - `p0005` title page (`VOL. I.`); `p0006` printer’s imprint verso (`Gilbert and Rivington, Limited`).
  - `p0007`–`p0008` Contents (`CONTENTS OF VOL. I.`, pp. [iii]–iv, Chapters I–XXIII).
  - `p0009`–`p0308` = printed pp. `[1]`–`300` (offset `+8`), Chapters I–XXIII, ending `END OF VOL. I.` and printer colophon on `p0308`.
  - `p0309`–`p0312` blank flyleaf/pastedown & back cover; `p0313`–`p0317` hidden cards (omitted).
- **Volume II (`p1000`–`p1357`, 358 leaves)**:
  - `p1000` spine/delete; `p1001` plain embossed cloth cover (no lettering); `p1002` UIUC bookplate pastedown; `p1003`–`p1004` blank flyleaf (omitted; no half-title).
  - `p1005` title page (`VOL. II.`); `p1006` printer’s imprint verso (`ST. JOHN’S SQUARF.` marked `[[corr SQUARF.|SQUARE.]]`).
  - `p1007`–`p1008` Contents (`CONTENTS OF VOL. II.`, pp. [iii]–iv, Chapters I–XXIII).
  - `p1009`–`p1316` = printed pp. `[1]`–`308` (offset `+8`), Chapters I–XXIII, ending `THE END.` and printer colophon on `p1316`.
  - `p1317`–`p1348` Sampson Low, Marston, Searle, & Rivington publisher’s catalogue (October, 1885; 32 pp., numbered `[1]`–`32`, transcribed for JSON only).
  - `p1349`–`p1357` blank flyleaf/pastedown, back cover, and hidden cards (omitted).
- **Illustrations / ornaments**: none (only typographic rules); `images/cover.jpg` cropped from Vol. I title page (`p0005`, `631×1000`, visually verified).
- **Scan check (2026-11-26)**: all 17 contact sheets and 32 full-size leaves visually inspected by Gemini Pro subagent; complete and crisp throughout, no missing, duplicated, clipped, or obscured pages; harmless library pencil marks on `p0004`, `p0007`, `p0009`, `p0160`, `p0308`, `p1007`, `p1009` omitted.

## Decisions
- Combined two-volume novel into a single digital edition opening with Volume I’s title page (`p0005`), keeping both printed tables of contents (`p0007`–`p0008`, `p1007`–`p1008`), Volume II’s title page (`p1005`–`p1006`), and the 32-page publisher’s catalogue (`p1317`–`p1348`) in the JSON only, and grouping each volume’s chapters under `Volume I` (`before: p0009`) and `Volume II` (`before: p1009`) Part headings.
- Added `"keep_hyphens": ["p0052", "p1039", "p1310"]` (`ill-repute`, `capstan-bars`, `hard-visaged`).
- Marked 20 scan-verified unmistakable printer’s errors with `[[corr printed|corrected]]`: `p0096` `tongues.`→`tongues.”`, `p0145` `now`→`“now`, `p0156` `Treleaven.`→`Treleaven.”`, `p0220` `Carnanton,`→`Carnanton.`, `p0300` `Craddock`→`Craddock.`, `p0304` `they.when`→`they when`, `p1006` `SQUARF.`→`SQUARE.`, `p1018` `again.”`→`again,”`, `p1080` `finger-ends,’`→`finger-ends,`, `p1099` `a a`→`a`, `p1123` `present.`→`present,`, `p1129` `I’il`→`I’ll`, `p1147` `shallsay`→`shall say`, `p1148` `ou`→`our`, `p1154` `Dunstable.”`→`Dunstable.`, `p1156` `Mr`→`Mr.`, `p1231` `white.`→`white,`, `p1253` `you’v`→`you’ve`, `p1291` `confessed. .`→`confessed.`, and `p1298` `romanticand`→`romantic and`. Magnified crop on `p0027` confirmed genuine dialect `diffikittles`.

## Runs
| Stage | Date | Model | Pages | Notes |
|---|---|---|---|---|
| Draft | 2026-11-26 | `gemini-pro` (+ `ocr_fallback.py`) | 648 (`p0005`–`p0308`, `p1005`–`p1348`) | 558 direct Pro draft + 90 Tesseract + Pro JSONL fallback (`p0059`–`p0065`, `p0067`, `p0070`, `p1011`–`p1025`, `p1035`–`p1040`, `p1042`, `p1044`, `p1054`–`p1056`, `p1077`–`p1078`, `p1089`–`p1132`, `p1162`–`p1167`, `p1194`, `p1196`–`p1197`); 0 `〓` |
| Verify | 2026-11-26 | `gemini-flash` | 648 | 12 batches; 30 corrections applied (`3` skipped on ad pages, `0` outliers, `1` `[[cont]]` verified on `p1193`) -> 15 spots on 14 pages |
| Judge | 2026-11-26 | `gemini-pro` (blind A/B) | 14 (15 spots) | `draft`: 5, `verified`: 10; magnified scan crops verified 22 spots (overturning `p1018` to `[[corr again.”|again,”]]` and confirming `p0027` `diffikittles`) |
| Audit | 2026-11-26 | `gemini-pro` (blind) | 7 (`p0063`, `p0073`, `p0103`, `p0301`, `p1108`, `p1303`, `p1342`) | Included 2 fallback pages (`p0063`, `p1108`); planted-error recall `34/35` (`97%`); `0` candidate real errors (`candidates.tsv` empty) |

## Versions
| Version | Date | Preflight stamp | Audit | Notes |
|---|---|---|---|---|
| 1 | 2026-11-26 | `preflight PASS: by-the-cornish-sea-isabell v1 — 0 to fix, 0 waived … tools@d22f398 2026-11-26` | 7 pages (`p0063`, `p0073`, `p0103`, `p0301`, `p1108`, `p1303`, `p1342`), recall `34/35` (`97%`), `0` real errors | First publication |
