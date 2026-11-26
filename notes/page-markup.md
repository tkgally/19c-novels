# Page markup

One UTF-8 text file per IA leaf, `pNNNN.txt` (`p0000`… for Volume I, `p1000`… for Volume II, `p2000`… for Volume III when prepared with `prep_pages.py --offset`). Read by `tools/compile_book.py`.

| Markup | Meaning |
|---|---|
| `[[page N]]` (line 1) | printed page number as printed; `?` if none |
| `[[blank]]` | blank page |
| a line of text | one paragraph (separated by a blank line; never wrap a paragraph across multiple lines) |
| `[[cont]]` at start of first paragraph | continues the previous page’s last paragraph |
| `# ` / `## ` / `### ` | main division (`# Chapter I.`, `# Preface.`) / section / subsection; typed in upper and lower case even if printed in capitals |
| `[[subtitle]] text` | chapter title or summary printed under the chapter number |
| `<i> <b> <sc> <sup> <sub>` | italic, bold, small capitals (typed in lower case), superscript, subscript; keep roman brackets outside `<i>…</i>` |
| `[[right]] text`, `[[center]] text` | short line set flush right / centred |
| `[[break]]` | scene break marked by blank space, asterisks, or an ornamental rule |
| `[[image: description]]` | illustration or ornament (`images/pNNNN-k.jpg`) |
| `[[caption]] text` | printed caption of the preceding `[[image: …]]` |
| `[[fnref *]]` / `[[fn *]] text` | footnote reference in text / footnote at end of page file (`[[fnref * again]]` for a second mark to the same note; `[[fn cont]]` for continued note) |
| `<blockquote>` … `</blockquote>` | set-off prose (letter, notice, prose epigraph), one paragraph per line |
| `<verse>` … `</verse>` | verse, one printed line per line, blank line between stanzas |
| `| a | b |` | pipe table |
| `<pref>34</pref>`, `<pref to="34">text</pref>` | internal page reference to this book’s page 34 |
| `[[side: text]]` | marginal side-note (kept in JSON, omitted from reading editions) |
| `[[stream]] text` | secondary text stream along page feet |
| `[[corr printed|corrected]]` | unmistakable printer’s error corrected (`notes/style.md`) |
| `[[supplied …]]` / `[[gap]]` | short scan loss supplied from context / unrecoverable `[…]` |
| `〓` | illegible character (must be resolved before publication) |
