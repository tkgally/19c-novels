# Draft Transcription Batch 8 (25 pages)

1. First read the transcription rules and markup specification in `/home/antigravity/tkgally/19c-novels/prompts/transcribe.md`.
2. For each page listed below, inspect the scan image directly with `view_file` (do NOT use IA's `_djvu.txt` or OCR files; transcribe strictly from the visual scan) and write the exact page-markup transcription to its output `.txt` file using `write_to_file`.
3. Watch carefully for two known pitfalls: NEVER modernize or normalize unusual/old spellings (e.g. keep `neophite`, `shew`, `connexion`, `to-day` exactly as printed), and keep roman parentheses/brackets OUTSIDE `<i>…</i>` tags.
4. If the platform blocks outputting any page due to a recitation/content filter, do NOT retry or rephrase that page; instead append `{"page": "<stem>", "error": "recitation"}` to `/home/antigravity/tkgally/19c-novels/wip/story-of-a-life-sherer/draft/log.jsonl` and continue to the next page.

## Pages in this batch

- `p0182`: image `/tmp/novels/story-of-a-life-sherer/pages/p0182.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/story-of-a-life-sherer/draft/p0182.txt`
- `p0183`: image `/tmp/novels/story-of-a-life-sherer/pages/p0183.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/story-of-a-life-sherer/draft/p0183.txt`
- `p0184`: image `/tmp/novels/story-of-a-life-sherer/pages/p0184.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/story-of-a-life-sherer/draft/p0184.txt`
- `p0185`: image `/tmp/novels/story-of-a-life-sherer/pages/p0185.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/story-of-a-life-sherer/draft/p0185.txt`
- `p0186`: image `/tmp/novels/story-of-a-life-sherer/pages/p0186.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/story-of-a-life-sherer/draft/p0186.txt`
- `p0187`: image `/tmp/novels/story-of-a-life-sherer/pages/p0187.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/story-of-a-life-sherer/draft/p0187.txt`
- `p0188`: image `/tmp/novels/story-of-a-life-sherer/pages/p0188.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/story-of-a-life-sherer/draft/p0188.txt`
- `p0189`: image `/tmp/novels/story-of-a-life-sherer/pages/p0189.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/story-of-a-life-sherer/draft/p0189.txt`
- `p0190`: image `/tmp/novels/story-of-a-life-sherer/pages/p0190.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/story-of-a-life-sherer/draft/p0190.txt`
- `p0191`: image `/tmp/novels/story-of-a-life-sherer/pages/p0191.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/story-of-a-life-sherer/draft/p0191.txt`
- `p0192`: image `/tmp/novels/story-of-a-life-sherer/pages/p0192.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/story-of-a-life-sherer/draft/p0192.txt`
- `p0193`: image `/tmp/novels/story-of-a-life-sherer/pages/p0193.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/story-of-a-life-sherer/draft/p0193.txt`
- `p0194`: image `/tmp/novels/story-of-a-life-sherer/pages/p0194.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/story-of-a-life-sherer/draft/p0194.txt`
- `p0195`: image `/tmp/novels/story-of-a-life-sherer/pages/p0195.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/story-of-a-life-sherer/draft/p0195.txt`
- `p0196`: image `/tmp/novels/story-of-a-life-sherer/pages/p0196.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/story-of-a-life-sherer/draft/p0196.txt`
- `p0197`: image `/tmp/novels/story-of-a-life-sherer/pages/p0197.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/story-of-a-life-sherer/draft/p0197.txt`
- `p0198`: image `/tmp/novels/story-of-a-life-sherer/pages/p0198.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/story-of-a-life-sherer/draft/p0198.txt`
- `p0199`: image `/tmp/novels/story-of-a-life-sherer/pages/p0199.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/story-of-a-life-sherer/draft/p0199.txt`
- `p0200`: image `/tmp/novels/story-of-a-life-sherer/pages/p0200.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/story-of-a-life-sherer/draft/p0200.txt`
- `p0201`: image `/tmp/novels/story-of-a-life-sherer/pages/p0201.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/story-of-a-life-sherer/draft/p0201.txt`
- `p0202`: image `/tmp/novels/story-of-a-life-sherer/pages/p0202.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/story-of-a-life-sherer/draft/p0202.txt`
- `p0203`: image `/tmp/novels/story-of-a-life-sherer/pages/p0203.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/story-of-a-life-sherer/draft/p0203.txt`
- `p0204`: image `/tmp/novels/story-of-a-life-sherer/pages/p0204.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/story-of-a-life-sherer/draft/p0204.txt`
- `p0205`: image `/tmp/novels/story-of-a-life-sherer/pages/p0205.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/story-of-a-life-sherer/draft/p0205.txt`
- `p0206`: image `/tmp/novels/story-of-a-life-sherer/pages/p0206.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/story-of-a-life-sherer/draft/p0206.txt`
