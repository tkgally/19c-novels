# Draft Transcription Batch 5 (54 pages)

1. First read the transcription rules and markup specification in `/home/antigravity/tkgally/19c-novels/prompts/transcribe.md`.
2. For each page listed below, inspect the scan image directly with `view_file` (do NOT use IA's `_djvu.txt` or OCR files; transcribe strictly from the visual scan) and write the exact page-markup transcription to its output `.txt` file using `write_to_file`.
3. Watch carefully for two known pitfalls: NEVER modernize or normalize unusual/old spellings (e.g. keep `neophite`, `shew`, `connexion`, `to-day` exactly as printed), and keep roman parentheses/brackets OUTSIDE `<i>…</i>` tags.
4. If the platform blocks outputting any page due to a recitation/content filter, do NOT retry or rephrase that page; instead append `{"page": "<stem>", "error": "recitation"}` to `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/log.jsonl` and continue to the next page.

## Pages in this batch

- `p0221`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0221.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0221.txt`
- `p0222`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0222.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0222.txt`
- `p0223`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0223.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0223.txt`
- `p0224`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0224.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0224.txt`
- `p0225`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0225.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0225.txt`
- `p0226`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0226.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0226.txt`
- `p0227`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0227.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0227.txt`
- `p0228`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0228.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0228.txt`
- `p0229`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0229.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0229.txt`
- `p0230`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0230.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0230.txt`
- `p0231`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0231.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0231.txt`
- `p0232`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0232.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0232.txt`
- `p0233`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0233.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0233.txt`
- `p0234`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0234.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0234.txt`
- `p0235`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0235.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0235.txt`
- `p0236`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0236.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0236.txt`
- `p0237`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0237.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0237.txt`
- `p0238`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0238.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0238.txt`
- `p0239`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0239.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0239.txt`
- `p0240`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0240.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0240.txt`
- `p0241`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0241.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0241.txt`
- `p0242`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0242.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0242.txt`
- `p0243`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0243.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0243.txt`
- `p0244`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0244.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0244.txt`
- `p0245`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0245.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0245.txt`
- `p0246`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0246.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0246.txt`
- `p0247`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0247.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0247.txt`
- `p0248`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0248.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0248.txt`
- `p0249`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0249.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0249.txt`
- `p0250`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0250.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0250.txt`
- `p0251`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0251.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0251.txt`
- `p0252`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0252.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0252.txt`
- `p0253`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0253.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0253.txt`
- `p0254`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0254.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0254.txt`
- `p0255`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0255.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0255.txt`
- `p0256`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0256.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0256.txt`
- `p0257`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0257.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0257.txt`
- `p0258`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0258.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0258.txt`
- `p0259`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0259.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0259.txt`
- `p0260`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0260.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0260.txt`
- `p0261`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0261.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0261.txt`
- `p0262`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0262.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0262.txt`
- `p0263`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0263.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0263.txt`
- `p0264`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0264.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0264.txt`
- `p0265`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0265.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0265.txt`
- `p0266`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0266.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0266.txt`
- `p0267`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0267.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0267.txt`
- `p0268`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0268.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0268.txt`
- `p0269`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0269.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0269.txt`
- `p0270`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0270.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0270.txt`
- `p0271`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0271.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0271.txt`
- `p0272`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0272.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0272.txt`
- `p0273`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0273.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0273.txt`
- `p0274`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p0274.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p0274.txt`
