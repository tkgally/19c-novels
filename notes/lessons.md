# Lessons learned

Keep this file short and actionable. Delete any lesson once a tool or preflight check enforces it automatically.

## Always

- **Never modernize unusual or archaic spellings.** Gemini models sometimes silently normalize rare or archaic spellings (`neophite` → `neophyte`, `shew` → `show`, `connexion` → `connection`, `chuse` → `choose`). Both `prompts/_rules.md` and `prompts/_verify-task.md` forbid this; inspect every `judge/report.txt` item where one reading is more modern or familiar than the other.
- **Keep roman parentheses and brackets outside `<i>…</i>`.** Write `(<i>aside</i>)`, not `<i>(aside)</i>`, unless the parentheses themselves are printed in italic (`preflight.py` `italic-brackets` lists candidates).
- **Check every crop visually with `view_file`.** Ensure `images/cover.jpg` and every illustration/ornament crop includes neither neighbouring body text nor clipped borders/lettering. `cover.jpg` must show a clearly readable title (front cover if readable, otherwise Volume I’s title page).
- **Inspect `〓` and preflight’s four word lists on scan crops.** Every `misprints`, `rare-forms`, `missing-stop`, and `accents` item is checked on the scan: printed misprints get `[[corr printed|corrected]]`; dialect and intentional spellings stay unmarked.
- **Title page first.** Volume I’s title page (`kind: "titlepage"`) is transcribed line-by-line with `[[center]]` and capitals as printed, and opens the reading editions.

## Multi-volume novels

- Verify the IA volume numbers on the title pages themselves (blog or catalogue links occasionally list Vol. II before Vol. I, e.g. `transgressionoft02vall` / `01vall`).
- Prepare Volume I at offset `0` (`p0000`…), Volume II at `--offset 1000` (`p1000`…), Volume III at `--offset 2000` (`p2000`…), etc.
- Mark Volume II+ title pages, half-titles, and printed contents with `"reading": false` in `divisions` so they remain in the JSON only, and group each volume’s chapters under `"Volume I"`, `"Volume II"`, `"Volume III"` (`part` divisions, via `divisions` if printed on a separate half-title leaf or via `parts` in `book.json` if not).
