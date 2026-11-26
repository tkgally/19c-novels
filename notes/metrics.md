# Metrics

## Published versions

| Date | Novel (`slug` vN) | Year / Vols | Leaves | Flash changes | Judge spots (Pro / Flash / scan) | Corrections (`[[corr]]`) | Audit (pages, recall, real errors) | Notes |
|---|---|---|---|---|---|---|---|---|
| 2026-11-26 | `browns-and-the-smiths-davies` v1 | 1863 / 2 vols | 662 (635 transcribed) | 39 (`0` unapplied) | 31 on 14 pp (`1` / `28` / `2` `neither`; scan crop overturned `1` false misprint on `p0054`) | 25 | 6 pp, `28/30` (`93%`), `0` real errors | 0 recitation blocks; 0 `〓`; combined 2-vol edition |
| 2026-11-26 | `browns-and-the-smiths-davies` v2 | 1863 / 2 vols | 662 (635 transcribed) | — | — | 25 | Carried from v1 | Compiler fix for page-break hyphens inside inline tags (`p0009`–`p0010` *ad nauseam*; GitHub #2) |
| 2026-11-26 | `by-the-cornish-sea-isabell` v1 | 1885 / 2 vols | 676 (648 transcribed) | 30 (`3` skipped) | 15 on 14 pp (`5` / `10` / `0`; magnified crop caught `p1018` printed period `[[corr again.”|again,”]]`) | 20 | 7 pp (incl. 2 fallback), `34/35` (`97%`), `0` real errors | 90 fallback pages (`ocr_fallback.py`); 0 `〓`; combined 2-vol edition |
| 2026-11-26 | `story-of-a-life-sherer` v1 | 1825 / 2 vols | 726 (692 transcribed) | 38 (`0` skipped) | 16 on 16 pp (`10` / `6` / `0`; 61 magnified crops checked, caught `p1014` `countenance` misread) | 34 | 7 pp (incl. 2 fallback), `34/35` (`97%`), `0` real errors | 35 fallback pages (`ocr_fallback.py`); 0 `〓`; unchaptered 2-vol novel split into 19 reading sections via `toc_entries` |

## Preflight checks (false alarms and promotions)

| Date | Check | Novel | Item | Action |
|---|---|---|---|---|
| 2026-11-26 | `rare-forms` | `browns-and-the-smiths-davies` | `erself` (`p0043`), `aud` (`p1193`) | Caught real printed misprints `keenlyh erself` and `aud`; `beard`, `curse`, `resent` verified genuine |
| 2026-11-26 | `quote-balance` | `browns-and-the-smiths-davies` | `p0095`, `p0202`, `p0257` | All 3 flagged real compositor quote errors on the scan |
| 2026-11-26 | `missing-stop` | `browns-and-the-smiths-davies` | `wicked There` (`p0203`), `course He` (`p0259`) | `p0203` caught real dropped full stop; `p0259` genuine (`He` = God) |
| 2026-11-26 | `hyphen-joins` | `story-of-a-life-sherer` | `an every-|together` (`p0277`–`p0278`) | Caught missed bottom line on `p0277` (`day street; priests in groups were taking snuff`) missed by both Pro and Flash |
| 2026-11-26 | `quote-balance` | `story-of-a-life-sherer` | `p0104`, `p0292`, `p0295`/`p0297`, `p1022`, `p1299`, `p1302` | All 6 flagged real compositor missing/spurious quotation marks on the scan |
| 2026-11-26 | `verse-joins` | `story-of-a-life-sherer` | `p1360`–`p1361` (`[9] | [9]`) | Caught spurious `[[cont]]` between two separate 9-line Spenserian stanzas |
