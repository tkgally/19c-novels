# Style: the text, multi-volume novels, the editions, the site

## The text

- **Faithful.** The author’s words, spelling, capitals, dialect, and punctuation marks exactly as printed, including old and inconsistent spellings (`shew`, `chuse`, `connexion`, `to-day`, `honour`, `neophite`).
- **Spacing is modern.** No space before `; : ! ?`, none inside quotation marks, contractions closed up (`do n't` → `don't`), dashes closed up (`tools/normalize.py`).
- **Printer’s errors.** Only unmistakable printer’s errors are corrected: transposed or doubled letters, a repeated word at a line end, a dropped letter in a common word, turned letters (`tbe`, `aud`, `iu`, `conld`), a missing full stop at the end of a paragraph, or a plainly missing/doubled quotation mark. Each is marked `[[corr printed|corrected]]`. Never “correct” dialect, archaic spelling, proper names, grammar, or authorial inconsistency. Printed errata slips are applied with `[[corr]]` and noted in `notes_on_text`.
- **Line-end hyphens** are resolved (keeping hyphens in real compounds and period forms such as `to-day`, `to-morrow`, `to-night`, `drawing-room`).
- **Quotation marks** curly, single or double as printed. Running opening quotation marks repeated down the left margin of a quotation are removed (`tools/running_quotes.py`), and multi-paragraph quotations use modern convention (an opening mark at the start of each paragraph, a closing mark only at the end of the whole quotation; note in `notes_on_text` when applied).
- **Text lost in the scan** (at most ~1 word at a tight gutter, fold, or blot, when no other scan settles it): inferable from context → `[[supplied …]]` (marked in JSON, plain in reading editions); not inferable → `[[gap]]` (`[…]` in both).
- **Typography:** long s (`ſ`) → `s`; ligatures `fi`, `fl` as separate letters; `æ`, `œ` kept. Italics (`<i>…</i>`) and small capitals (`<sc>…</sc>`, typed in lower case with full capitals only where visibly taller) as printed. Keep roman parentheses and square brackets outside `<i>…</i>`.
- **Headings and titles in upper and lower case:** headings, chapter titles/subtitles, and captions printed in ALL CAPITALS are typed in ordinary title case (`# Chapter IV.`, `# Volume II.`, `[[subtitle]] At the Rectory`), keeping roman numerals in capitals and keeping the original words, spelling, and punctuation.

## Multi-volume novels (“three-deckers” and 2–5 volume sets)

- Published digitally as **one combined book** (`Tom, 2026-11-26`).
- **Title pages:** Volume I’s title page (`kind: "titlepage"`) opens the HTML, EPUB, and ODT reading editions. The title pages, half-titles, and front/back advertisements of Volumes II, III, etc. are transcribed in full and marked `{"at": "p10NN", "kind": "front", "reading": false}` (or `"advertisements"` / `"back"`) so they are preserved in the JSON and omitted from the reading editions (stated in `omitted_from_reading`).
- **Volumes as Parts:** Volumes I, II, III, etc. appear as `part` divisions (`"Volume I"`, `"Volume II"`, `"Volume III"`) in the reading editions — either from a printed volume half-title page (`{"at": "p00NN", "kind": "part", "title": "Volume I"}`) or via `book.json` `"parts": [{"before": "p00NN", "title": "Volume I"}, …]` when the scan has no separate part leaf — keeping each volume’s own chapter numbering (`Chapter I`, `Chapter II`, …) nested under its Volume in the table of contents.

## What goes where

| Part | JSON | HTML / EPUB / ODT |
|---|---|---|
| Cover, half-title, anything before Vol. I’s title page | yes (`front`) | no |
| Volume I title page and its verso (`titlepage`) | yes | yes (first page of the editions; frontispiece after its first leaf) |
| Later volumes’ title pages and half-titles | yes (`front`) | no |
| Volume I, II, III… headings (`part`) | yes | yes (groups each volume’s chapters) |
| Dedication, preface, introduction, chapters, epilogue, author’s notes, glossary | yes | yes |
| Printed contents, list of illustrations | yes | no (replaced by generated contents) |
| Errata slip | yes | no (applied via `[[corr]]`) |
| Publisher’s advertisements | yes (`advertisements`) | no |

## Editions and site text

- Long italic passages (≥ 30 words prose or ≥ 4 lines verse, ≥ 90% italic) are rendered in roman in HTML, EPUB, and ODT while remaining italic in the JSON (`render_html.roman_long_italics`).
- Decorative head-pieces and tail-pieces are cropped and listed in `book.json` `ornaments` so they appear small in the editions.
- **Site prose (`summary`, `setting`, `period`, `notes_on_text`, `omitted_from_reading`):** 60–150 plain, factual words for `summary` — who the author was (briefly), where and when the story is set, its central situation, and any factual textual notes (dialect, original volume count, missing plates). No adjectives of praise (“fascinating”, “vivid”, “masterpiece”, “delightful”), no marketing tone, serial commas (“A, B, and C”), and curly apostrophes and quotation marks everywhere outside `code`.
