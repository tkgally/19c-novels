# Draft Transcription Batch 7 (54 pages)

1. First read the transcription rules and markup specification in `/home/antigravity/tkgally/19c-novels/prompts/transcribe.md`.
2. For each page listed below, inspect the scan image directly with `view_file` (do NOT use IA's `_djvu.txt` or OCR files; transcribe strictly from the visual scan) and write the exact page-markup transcription to its output `.txt` file using `write_to_file`.
3. Watch carefully for two known pitfalls: NEVER modernize or normalize unusual/old spellings (e.g. keep `neophite`, `shew`, `connexion`, `to-day` exactly as printed), and keep roman parentheses/brackets OUTSIDE `<i>…</i>` tags.
4. If the platform blocks outputting any page due to a recitation/content filter, do NOT retry or rephrase that page; instead append `{"page": "<stem>", "error": "recitation"}` to `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/log.jsonl` and continue to the next page.

## Pages in this batch

- `p1025`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1025.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1025.txt`
- `p1026`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1026.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1026.txt`
- `p1027`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1027.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1027.txt`
- `p1028`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1028.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1028.txt`
- `p1029`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1029.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1029.txt`
- `p1030`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1030.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1030.txt`
- `p1031`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1031.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1031.txt`
- `p1032`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1032.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1032.txt`
- `p1033`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1033.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1033.txt`
- `p1034`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1034.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1034.txt`
- `p1035`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1035.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1035.txt`
- `p1036`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1036.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1036.txt`
- `p1037`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1037.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1037.txt`
- `p1038`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1038.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1038.txt`
- `p1039`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1039.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1039.txt`
- `p1040`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1040.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1040.txt`
- `p1041`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1041.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1041.txt`
- `p1042`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1042.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1042.txt`
- `p1043`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1043.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1043.txt`
- `p1044`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1044.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1044.txt`
- `p1045`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1045.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1045.txt`
- `p1046`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1046.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1046.txt`
- `p1047`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1047.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1047.txt`
- `p1048`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1048.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1048.txt`
- `p1049`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1049.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1049.txt`
- `p1050`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1050.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1050.txt`
- `p1051`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1051.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1051.txt`
- `p1052`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1052.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1052.txt`
- `p1053`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1053.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1053.txt`
- `p1054`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1054.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1054.txt`
- `p1055`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1055.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1055.txt`
- `p1056`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1056.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1056.txt`
- `p1057`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1057.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1057.txt`
- `p1058`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1058.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1058.txt`
- `p1059`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1059.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1059.txt`
- `p1060`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1060.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1060.txt`
- `p1061`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1061.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1061.txt`
- `p1062`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1062.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1062.txt`
- `p1063`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1063.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1063.txt`
- `p1064`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1064.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1064.txt`
- `p1065`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1065.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1065.txt`
- `p1066`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1066.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1066.txt`
- `p1067`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1067.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1067.txt`
- `p1068`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1068.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1068.txt`
- `p1069`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1069.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1069.txt`
- `p1070`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1070.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1070.txt`
- `p1071`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1071.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1071.txt`
- `p1072`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1072.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1072.txt`
- `p1073`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1073.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1073.txt`
- `p1074`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1074.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1074.txt`
- `p1075`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1075.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1075.txt`
- `p1076`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1076.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1076.txt`
- `p1077`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1077.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1077.txt`
- `p1078`: image `/tmp/novels/by-the-cornish-sea-isabell/pages/p1078.jpg` -> write `/home/antigravity/tkgally/19c-novels/wip/by-the-cornish-sea-isabell/draft/p1078.txt`
