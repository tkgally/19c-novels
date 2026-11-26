# Draft Transcription Batch 6 (54 pages)

1. First read the transcription rules and markup specification in `/home/antigravity/tkgally/19c-novels/prompts/transcribe.md`.
2. For each page listed below, inspect the scan image directly with `view_file` (do NOT use IA's `_djvu.txt` or OCR files; transcribe strictly from the visual scan) and write the exact page-markup transcription to its output `.txt` file using `write_to_file`.
3. Watch carefully for two known pitfalls: NEVER modernize or normalize unusual/old spellings (e.g. keep `neophite`, `shew`, `connexion`, `to-day` exactly as printed), and keep roman parentheses/brackets OUTSIDE `<i>…</i>` tags.
4. If the platform blocks outputting any page due to a recitation/content filter, do NOT retry or rephrase that page; instead append `{"page": "<stem>", "error": "recitation"}` to `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/log.jsonl` and continue to the next page.

## Pages in this batch

- `p0275`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0275.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0275.txt`
- `p0276`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0276.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0276.txt`
- `p0277`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0277.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0277.txt`
- `p0278`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0278.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0278.txt`
- `p0279`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0279.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0279.txt`
- `p0280`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0280.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0280.txt`
- `p0281`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0281.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0281.txt`
- `p0282`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0282.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0282.txt`
- `p0283`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0283.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0283.txt`
- `p0284`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0284.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0284.txt`
- `p0285`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0285.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0285.txt`
- `p0286`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0286.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0286.txt`
- `p0287`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0287.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0287.txt`
- `p0288`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0288.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0288.txt`
- `p0289`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0289.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0289.txt`
- `p0290`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0290.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0290.txt`
- `p0291`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0291.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0291.txt`
- `p0292`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0292.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0292.txt`
- `p0293`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0293.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0293.txt`
- `p0294`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0294.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0294.txt`
- `p0295`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0295.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0295.txt`
- `p0296`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0296.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0296.txt`
- `p0297`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0297.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0297.txt`
- `p0298`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0298.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0298.txt`
- `p0299`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0299.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0299.txt`
- `p0300`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0300.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0300.txt`
- `p0301`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0301.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0301.txt`
- `p0302`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0302.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0302.txt`
- `p0303`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0303.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0303.txt`
- `p0304`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0304.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0304.txt`
- `p0305`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0305.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0305.txt`
- `p0306`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0306.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0306.txt`
- `p0307`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0307.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0307.txt`
- `p0308`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0308.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0308.txt`
- `p1005`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1005.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1005.txt`
- `p1006`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1006.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1006.txt`
- `p1007`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1007.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1007.txt`
- `p1008`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1008.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1008.txt`
- `p1009`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1009.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1009.txt`
- `p1010`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1010.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1010.txt`
- `p1011`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1011.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1011.txt`
- `p1012`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1012.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1012.txt`
- `p1013`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1013.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1013.txt`
- `p1014`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1014.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1014.txt`
- `p1015`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1015.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1015.txt`
- `p1016`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1016.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1016.txt`
- `p1017`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1017.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1017.txt`
- `p1018`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1018.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1018.txt`
- `p1019`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1019.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1019.txt`
- `p1020`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1020.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1020.txt`
- `p1021`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1021.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1021.txt`
- `p1022`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1022.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1022.txt`
- `p1023`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1023.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1023.txt`
- `p1024`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1024.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1024.txt`
