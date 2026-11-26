# Lessons learned

Keep this file short and actionable. Delete any lesson once a tool or preflight check enforces it automatically.

## Always

- **Never modernize unusual or archaic spellings.** Gemini models sometimes silently normalize rare or archaic spellings (`neophite` → `neophyte`, `shew` → `show`, `connexion` → `connection`, `chuse` → `choose`). Both `prompts/_rules.md` and `prompts/_verify-task.md` forbid this; inspect every `judge/report.txt` item where one reading is more modern or familiar than the other.
- **Keep roman parentheses and brackets outside `<i>…</i>`.** Write `(<i>aside</i>)`, not `<i>(aside)</i>`, unless the parentheses themselves are printed in italic (`preflight.py` `italic-brackets` lists candidates).
- **Check every crop visually with `view_file`.** Ensure `images/cover.jpg` and every illustration/ornament crop includes neither neighbouring body text nor clipped borders/lettering. `cover.jpg` must show a clearly readable title (front cover if readable, otherwise Volume I’s title page).
- **Inspect `〓` and preflight’s word lists on scan crops.** Every `misprints`, `rare-forms`, `missing-stop`, and `accents` item is checked on the scan: printed misprints get `[[corr printed|corrected]]`; dialect and intentional spellings stay unmarked.
- **Title page first.** Volume I’s title page (`kind: "titlepage"`) is transcribed line-by-line with `[[center]]` and capitals as printed, and opens the reading editions.

## Vetting candidates (`select-novel`)

- **Google-digitized (`…goog`) items on IA often lack `_jp2.zip` archives.** All seven Google-scanned single-volume candidates checked in `data/blog_2021.json` had no `_jp2.zip`/`_jp2.tar` file (only PDF/DjVu), disqualifying them unless a library scan (`uiuc`, `uoft`, `cdl`/`rich`, `bodleian`, `loc`) exists. Always run `ia.py meta <id>` first.
- **Check title pages for misdated, composite, or misattributed records.** In `blog_2021.json`, *“Corinna”* by “Rita” was catalogued as `1800` on IA when its actual title-page date is `1885` (and Volume III appends a separate novella, *Edelweiss*); *Vargas: A Tale of Spain* (1822) is by Alexander Robert Charles Dallas, not Joseph Blanco White; and *The Metropolis* (1819) is anonymous rather than by E. S. Barrett (Garside).
- **Verify end-of-book completeness before queuing.** Pierce Egan’s *The Pilgrims of the Thames* (`pilgrimsofthames00eganrich`) breaks off mid-sentence at p. 360 of 375. Always check the final pages of `_djvu.txt` / `scandata.xml` against the physical collation (`375 p.`).

## Multi-volume novels

- Verify the IA volume numbers on the title pages themselves (catalogue links occasionally swap volume order, e.g. `transgressionoft02vall` is Volume I and `transgressionoft01vall` is Volume II).
- Prepare Volume I at offset `0` (`p0000`…), Volume II at `--offset 1000` (`p1000`…), Volume III at `--offset 2000` (`p2000`…), etc.
- Mark Volume II+ title pages, half-titles, and printed contents with `"reading": false` in `divisions` so they remain in the JSON only, and group each volume’s chapters under `"Volume I"`, `"Volume II"`, `"Volume III"` (`part` divisions, via `divisions` if printed on a separate half-title leaf or via `parts` in `book.json` if not).
