---
name: select-novel
description: Find, vet, and queue pre-1914 English novels from the Internet Archive that have no other digital reading edition and no post-1914 print edition. Use when fewer than six novels are queued or when adding candidates from data/blog_2021.json or broader IA searches.
---

# Select and vet candidate novels

Follow `notes/selection.md` strictly. Every queued novel must pass **all four** eligibility conditions before any transcription work begins.

## 1. Where to look

1. **Unvetted entries in `data/blog_2021.json`** (Tom Gally’s July 14, 2021 IA blog post of 50 forgotten 19th-century novels). Check which numbers `n` are not yet in `data/queue.json` (`books` or `rejected`). Remember: `blog_2021.json` is a starting seed list, **not** an exemption — several books from 2021 may since have entered Project Gutenberg, Wikisource, or modern reprint series, or may have incomplete `goog` scans!
2. **Broader Internet Archive searches** (`python3 tools/ia.py search 'subject:fiction ...'`), aiming to balance decades across **1700–1914** (including 18th-century and 1900–1913 novels alongside 19th-century ones), settings, themes, single-volume and multi-volume formats, and a wide range of authors without preferring any demographic group.

## 2. Vet every candidate thoroughly (delegate batches of 3–4 to `pro` subagents)

For each candidate:
1. **Scan check (`ia.py meta <id>`):**
   - Confirm every volume of the novel is present on IA and has a `_jp2.zip` or `_jp2.tar` archive. (Watch out for orphan single volumes of 3-deckers, e.g. an item whose title page or spine says `Vol. III`!)
   - Prefer clean library scans (`uoft`, `uiuc`, `cdl`/`rich`, `bodleian`, `bl`, `loc`) over blurry bilevel `goog` scans; search IA for alternative scans of the same pre-1914 edition if needed.
   - Sample ~20 lines of `_djvu.txt` from the middle to confirm it is an English novel (not a play, treatise, collection of essays, or translation) and is readable.
2. **No digital reading edition elsewhere:**
   - Search Project Gutenberg’s `pg_catalog.csv` by author and title words.
   - Check Standard Ebooks, The Online Books Page (`onlinebooks.library.upenn.edu`), English Wikisource, Faded Page, and A Celebration of Women Writers.
   - Run a quoted web search on a distinctive sentence from the novel plus `"Title" "Author" ebook OR gutenberg`.
   - Raw OCR (IA, HathiTrust, Google Books) and non-reading scholarly/subscription databases (EEBO-TCP, ECCO-TCP, Gale, ProQuest) do **not** disqualify; note them in `eligibility`.
3. **No post-1914 print edition:**
   - Check Open Library (`openlibrary.org/search.json`) and web search (`"Title" "Author" edition OR reprint OR press`).
   - Print-on-demand scan replicas (Kessinger, Forgotten Books, Nabu, Palala, Wentworth, Legare Street, Creative Media Partners, Hansebooks, BiblioLife) do **not** count.
   - Reset editions or established publisher/scholarly reprints (Oxford, Penguin, Broadview, Virago, Valancourt, Garland, Routledge, AMS, Arno, Cambridge Library Collection, Victorian Secrets, etc.) **disqualify** the novel.

## 3. Record in `data/queue.json` and check

- Qualifying novels go into `data/queue.json` `books` (`"status": "queued"`, `"slug"`, `"title"`, `"author"`, `"year"`, `"volumes"`, `"ia"` and optional `"ia_items"`, `"images"`, `"setting"`, `"period"`, optional `"from": "blog_2021"` and `"blog_2021": N`, and a detailed `"eligibility"` string naming every source checked and date).
- Disqualified candidates go into `data/queue.json` `rejected` (`{"title", "author", "year", "ia", "blog_2021"?, "why"}`) so future sessions never re-check them.
- Run `python3 tools/ledger.py check` and `tools/run_tests.sh` before committing.
