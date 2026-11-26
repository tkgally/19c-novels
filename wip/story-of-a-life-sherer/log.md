# The Story of a Life — Joseph Moyle Sherer (1825)

IA: `storyoflife01sher` (Vol. I, 344 leaves) and `storyoflife02sher` (Vol. II, 382 leaves), University of Illinois Urbana-Champaign, 500 ppi.
Eligibility: re-checked 2026-11-26 (`data/queue.json`, blog_2021 #37): original English novel published anonymously in 1825 (London: Longman, Hurst, Rees, Orme, Brown, and Green, 2 vols., first ed.), complete 500 ppi UIUC `_jp2.zip` scans for both volumes, not on Project Gutenberg (only *The Broken Font* is listed), Standard Ebooks, Wikisource, Faded Page, or Penn Online Books Page; no post-1914 trade/scholarly print edition (only print-on-demand scan replicas); author Joseph Moyle Sherer (1789–1869) died >70 years ago.

## Status
Stage reached: Stage 4 (Flash verify, blind Pro judge, 61 magnified scan-crop checks, structure & preflight `0` non-audit issues) | Next step: Stage 5 blind sampled audit (`audit_sample.py`) and publish.

## Page map
- **Volume I (`p0000`–`p0343`, 344 leaves)**:
  - `p0000` dark backing/delete; `p0001` plain marbled half-leather cover (no lettering); `p0002` Cork & Orrery bookplate + UIUC library label; `p0003`–`p0005` blank flyleaves; `p0006` IA digitization target sheet (omitted).
  - `p0007` title page (`VOL. I.`); `p0008` blank verso (pencil call number omitted).
  - `p0009`–`p0010` Preface (pp. `[v]`–`vi`).
  - `p0011`–`p0016` Introduction (pp. `[vii]`–`xii`).
  - `p0017`–`p0332` = printed pp. `[1]`–`316` (offset `+16`), continuous prose narrative with blank-line/rule breaks and embedded letters/tales (`Letter from Harriet.`, `Agatha to Henry.`, `Henry to Agatha.`, `Gianetta’s Tale.`, etc.), ending `END OF THE FIRST VOLUME.` and printer colophon (`London: Printed by A. & R. Spottiswoode, New-Street-Square.`) on `p0332`.
  - `p0333`–`p0338` blank rear flyleaves & back cover; `p0339`–`p0343` hidden scanner backing and color/white cards (omitted).
- **Volume II (`p1000`–`p1381`, 382 leaves)**:
  - `p1000` dark backing/delete; `p1001` plain marbled half-leather cover (no lettering); `p1002` Cork & Orrery bookplate + UIUC library label; `p1003`–`p1005` blank flyleaves; `p1006` IA digitization target sheet (omitted).
  - `p1007` title page (`VOL. II.`); `p1008` blank verso (pencil call number omitted).
  - `p1009`–`p1372` = printed pp. `[1]`–`364` (offset `+1008`, with printer-transposed folios `31` and `30` on `p1038`–`p1039`), continuous prose narrative with embedded letters and tales (`The Muser’s Tale.`, `The Tale of the Young Mogul.`, `The Monk’s Tale.`, etc.), ending with 2-line Spenser quotation, `THE END.`, and Spottiswoode colophon on `p1372`.
  - `p1373`–`p1376` blank rear flyleaves & back cover; `p1377`–`p1381` hidden scanner backing and color/white cards (omitted).
- **Illustrations / ornaments**: none (only simple typographic rules). `images/cover.jpg` cropped from full-colour Vol. I title page (`p0007`, `603×1000`, visually verified).
- **Scan check (2026-11-26)**: all 19 contact sheets (`sheet-01.jpg`–`sheet-19.jpg`) and 55+ full-size leaves visually inspected by Gemini Pro subagent (`6fd861408c3d04d572f2b10e4a05022e`); 100% complete and crisp throughout, zero pagination gaps or missing/obscured leaves; handwritten pencil author attribution (`Joseph Moyle Sherer`) on `p0007`/`p1007`, call numbers on `p0008`/`p1008`, and accession numbers/stamps on `p0009`/`p0017`/`p1009` omitted.

## Decisions
- Combined two-volume anonymous novel into a single digital edition opening with Volume I’s title page (`p0007`), Preface (`p0009`–`p0010`), and Introduction (`p0011`–`p0016`), keeping Volume II’s title page (`p1007`–`p1008`) in JSON only. Because the printed novel has no numbered chapters, Volume I (`p0017`–`p0332`) and Volume II (`p1009`–`p1372`) are split via `toc_entries` at natural scene breaks (editorial headings) and the four printed embedded tales (`Gianetta’s Tale`, `The Muser’s Tale`, `The Tale of the Young Mogul`, `The Monk’s Tale`, `"editor": false`).
- Added `"keep_hyphens": ["p0287", "p0304", "p1114"]` (`fellow-creatures`, `aid-de-camp`, `wide-stretched`).
- Restored `[[cont]]` on `p0018` and `p0049` (verified flush-left on scans after Flash removal), removed `[[cont]]` on `p1361` (new Spenserian stanza opening with `“` after complete 9-line stanza on `p1360`), restored missed bottom line on `p0277` (`day street; priests in groups were taking snuff`, verified the single dropped line across all 132,840 words via full word-stream check), italicized `&c.` on `p1007`, fixed misread `countenence` → `countenance` on `p1014` (magnified crop), and stripped repeated line-start quotation marks on lines 2–6 of the song on `p0131` per modern convention.
- Marked 34 scan-verified unmistakable printer’s errors with `[[corr printed|corrected]]`: `p0047` `dedegraded`→`degraded`, `p0063` `aa`→`a`, `p0082` `cocl`→`cool`, `p0104` `abruptly.”`→`abruptly.`, `p0204` `digustedly`→`disgustedly`, `p0217` `1`→`I`, `p0230` `at at`→`at`, `p0235` `ourning`→`burning`, `p0292` `No,`→`“No,`, `p0295` `paid.`→`paid.”`, `p0297` `pride.”`→`pride.`, `p0298` `contemptuons`→`contemptuous`, `p1022` `death.”`→`death.`, `p1062` `my my`→`my`, `p1079` `whan`→`when`, `p1117` `warnith`→`warmth`, `p1142` `spokeu`→`spoken`, `p1154` `tearsfell`→`tears fell`, `p1165` `reprcach`→`reproach`, `p1167` `gentlemen`→`gentleman`, `p1175` `crossed`→`crossed?`, `p1188` `oppresed`→`oppressed`, `p1216` `the the`→`the`, `p1224` `firstr eceiving`→`first receiving`, `p1226` `1`→`I`, `p1229` `Fool,’ theyseemed`→`Fool,” they seemed`, `p1268` `hazipooor`→`hazipoor`, `p1290` `factories.`→`factories.”`, `p1299` `me.”`→`me.`, `p1302` `I,`→`“I,`, `p1313` `air`→`hair`, `p1324` `the the`→`the`, `p1328` `disgusted`→`Disgusted`, and `p1334` `c!imbed`→`climbed`.

## Runs
| Stage | Date | Model | Pages | Notes |
|---|---|---|---|---|
| Draft | 2026-11-26 | `gemini-pro` (+ `ocr_fallback.py`) | 692 (`p0007`–`p0332`, `p1007`–`p1372`) | 657 direct Pro draft (all 326 Vol. I + 331 Vol. II) + 35 Tesseract + Pro JSONL fallback (`p1022`–`p1023`, `p1050`–`p1055`, `p1069`–`p1070`, `p1108`–`p1109`, `p1120`, `p1141`–`p1142`, `p1263`–`p1264`, `p1311`–`p1317`, `p1362`–`p1372`); normalized cleanly; 0 `〓` |
| Verify | 2026-11-26 | `gemini-flash` | 692 | 14 batches (+ 5-page completion for `p0237`–`p0241`); 38 corrections applied (`0` skipped, `0` outliers, `2` `[[cont]]` removals on `p0018`/`p0049` overturned on scan) -> 16 spots on 16 pages |
| Judge | 2026-11-26 | `gemini-pro` (blind A/B) | 16 (16 spots) | `draft`: 10, `verified`: 6; 61 magnified scan crops inspected across judge report, preflight observe lists, and draft flags (caught `p1014` `countenance` misread, confirmed `p1343` `American`, marked 34 `[[corr]]` entries; restored dropped line on `p0277`) |

## Versions
| Version | Date | Preflight stamp | Audit | Notes |
|---|---|---|---|---|
