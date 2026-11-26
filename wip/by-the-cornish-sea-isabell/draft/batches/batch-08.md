# Draft Transcription Batch 8 (54 pages)

1. First read the transcription rules and markup specification in `/home/antigravity/tkgally/19c-novels/prompts/transcribe.md`.
2. For each page listed below, inspect the scan image directly with `view_file` (do NOT use IA's `_djvu.txt` or OCR files; transcribe strictly from the visual scan) and write the exact page-markup transcription to its output `.txt` file using `write_to_file`.
3. Watch carefully for two known pitfalls: NEVER modernize or normalize unusual/old spellings (e.g. keep `neophite`, `shew`, `connexion`, `to-day` exactly as printed), and keep roman parentheses/brackets OUTSIDE `<i>…</i>` tags.
4. If the platform blocks outputting any page due to a recitation/content filter, do NOT retry or rephrase that page; instead append `{"page": "<stem>", "error": "recitation"}` to `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/log.jsonl` and continue to the next page.

## Pages in this batch

- `p1079`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1079.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1079.txt`
- `p1080`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1080.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1080.txt`
- `p1081`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1081.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1081.txt`
- `p1082`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1082.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1082.txt`
- `p1083`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1083.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1083.txt`
- `p1084`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1084.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1084.txt`
- `p1085`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1085.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1085.txt`
- `p1086`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1086.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1086.txt`
- `p1087`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1087.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1087.txt`
- `p1088`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1088.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1088.txt`
- `p1089`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1089.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1089.txt`
- `p1090`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1090.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1090.txt`
- `p1091`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1091.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1091.txt`
- `p1092`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1092.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1092.txt`
- `p1093`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1093.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1093.txt`
- `p1094`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1094.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1094.txt`
- `p1095`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1095.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1095.txt`
- `p1096`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1096.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1096.txt`
- `p1097`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1097.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1097.txt`
- `p1098`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1098.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1098.txt`
- `p1099`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1099.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1099.txt`
- `p1100`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1100.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1100.txt`
- `p1101`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1101.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1101.txt`
- `p1102`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1102.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1102.txt`
- `p1103`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1103.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1103.txt`
- `p1104`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1104.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1104.txt`
- `p1105`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1105.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1105.txt`
- `p1106`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1106.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1106.txt`
- `p1107`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1107.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1107.txt`
- `p1108`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1108.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1108.txt`
- `p1109`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1109.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1109.txt`
- `p1110`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1110.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1110.txt`
- `p1111`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1111.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1111.txt`
- `p1112`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1112.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1112.txt`
- `p1113`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1113.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1113.txt`
- `p1114`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1114.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1114.txt`
- `p1115`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1115.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1115.txt`
- `p1116`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1116.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1116.txt`
- `p1117`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1117.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1117.txt`
- `p1118`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1118.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1118.txt`
- `p1119`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1119.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1119.txt`
- `p1120`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1120.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1120.txt`
- `p1121`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1121.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1121.txt`
- `p1122`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1122.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1122.txt`
- `p1123`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1123.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1123.txt`
- `p1124`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1124.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1124.txt`
- `p1125`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1125.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1125.txt`
- `p1126`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1126.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1126.txt`
- `p1127`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1127.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1127.txt`
- `p1128`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1128.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1128.txt`
- `p1129`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1129.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1129.txt`
- `p1130`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1130.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1130.txt`
- `p1131`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1131.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1131.txt`
- `p1132`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1132.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1132.txt`
