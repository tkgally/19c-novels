# OCR Fallback Corrections Task

Read `/home/antigravity/tkgally/19c-novels/prompts/verify.md`. Each page below was first read by local Tesseract OCR (`*.raw.txt`), so running heads, page numbers, italics, small capitals, `[[cont]]`, headings, and misread letters need to be corrected against the scan image (`view_file`) using ONLY JSONL `{"find": ..., "replace": ...}` lines written to `*.corr`.

- `p2046`: image `/tmp/novels/country-houses-moore/pages/p2046.jpg` | raw `/home/antigravity/tkgally/19c-novels/wip/country-houses-moore/draft/_fallback/p2046.raw.txt` -> write `/home/antigravity/tkgally/19c-novels/wip/country-houses-moore/draft/_fallback/p2046.corr`
- `p2047`: image `/tmp/novels/country-houses-moore/pages/p2047.jpg` | raw `/home/antigravity/tkgally/19c-novels/wip/country-houses-moore/draft/_fallback/p2047.raw.txt` -> write `/home/antigravity/tkgally/19c-novels/wip/country-houses-moore/draft/_fallback/p2047.corr`
