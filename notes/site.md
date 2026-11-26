# The site as it grows

Built by `tools/build_site.py` into `_site/` and deployed to `https://tkgally.github.io/19c-novels/` by `.github/workflows/pages.yml`.

## Pages

| Page | Purpose | Built from |
|---|---|---|
| `index.html` | cover carousel (`carousel_html`), hidden `<h1>Forgotten Novels</h1>`, two short introductory paragraphs, link to `about.html` | `data/carousel.json`, `site/carousel/` |
| `books.html` | up to 30 novels: all novels by author + link to `dates.html` + queue; above 30 novels: 10 newest + links to `authors.html` and `dates.html` + queue | `books/*/book.json`, `data/queue.json`, `data/published.json` |
| `dates.html` | novels grouped by decade of publication (`1700s` … `1910s`) | `year` in `book.json` |
| `authors.html` | novels grouped alphabetically by author surname (written once more than 30 novels are published) | `authors[0].sort` |
| `about.html`, `json-format.html` | project explanation, editorial rules, Display settings, and JSON schema | `site/about.md`, `site/json-format.md` |
| `books/<id>/…` | novel index page (`index.html`), reading pages (`01.html`…), `<id>.json`, `images/` | `books/<id>/` |
| GitHub Releases (`book-<id>`) | `<id>-v<N>.epub` and `<id>-v<N>.odt` uploaded and removed from `_site/` by `tools/releases.py` so GitHub Pages stays well under 1 GB | `_site/` during Actions build |

Each novel line in the lists shows `<cite>Short Title</cite>, Author (Year)` and on the second line `<span class="meta">Setting · Period</span>`.
