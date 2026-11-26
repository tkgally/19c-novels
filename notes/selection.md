# Choosing novels

## What qualifies (Tom, 2026-11-26 — all required)

1. **Complete scan on the Internet Archive.** Every volume of the novel has a complete, readable scan on IA (`_jp2.zip` or `_jp2.tar`), with no text pages missing, clipped, or illegible. Checked before any transcription (`workflow.md` §1.4). If one scan is defective, another IA scan of the same edition may be used (or individual leaves supplied via `source.extra_leaves`, noted in `notes_on_text`).
2. **Novel in English, 1700–1914.** A novel written in English (not a translation from another language) and published between 1700 and 1914 (`1700 <= year <= 1913`). Short-story collections, plays, verse narratives, essays, and nonfiction are excluded.
3. **No digital reading edition elsewhere.** No free edition of the novel formatted for reading exists on the Internet — including Project Gutenberg, Standard Ebooks, Wikisource, Faded Page, A Celebration of Women Writers, British Women Romantic Poets / Victorian Women Writers Project (where free and formatted for reading), or independent e-text sites. Brief excerpts do not count. Nor do:
   - raw OCR, alone or behind page images (IA, HathiTrust, Google Books, British Library viewer);
   - texts in subscription library databases (Gale, ProQuest, Alexander Street, Adam Matthew);
   - texts in online scholarly databases not formatted for immersive reading, such as EEBO-TCP and ECCO-TCP, even where free (record in `eligibility` if found).
4. **Not republished in print since 1914.** No real reset, publisher’s, or scholarly print edition after 1914 (such as Oxford World’s Classics, Penguin, Virago, Broadview, Valancourt, Garland’s Victorian Fiction / Novels of Faith and Doubt series, Routledge, AMS, Arno, Cambridge Library Collection, Victorian Secrets, Dover, etc.). Print-on-demand replicas of library scans (Kessinger, Forgotten Books, Palala, Nabu, Wentworth, HardPress, Franklin Classics, BiblioLife, Creative Media Partners, Legare Street, Hansebooks, Sagwan, CreateSpace replicas) do **not** count.
5. **Public domain** (Tom, 2026-11-26): every author, artist, and illustrator of a book published before 1914 is assumed to have died more than 70 years ago.

## Role of the 2021 blog list (`data/blog_2021.json`)

Tom’s July 14, 2021 Internet Archive blog post, [“Forgotten Novels of the 19th Century”](https://blog.archive.org/2021/07/14/forgotten-novels-of-the-19th-century/), lists fifty 19th-century novels that had zero ratings and zero reviews on Goodreads in May 2021. Those fifty titles are stored in `data/blog_2021.json` as our initial starting pool, **provided they still meet all four conditions above**. Always vet each candidate fresh before queuing (`blog_2021` is recorded on the queue row as provenance, not an exemption).

## How to check (record every check in the queue row’s `eligibility`)

- **Project Gutenberg**: search `pg_catalog.csv` locally by author surname and distinctive title words.
- **Standard Ebooks**: search `standardebooks.org/ebooks` or web search `site:standardebooks.org`.
- **The Online Books Page** (`onlinebooks.library.upenn.edu/webbin/book/search?...`): links only to page scans (HathiTrust/IA) do not disqualify; links to HTML/EPUB reading editions do.
- **Wikisource**: search `en.wikisource.org` API for title and author.
- **Faded Page** and **A Celebration of Women Writers**: search author/title lists.
- **Quoted phrase search**: search Google for a distinctive 7–10 word phrase from the novel in quotation marks, plus `"Title" "Author" ebook OR gutenberg OR reprint OR edition`.
- **Post-1914 reprints**: check Open Library (`openlibrary.org/search.json`) and web search for publisher/scholarly editions (paying particular attention to Garland, Valancourt, Virago, Broadview, Cambridge Library Collection, Oxford, Penguin).
- **IA scan**: `python3 tools/ia.py meta <id>` (confirm `_jp2.zip`/`_jp2.tar`, volume count, contributor library; prefer UIUC, Toronto, California, Bodleian, LOC over blurry bilevel `goog` scans).

## Choosing among qualifying novels

Aim for a wide, engaging shelf:
- **Readable prose and narrative life**: sample 20–30 lines from the middle of `_djvu.txt` before queuing.
- **Variety across the collection**: vary decades across the full **1700–1914** span (18th century, Regency, early/mid/late Victorian, Edwardian), settings (provincial, metropolitan, historical, colonial/international), genres/themes (social satire, domestic realism, mystery/sensation, historical romance, industrial/political fiction), single-volume and multi-volume works, and authors — without preferring or passing over books by an author’s gender or background.
- Keep at least **six** vetted novels `queued` in `data/queue.json`; record every disqualified candidate in `data/queue.json` `rejected` with the reason so no session checks it twice.
