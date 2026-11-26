# The Story of a Life — Joseph Moyle Sherer (1825)

IA: `storyoflife01sher` (Vol. I, 344 leaves) and `storyoflife02sher` (Vol. II, 382 leaves), University of Illinois Urbana-Champaign, 500 ppi.
Eligibility: re-checked 2026-11-26 (`data/queue.json`, blog_2021 #37): original English novel published anonymously in 1825 (London: Longman, Hurst, Rees, Orme, Brown, and Green, 2 vols., first ed.), complete 500 ppi UIUC `_jp2.zip` scans for both volumes, not on Project Gutenberg (only *The Broken Font* is listed), Standard Ebooks, Wikisource, Faded Page, or Penn Online Books Page; no post-1914 trade/scholarly print edition (only print-on-demand scan replicas); author Joseph Moyle Sherer (1789–1869) died >70 years ago.

## Status
Stage reached: Stage 2 (Gemini Pro draft + 35 fallback pages normalized, 692/692 complete) | Next step: Stage 3 Gemini Flash second-pass verification and blind Pro judging.

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
  - `p1009`–`p1372` = printed pp. `[1]`–`364` (offset `+1008`), continuous prose narrative with embedded letters and tales (`The Tale of the Young Mogul.`, `The Monk’s Tale.`, etc.), ending with 2-line Spenser quotation, `THE END.`, and Spottiswoode colophon on `p1372`.
  - `p1373`–`p1376` blank rear flyleaves & back cover; `p1377`–`p1381` hidden scanner backing and color/white cards (omitted).
- **Illustrations / ornaments**: none (only simple typographic rules). `images/cover.jpg` cropped from full-colour Vol. I title page (`p0007`).
- **Scan check (2026-11-26)**: all 19 contact sheets (`sheet-01.jpg`–`sheet-19.jpg`) and 55+ full-size leaves visually inspected by Gemini Pro subagent (`6fd861408c3d04d572f2b10e4a05022e`); 100% complete and crisp throughout, zero pagination gaps or missing/obscured leaves; handwritten pencil author attribution (`Joseph Moyle Sherer`) on `p0007`/`p1007`, call numbers on `p0008`/`p1008`, and accession numbers/stamps on `p0009`/`p0017`/`p1009` to be omitted.

## Decisions
- Combined two-volume novel into a single digital edition opening with Volume I’s title page (`p0007`), Preface (`p0009`–`p0010`), and Introduction (`p0011`–`p0016`), keeping Volume II’s title page (`p1007`–`p1008`) in JSON only, and grouping Volume I (`p0017`–`p0332`) and Volume II (`p1009`–`p1372`) as Parts.
- Transcribed leaf ranges: `p0007`–`p0332` (326 leaves) and `p1007`–`p1372` (366 leaves), total 692 leaves.

## Runs
| Stage | Date | Model | Pages | Notes |
|---|---|---|---|---|
| Draft | 2026-11-26 | `gemini-pro` (+ `ocr_fallback.py`) | 692 (`p0007`–`p0332`, `p1007`–`p1372`) | 657 direct Pro draft (all 326 Vol. I + 331 Vol. II) + 35 Tesseract + Pro JSONL fallback (`p1022`–`p1023`, `p1050`–`p1055`, `p1069`–`p1070`, `p1108`–`p1109`, `p1120`, `p1141`–`p1142`, `p1263`–`p1264`, `p1311`–`p1317`, `p1362`–`p1372`); normalized cleanly; 0 `〓` |

## Versions
| Version | Date | Preflight stamp | Audit | Notes |
|---|---|---|---|---|
