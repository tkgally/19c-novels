# OCR Fallback Corrections Task

Read `/home/antigravity/tkgally/19c-novels/prompts/verify.md`. Each page below was first read by local Tesseract OCR (`*.raw.txt`), so running heads, page numbers, italics, small capitals, `[[cont]]`, headings, and misread letters need to be corrected against the scan image (`view_file`) using ONLY JSONL `{"find": ..., "replace": ...}` lines written to `*.corr`.

- `p0189`: image `/tmp/novels/middle-aged-lover-fitzgerald/pages/p0189.jpg` | raw `/home/antigravity/tkgally/19c-novels/wip/middle-aged-lover-fitzgerald/draft/_fallback/p0189.raw.txt` -> write `/home/antigravity/tkgally/19c-novels/wip/middle-aged-lover-fitzgerald/draft/_fallback/p0189.corr`
