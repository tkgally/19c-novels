## Output format ("page markup")

Output ONLY the transcription of this one page, in the plain-text markup below. No commentary, no code fences.

- Line 1 is always `[[page N]]`, where N is the page number printed on the page (arabic or roman, as printed; `[[page ?]]` if none is printed).
- Then the page's content, paragraphs separated by one blank line. Each paragraph is ONE line: join its printed lines.
- If the page's first paragraph continues a paragraph begun on the previous page (it does not start with a paragraph indent), start it with `[[cont]]`.
- Headings: `# ` for the title of a chapter, volume/part, or other main division (`# CHAPTER IV.`, `# VOLUME II.`, `# PREFACE.`); `## ` for a section heading inside a chapter; `### ` for a smaller one. A heading printed in capitals is typed in upper and lower case, title style (`# Chapter IV.`, `## At the Parsonage`), with roman numerals in capitals; its words, spelling, and punctuation stay as printed.
- A chapter title or summary of contents printed under the chapter number (`In Which Our Hero Sets Forth`) goes on the next line as `[[subtitle]] text`, also in upper and lower case if printed in capitals.
- An epigraph under a chapter heading: prose epigraphs in `<blockquote>` … `</blockquote>`, verse epigraphs in `<verse>` … `</verse>`, with an attribution line starting `[[right]]` (either inside `<blockquote>` for prose or right after `</verse>`).
- A page of the printed table of CONTENTS: only its title is a heading (`# Contents.`); type each entry as plain lines in printed order, never as a table or with `#` headings: the chapter number as `[[center]] Chapter IV.`, the title with its page number marked (`[[center]] The Rectory <pref>41</pref>`), a summary printed under it as its own paragraph. Leave out the column head “PAGE” and dot leaders. Type every contents page of the book the same way.
- A TITLE PAGE: no `#` heading. Each printed line, or group of lines that form one phrase, is a paragraph of its own starting with `[[center]]` (`[[right]]` if set flush right), in printed order, with capitals as printed: title, subtitle, author, epigraph, volume statement, edition, publisher, place, date. A device or vignette is `[[image: …]]`.
- A short line set flush right (a signature, a place and date closing a letter) starts with `[[right]]`; a short centred line that is not a heading (an inscription, a half-title, `THE END`, `END OF VOL. I.`) starts with `[[center]]`.
- A space, rule, or asterisks printed between paragraphs to mark a scene break in the narrative: a line with only `[[break]]`.
- Illustrations, plates, vignettes, decorative head-pieces and tail-pieces: `[[image: a few words describing it]]` on its own line where it occurs; do not transcribe lettering that is inside the picture. A printed caption goes on the next line as `[[caption]] caption text` (upper and lower case if printed in capitals).
- Footnotes printed at the foot of the page: one per line at the end, `[[fn *]] note text`, with the mark as printed (`*`, `†`, `1`). Mark the reference in the text as `[[fnref *]]`. A note continued from the previous page: `[[fn cont]] text`.
- Prose set off from the text (a quoted letter, notice, or extract in smaller type): a line `<blockquote>`, its paragraphs one per line, a line `</blockquote>`.
- Verse: a line `<verse>`, each printed line of verse on its own line, an empty line between stanzas, a line `</verse>`.
- If a quotation or verse continues from the previous page, put `[[cont]]` at the start of its first line.
- Marginal notes (side-notes): `[[side: words as printed]]` inside the paragraph, immediately before the first word of the printed line the note stands beside.
- Tables: simple pipe tables, one row per line (`| a | b |`).
- A reference to another page OF THIS SAME BOOK (`see p. 34`): wrap just the number, `p. <pref>34</pref>`. Not for pages of other books.
- A blank page is `[[page ?]]` followed by `[[blank]]`. A page with only a picture has the `[[page ?]]` line and the `[[image: …]]` line.
- If a character is truly illegible write `〓`.
