# Tom’s decisions

## 2026-11-26 (project set-up)

- **Purpose:** a public, open-ended digital-editions project making lesser-known and forgotten novels written in English available to a wider public in readable, reliable formats (HTML web pages, EPUB, ODT, and JSON), dedicated to the public domain (CC0 1.0).
- **Site name:** **Forgotten Novels** (`https://tkgally.github.io/19c-novels/`), covering novels published between 1700 and 1914 and echoing Tom’s July 14, 2021 Internet Archive blog post, [“Forgotten Novels of the 19th Century”](https://blog.archive.org/2021/07/14/forgotten-novels-of-the-19th-century/).
- **Starting seed list:** the fifty 19th-century novels in Tom’s 2021 Internet Archive blog post serve as a starting point **if they still qualify** under the four selection conditions (unlike JATSI in `travel-books`, the blog-post list is not an exemption from the eligibility rules).
- **Selection conditions (all required):**
  1. Complete, readable scans of the novel are available on the Internet Archive.
  2. Written in English and published between 1700 and 1914.
  3. Not available in digital reader editions elsewhere (such as Project Gutenberg, Standard Ebooks, Wikisource, Faded Page, or A Celebration of Women Writers; raw OCR and scholarly/subscription databases not formatted for immersive reading, such as EEBO-TCP and ECCO-TCP, do not count).
  4. Not republished in print since 1914 (print-on-demand scan reprints do not count; real reset, publisher’s, or scholarly editions do).
  5. Public domain: following Tom’s standing rule (2026-11-26), any author, artist, or illustrator of a book published before 1914 is assumed to have died more than 70 years ago.
- **Variety:** Gemini selects qualifying novels aiming for a wide variety of authors, themes, settings, and decades of publication, without preferring any particular demographic group.
- **Multi-volume novels (“three-deckers” and other multi-volume sets):** combined and published digitally as **single volumes**. In the HTML, EPUB, and ODT reading editions, the book opens with Volume I’s title page, and Volumes I, II, III, etc. are presented as Parts keeping each volume’s own chapter numbering underneath; later volumes’ title pages and front matter are preserved in the JSON only.
- **Design and adaptation from `travel-books`:** workflow, scripts, skills, editorial conventions, quality checks (`preflight.py`, `epubcheck`, LibreOffice ODT conversion, planted-error sampled audits), and website design are adapted from `tkgally/travel-books`, excluding parts specific to travel books (such as JATSI, travel route regions, and journey dates). The `travel-books` repository itself is never modified by this project.
- **Website lists and metadata:** each novel’s list entry shows a brief setting and time-period line under its title, author, and publication year; browse lists are organized by author and by publication decade (`dates.html`), with `books.html` listing all novels (and switching to newest + full lists as the shelf grows). EPUB and ODT downloads are hosted on GitHub Releases so the GitHub Pages site remains well under 1 GB.
- **Google Drive scan cache:** Internet Archive downloads and prepared working page images are cached in Tom’s Google Drive folder **“19C Novels”** (`1ecaIjeQldRJ8cfAD1-mGtNbofezQLbcy`), one subfolder per novel slug, so the Internet Archive’s servers are not hit repeatedly. Scans and working page archives are never committed to git.
- **Models and multi-pass verification:** run by Gemini in Antigravity. Subagents use **Gemini Pro** (`pro`) for drafting, blind judging of disagreements, and planted-error sampled audits, and **Gemini Flash** (`flash`) for the second-pass verification check so two distinct models check each page, backed by Tesseract OCR comparisons, scan-crop inspection, and mechanical `preflight.py` checks.
- **Continuous evaluation and live deployment:** continuously monitor and evaluate transcription accuracy and pipeline performance, keep repository documentation (`RESUME.md`, `notes/`) current with the latest findings, and merge and deploy to `main` once all preflight checks and audits pass.

## Questions for Tom

*(None at present.)*
