# Metrics

## Published versions

| Date | Novel (`slug` vN) | Year / Vols | Leaves | Flash changes | Judge spots (Pro / Flash / scan) | Corrections (`[[corr]]`) | Audit (pages, recall, real errors) | Notes |
|---|---|---|---|---|---|---|---|---|
| 2026-11-26 | `browns-and-the-smiths-davies` v1 | 1863 / 2 vols | 662 (635 transcribed) | 39 (`0` unapplied) | 31 on 14 pp (`1` / `28` / `2` `neither`; scan crop overturned `1` false misprint on `p0054`) | 25 | 6 pp, `28/30` (`93%`), `0` real errors | 0 recitation blocks; 0 `〓`; combined 2-vol edition |
| 2026-11-26 | `browns-and-the-smiths-davies` v2 | 1863 / 2 vols | 662 (635 transcribed) | — | — | 25 | Carried from v1 | Compiler fix for page-break hyphens inside inline tags (`p0009`–`p0010` *ad nauseam*; GitHub #2) |
| 2026-11-26 | `by-the-cornish-sea-isabell` v1 | 1885 / 2 vols | 676 (648 transcribed) | 30 (`3` skipped) | 15 on 14 pp (`5` / `10` / `0`; magnified crop caught `p1018` printed period `[[corr again.”|again,”]]`) | 20 | 7 pp (incl. 2 fallback), `34/35` (`97%`), `0` real errors | 90 fallback pages (`ocr_fallback.py`); 0 `〓`; combined 2-vol edition |
| 2026-11-26 | `story-of-a-life-sherer` v1 | 1825 / 2 vols | 726 (692 transcribed) | 38 (`0` skipped) | 16 on 16 pp (`10` / `6` / `0`; 61 magnified crops checked, caught `p1014` `countenance` misread) | 34 | 7 pp (incl. 2 fallback), `34/35` (`97%`), `0` real errors | 35 fallback pages (`ocr_fallback.py`); 0 `〓`; unchaptered 2-vol novel split into 19 reading sections via `toc_entries` |
| 2026-11-26 | `transgression-of-terence-clancy-vallings` v1 | 1893 / 3 vols | 938 (875 transcribed + 6 blank versos) | 60 (`0` skipped) | 34 on 32 pp (`16` / `17` / `1` manual; 31 scan spots verified) | 21 | 6 pp (incl. 3 fallback), `28/29` (`97%`), `0` real errors | First three-decker; 435 fallback pages (`ocr_fallback.py`); Flash caught wrong-page draft on `p1223`; 0 `〓` |
| 2026-11-27 | `transgression-of-terence-clancy-vallings` v2 | 1893 / 3 vols | 938 (875 transcribed + 6 blank versos) | — | — | 21 | Carried from v1 | Restored missing `[[cont]]` on `p1152` (Vol. II p. 144) caught by 5-novel review sweep (`notes/errata.md`) |
| 2026-11-27 | `middle-aged-lover-fitzgerald` v1 | 1873 / 2 vols | 692 (660 transcribed + 2 blank versos) | 36 (`1` already-applied skipped) | 20 on 19 pp (`6` / `14` / `0`; 17 magnified crops checked; scan overturned judge on `p1273` `<sc>have had no money</sc>`) | 3 | 6 pp (incl. 1 fallback `p0139`), `28/30` (`93%`), `0` real errors | 74 fallback pages (`ocr_fallback.py`, 0 skipped patches); full `_djvu.txt` word-stream diff showed 0 dropped lines; 0 `〓` |
| 2026-11-27 | `reginald-hastings-warburton` v1 | 1850 / 3 vols | 1,032 (968 transcribed + 2 blank versos) | 46 (`0` skipped) | 37 on 31 pp (`11` / `25` / `1` `neither`; 64 magnified crops checked; scans overturned 3 judge spots: `p1321` `countenance`, `p2178` & `p2179` `portress`) | 42 | 6 pp, `30/30` (`100%`), `0` real errors | 0 recitation blocks; full `_djvu.txt` word-stream diff showed 0 dropped lines; extended `quote-balance` caught 2 missed `[[cont]]` (`p0200`, `p0202`) and 10 compositor quote errors; 0 `〓` |

## Preflight checks (false alarms and promotions)

| Date | Check | Novel | Item | Action |
|---|---|---|---|---|
| 2026-11-26 | `rare-forms` | `browns-and-the-smiths-davies` | `erself` (`p0043`), `aud` (`p1193`) | Caught real printed misprints `keenlyh erself` and `aud`; `beard`, `curse`, `resent` verified genuine |
| 2026-11-26 | `quote-balance` | `browns-and-the-smiths-davies` | `p0095`, `p0202`, `p0257` | All 3 flagged real compositor quote errors on the scan |
| 2026-11-26 | `missing-stop` | `browns-and-the-smiths-davies` | `wicked There` (`p0203`), `course He` (`p0259`) | `p0203` caught real dropped full stop; `p0259` genuine (`He` = God) |
| 2026-11-26 | `hyphen-joins` | `story-of-a-life-sherer` | `an every-|together` (`p0277`–`p0278`) | Caught missed bottom line on `p0277` (`day street; priests in groups were taking snuff`) missed by both Pro and Flash |
| 2026-11-26 | `quote-balance` | `story-of-a-life-sherer` | `p0104`, `p0292`, `p0295`/`p0297`, `p1022`, `p1299`, `p1302` | All 6 flagged real compositor missing/spurious quotation marks on the scan |
| 2026-11-26 | `verse-joins` | `story-of-a-life-sherer` | `p1360`–`p1361` (`[9] | [9]`) | Caught spurious `[[cont]]` between two separate 9-line Spenserian stanzas |
| 2026-11-27 | `contents` | `middle-aged-lover-fitzgerald` | `p1008` (`A Confession 238`) | Genuine Victorian printer mismatch between Vol. II Contents (`A CONFESSION`) and Ch. XXI heading (`A CONVERSION.` on `p1246`) |
| 2026-11-27 | `folios` | `middle-aged-lover-fitzgerald` | `p1296` (`88` after `287`) | Verified genuine dropped leading `2` on Vol. II p. 288 |
| 2026-11-27 | `misprints` | `middle-aged-lover-fitzgerald` | `p0110`–`p0111` (`—th`) | Verified genuine redacted regiment number (`—th Du Barry’s own Hussars`) |
| 2026-11-27 | `quote-balance` | `reginald-hastings-warburton` | `p0199`–`p0200`, `p0201`–`p0202`, plus 10 quote errors | Extended `quote-balance` caught 2 missed flush-left `[[cont]]` continuations (`p0200`, `p0202`) missed by both Pro and Flash, plus 10 genuine compositor quotation-mark errors |
| 2026-11-27 | `accents` | `reginald-hastings-warburton` | `mélée` (`p0334`) vs `mêlée` | Magnified crop verified `mêlée` on `p0334`, fixing the accent mismatch; Italian `nè` (`p0253`) and French `péril` (`p0140`) verified genuine |
| 2026-11-27 | `lowercase-after-stop` | `reginald-hastings-warburton` | `lb. shot` (`p2148`) | Genuine weight abbreviation (`3 lb. shot`) |
