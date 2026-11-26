#!/usr/bin/env python3
"""Build the whole Forgotten Novels website into a directory (default _site/). Run by the Pages workflow and by preflight.

  build_site.py [--out _site] [--only SLUG] [--bookdir DIR]

For every novel in books/<slug>/ (or the one given with --bookdir, e.g. a novel still in wip/):
  books/<slug>/index.html     the novel's page
  books/<slug>/NN.html        the reading text, one file per division
  books/<slug>/<slug>.json    the book JSON (base of everything else)
  books/<slug>/<slug>.epub, <slug>.odt   for preflight and the tests; the Pages workflow uploads them to GitHub
                              Releases and removes them from the site (tools/releases.py), and the novel's page
                              links to the release files (download_url)
  books/<slug>/images/
Plus index.html, books.html, dates.html (authors.html when there are many books), about.html, json-format.html, assets/.
Standard library only; output is deterministic.
"""
import argparse, html, json, os, re, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import compile_book, inline, releases, render_html as rh, render_epub, render_odt  # noqa: E402

SITE = "Forgotten Novels"
REPO_URL = "https://github.com/tkgally/19c-novels"


def download_url(book, ext):
    return (f"{REPO_URL}/releases/download/{releases.tag_for(book['id'])}/"
            f"{releases.asset_name(book['id'], book['version'], ext)}")


LOGO = ('<svg class="logo" viewBox="0 0 32 29.5" width="32" height="29.5" aria-hidden="true" focusable="false">'
        '<rect class="logo-i" x="2.5" y="23" width="27" height="6.5" rx="1"/>'
        '<rect class="logo-a" x="5" y="15.5" width="23" height="6.5" rx="1"/>'
        '<rect class="logo-i" x="3.5" y="8" width="21" height="6.5" rx="1" transform="rotate(-6 14 11.25)"/>'
        '<path class="logo-k" stroke-width="1.4" d="M7 23V29.5M9.5 15.5V22"/></svg>')
esc = rh.esc
attr = rh.attr


def outside_links(html_):
    return re.sub(r'<a (?![^>]*\btarget=)([^>]*\bhref="https?://[^"]*"[^>]*)>', r'<a \1 target="_blank" rel="noopener">', html_)


BOOKS_PAGE = "books.html"
HOME_FULL_LIST = 30
HOME_NEWEST = 10


def page(title, body, root, crumbs=(), extra_head="", book_css=False, before_main=""):
    return outside_links(_page(title, body, root, crumbs, extra_head, book_css, before_main))


def _page(title, body, root, crumbs=(), extra_head="", book_css=False, before_main=""):
    nav = "".join(f'<li><a href="{attr(h)}">{esc(t)}</a></li>' for t, h in crumbs)
    css = f'<link rel="stylesheet" href="{root}assets/book.css"/>' if book_css else ""
    full = f"{title} – {SITE}" if title != SITE else SITE
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>{esc(full)}</title>
<link rel="icon" href="{root}assets/logo.svg" type="image/svg+xml"/>
<link rel="stylesheet" href="{root}assets/site.css"/>
{css}{extra_head}
<script src="{root}assets/site.js"></script>
</head>
<body>
<a class="skip" href="#main">Skip to the text</a>
<header class="site">
<p class="sitename"><a href="{root}index.html">{LOGO}{SITE}</a></p>
<nav aria-label="Site"><ul><li><a href="{root}{BOOKS_PAGE}">Books</a></li><li><a href="{root}about.html">About</a></li></ul></nav>
</header>
{f'<nav class="crumbs" aria-label="Breadcrumb"><ol>{nav}</ol></nav>' if nav else ''}
{before_main}<main id="main">
{body}
</main>
<footer class="site">
<p>The transcriptions on this site are in the public domain (<a href="https://creativecommons.org/publicdomain/zero/1.0/">CC0 1.0</a>).
Found an error? <a href="{REPO_URL}/issues">Report it on GitHub</a>.</p>
</footer>
</body>
</html>
"""


def setting_text(b):
    st = b.get("setting", "")
    return ", ".join(st) if isinstance(st, list) else str(st or "")


def book_line(b, href):
    a = rh.authors_text(b)
    meta = []
    st = setting_text(b)
    if st:
        meta.append(esc(st))
    if b.get("period"):
        meta.append(esc(str(b["period"])))
    return (f'<li><a href="{attr(href)}"><cite>{esc(b.get("short_title") or b["title"])}</cite></a>, {esc(a)} ({b.get("year", "")})'
            + (f'<br/><span class="meta">{" · ".join(meta)}</span>' if meta else "") + "</li>")


def sort_key(b):
    a = (b.get("authors") or [{}])[0]
    return (a.get("sort") or a.get("name") or "", b.get("year") or 0, b.get("id", ""))


def first_published(b, times=None):
    if times and b.get("id") in times:
        return times[b["id"]]
    h = b.get("history") or []
    return (h[0].get("date") if h else None) or b.get("date") or ""


def load_published_times():
    f = os.path.join(REPO, "data", "published.json")
    return json.load(open(f, encoding="utf-8")) if os.path.exists(f) else {}


def pub_year(b):
    m = re.search(r"\b(1[7-9]\d\d)\b", str(b.get("year", "")))
    return int(m.group(1)) if m else 0


def books_ul(bs):
    return '<ul class="books">' + "\n".join(book_line(b, f"books/{b['id']}/index.html") for b in bs) + "</ul>"


def queue_line(x):
    scans = x.get("ia_items") or ([{"label": "scan", "ia_identifier": x["ia"]}] if x.get("ia") else [])
    scan_html = ""
    if len(scans) == 1:
        scan_html = f' <span class="meta"><a href="https://archive.org/details/{attr(scans[0]["ia_identifier"])}">scan</a></span>'
    elif len(scans) > 1:
        links = ", ".join(f'<a href="https://archive.org/details/{attr(s["ia_identifier"])}">{esc(s.get("label") or f"vol. {i}")}</a>'
                          for i, s in enumerate(scans, 1))
        scan_html = f' <span class="meta">({links})</span>'
    return (f'<li><cite>{esc(inline.smart_quotes(x["title"]))}</cite>, {esc(inline.smart_quotes(x.get("author", "")))} ({x.get("year", "")})'
            + (' <span class="meta">— in progress</span>' if x["status"] == "in progress" else "")
            + scan_html + "</li>")


CAROUSEL_DIR = "carousel"


def load_carousel():
    f = os.path.join(REPO, "data", "carousel.json")
    return json.load(open(f, encoding="utf-8")).get("books", {}) if os.path.exists(f) else {}


def carousel_html(books, record, have):
    items = []
    for b in sorted(books, key=lambda b: b["id"]):
        r = record.get(b["id"])
        if not r or b["id"] + ".jpg" not in have:
            continue
        a = rh.authors_text(b)
        alt = (b.get("short_title") or b["title"]) + (f", by {a}" if a else "")
        items.append(f'<li><a href="books/{attr(b["id"])}/index.html"><img src="{CAROUSEL_DIR}/{attr(b["id"])}.jpg" alt="{attr(alt)}" '
                     f'width="{int(r["width"])}" height="{int(r["height"])}" loading="lazy" decoding="async"/></a></li>')
    if not items:
        return ""
    return '<nav class="carousel" aria-label="Some of the books"><ul>\n' + "\n".join(items) + "\n</ul></nav>\n"


def build_index(out, carousel="", nbooks=0):
    if nbooks == 1:
        count = " The site now contains 1 novel, with more being added regularly."
    elif nbooks > 1:
        count = f" The site now contains {nbooks} novels, with more being added regularly."
    else:
        count = ""
    body = f"""<h1 class="visually-hidden">{SITE}</h1>
<p>Lesser-known and forgotten novels written in English and published between 1700 and 1914, transcribed from library scans at the
Internet Archive. Each can be read on this site or downloaded as EPUB, ODT, or JSON.{count}</p>
<p>The novels are chosen because they have no other digital reading edition and have not been republished in print since 1914. Works originally issued in two, three, or more volumes are published here as single digital volumes.</p>
<p><a href="about.html">More about the project.</a></p>
"""
    open(os.path.join(out, "index.html"), "w", encoding="utf-8").write(page(SITE, body, "", before_main=carousel))


def build_books(out, books, queue, times=None):
    books = sorted(books, key=sort_key)
    if not books:
        shelf = "<p>No books have been published yet.</p>"
    elif len(books) <= HOME_FULL_LIST:
        shelf = f'<p class="meta">By author. Also listed by <a href="dates.html">decade of publication</a>.</p>\n{books_ul(books)}'
    else:
        newest = sorted(books, key=lambda b: (first_published(b, times), b["id"]), reverse=True)[:HOME_NEWEST]
        shelf = (f'<p>{len(books)} novels, listed by <a href="authors.html">author</a> and by <a href="dates.html">decade of publication</a>.</p>\n'
                 f'<h2 id="newest">Newest</h2>\n{books_ul(newest)}')
    q = [x for x in queue if x.get("status") in ("queued", "in progress")]
    qitems = "\n".join(queue_line(x) for x in q)
    body = f"""<h1>Books</h1>
{shelf}
<h2 id="queue">In the queue</h2>
{f'<p>Novels chosen for transcription, not yet published.</p><ul class="books">{qitems}</ul>' if qitems else '<p>The queue is empty.</p>'}
"""
    open(os.path.join(out, BOOKS_PAGE), "w", encoding="utf-8").write(page("Books", body, ""))


def build_lists(out, books):
    books = sorted(books, key=sort_key)
    many = len(books) > HOME_FULL_LIST
    kinds = [("authors.html" if many else BOOKS_PAGE, "author"), ("dates.html", "decade of publication")]

    def write(name, title, intro, groups):
        toc = " · ".join(f'<a href="#{attr(i)}">{esc(t)}</a>' for i, t, bs in groups)
        also = " and by ".join(f'<a href="{h}">{t}</a>' for h, t in kinds if h != name)
        body = (f"<h1>{esc(title)}</h1>\n<p>{intro}</p>\n<p class=\"meta\">Also listed by {also}.</p>\n"
                + (f'<p class="meta">{toc}</p>\n' if len(groups) > 1 else "")
                + ("\n".join(f'<h2 id="{attr(i)}">{esc(t)}</h2>\n{books_ul(bs)}' for i, t, bs in groups)
                   if groups else "<p>No books have been published yet.</p>"))
        open(os.path.join(out, name), "w", encoding="utf-8").write(page(title, body, ""))

    def ident(t):
        return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")

    by_dec = {}
    for b in sorted(books, key=lambda b: (pub_year(b),) + sort_key(b)):
        by_dec.setdefault(pub_year(b) // 10 * 10, []).append(b)
    write("dates.html", "Books by decade of publication",
          "By the decade in which the edition transcribed here was published.",
          [(f"d{d}", f"{d}s", bs) for d, bs in sorted(by_dec.items())])
    if many:
        by_letter = {}
        for b in books:
            by_letter.setdefault((sort_key(b)[0][:1] or "?").upper(), []).append(b)
        write("authors.html", "Books by author", "By the first author’s surname.",
              [(f"a-{ident(k) or 'x'}", k, bs) for k, bs in sorted(by_letter.items())])


def md_page(out, name, title, src):
    lines = open(src, encoding="utf-8").read().splitlines()
    outl, i = [], 0

    def inl(s):
        s = "".join(x if x.startswith("`") else inline.smart_quotes(x) for x in re.split(r"(`[^`]+`)", s))
        s = esc(s)
        s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
        s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
        s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
        s = re.sub(r"(?<![\w*])\*([^*]+)\*(?![\w*])", r"<em>\1</em>", s)
        return s
    while i < len(lines):
        ln = lines[i]
        if ln.startswith("```"):
            j = i + 1
            while j < len(lines) and not lines[j].startswith("```"):
                j += 1
            outl.append("<pre><code>" + esc("\n".join(lines[i + 1:j])) + "</code></pre>")
            i = j + 1
        elif re.match(r"#{1,3} ", ln):
            n = len(ln.split(" ")[0])
            text = ln[n + 1:]
            ident = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
            outl.append(f'<h{n} id="{ident}">{inl(text)}</h{n}>')
            i += 1
        elif ln.startswith("- "):
            items = []
            while i < len(lines) and (lines[i].startswith("- ") or lines[i].startswith("  ")):
                if lines[i].startswith("- "):
                    items.append(lines[i][2:])
                else:
                    items[-1] += " " + lines[i].strip()
                i += 1
            outl.append("<ul>" + "".join(f"<li>{inl(x)}</li>" for x in items) + "</ul>")
        elif ln.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                if not re.fullmatch(r"\|[-| :]+\|", lines[i].strip()):
                    rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            head = "<tr>" + "".join(f'<th scope="col">{inl(c)}</th>' for c in rows[0]) + "</tr>"
            rest = "".join("<tr>" + "".join(f"<td>{inl(c)}</td>" for c in r) + "</tr>" for r in rows[1:])
            outl.append(f'<div class="tablewrap"><table class="doc"><thead>{head}</thead><tbody>{rest}</tbody></table></div>')
        elif not ln.strip():
            i += 1
        else:
            para = []
            while i < len(lines) and lines[i].strip() and not re.match(r"(#{1,3} |- |\||```)", lines[i]):
                para.append(lines[i].strip())
                i += 1
            outl.append("<p>" + inl(" ".join(para)) + "</p>")
    open(os.path.join(out, name), "w", encoding="utf-8").write(page(title, "\n".join(outl), ""))


def with_h1(body, d, added):
    if "<h1" in body:
        return added
    if d.get("added"):
        return added.replace('<h2 class="added">', '<h1 class="added">', 1).replace("</h2>", "</h1>", 1)
    return f'<h1 class="visually-hidden">{esc(d["title"])}</h1>\n' + added


def build_book(out, bookdir, strict=True):
    book, warnings = compile_book.compile_book(bookdir)
    slug = book["id"]
    cfg = json.load(open(os.path.join(bookdir, "book.json"), encoding="utf-8"))
    bout = os.path.join(out, "books", slug)
    os.makedirs(bout, exist_ok=True)
    idir = os.path.join(bookdir, "images")
    open(os.path.join(bout, slug + ".json"), "w", encoding="utf-8").write(compile_book.dumps(book))
    open(os.path.join(bout, slug + ".epub"), "wb").write(render_epub.render(book, idir))
    open(os.path.join(bout, slug + ".odt"), "wb").write(render_odt.render(book, idir))
    names = rh.file_names(book, ".html")
    ctx = rh.Ctx(book, "web", names)
    divs = rh.reading_divisions(book)
    used = set()
    short = book.get("short_title") or book["title"]
    extra = f"<style>{cfg['css_extra']}</style>" if cfg.get("css_extra") else ""
    start = rh.body_start(book)
    for i, d in enumerate(divs):
        body = ctx.blocks(d)
        if start is not None and d["id"] == start["id"]:
            body, n = re.subn(r"<h1>", f'<h1 id="{START_ID}">', body, count=1)
            if not n:
                body = f'<span id="{START_ID}"></span>' + body
        added = f'<h2 class="added">{esc(d["added"])}</h2>\n' if d.get("added") else ""
        added += rh.editor_figures(book, d)
        added = with_h1(body, d, added)
        used.update(re.findall(r'<img src="images/([^"]+)"', body + added))
        prev_ = f'<a rel="prev" href="{names[divs[i - 1]["id"]]}">← {esc(divs[i - 1]["title"])}</a>' if i else "<span></span>"
        next_ = f'<a rel="next" href="{names[divs[i + 1]["id"]]}">{esc(divs[i + 1]["title"])} →</a>' if i + 1 < len(divs) else "<span></span>"
        pager = f'<nav class="pager" aria-label="Chapters">{prev_}<a href="index.html#contents">Contents</a>{next_}</nav>'
        toggle = ('<p class="pbtoggle"><label><input type="checkbox" id="showpb"/> Show the page numbers of the printed book '
                  "(each links to the scanned page)</label></p>")
        html_ = page(f"{d['title']} – {short}",
                     f'{pager}\n{toggle}\n{added}<article class="book">\n{body}\n</article>\n{pager}', "../../",
                     crumbs=[(short, "index.html"), (d["title"], names[d["id"]])],
                     extra_head=extra, book_css=True)
        open(os.path.join(bout, names[d["id"]]), "w", encoding="utf-8").write(html_)
    if os.path.isdir(idir):
        os.makedirs(os.path.join(bout, "images"), exist_ok=True)
        for f in sorted(used | ({"cover.jpg", "cover.png"} & set(os.listdir(idir)))):
            if os.path.exists(os.path.join(idir, f)):
                shutil.copyfile(os.path.join(idir, f), os.path.join(bout, "images", f))
    has_cov = any(os.path.exists(os.path.join(idir, f)) for f in ("cover.jpg", "cover.png"))
    open(os.path.join(bout, "index.html"), "w", encoding="utf-8").write(
        book_page(book, names, has_cov, (load_carousel().get(slug) or {}).get("image"))
    )
    return book, warnings


def correction_page(book, c, pnum):
    n = pnum.get(c["leaf"], "")
    if n:
        return n
    title = next((d.get("title") for d in book.get("divisions", []) if d.get("id") == c.get("division")), "")
    title = (title or "").rstrip(",;: ")
    if title.endswith(".") and not re.search(r"\b\w{1,3}\.$", title):
        title = title[:-1]
    return f"{title}, unnumbered page" if title else "unnumbered page"


START_ID = "start"
COVER_ALT = {"cover": "Cover of the book", "title page": "Title page of the book", "page of the text": "A page of the book"}


def book_page(book, names, has_cover=False, kind=None):
    src = book.get("source", {})
    ia = src.get("ia_identifier")
    slug = book["id"]
    rows = []

    def row(k, v):
        if v:
            rows.append(f'<tr><th scope="row">{esc(k)}</th><td>{v}</td></tr>')
    authors, editors = [], []
    for a in book.get("authors", []):
        dates = f' ({a.get("born", "?")}–{a.get("died", "?")})' if a.get("born") or a.get("died") else ""
        (editors if a.get("role") == "editor" else authors).append(esc(a["name"] + dates))
    row("Author" if len(authors) < 2 else "Authors", "; ".join(authors) or "Anonymous")
    row("Editor" if len(editors) < 2 else "Editors", "; ".join(editors))
    row("Title", f'<cite>{esc(book["title"])}</cite>' + (f': {esc(book["subtitle"])}' if book.get("subtitle") else ""))
    row("Published", esc(", ".join(x for x in (book.get("place"), book.get("publisher"), str(book.get("year", ""))) if x)))
    row("Edition transcribed", esc(book.get("edition_statement", "")))
    if book.get("volumes"):
        v = book["volumes"]
        vstr = f"{v} volumes, combined here into one" if isinstance(v, int) and v > 1 else (str(v) if not isinstance(v, int) else "")
        row("Original volumes", esc(vstr))
    row("Setting", esc(setting_text(book)))
    row("Time period", esc(str(book.get("period", ""))))
    row("Subjects", esc("; ".join(book.get("subjects", []))))
    scans = [(it["ia_identifier"], it.get("label", "")) for it in src.get("items", [])] if len(src.get("items", [])) > 1 else \
        ([(ia, "")] if ia else [])
    if scans:
        row("Scan" if len(scans) == 1 else "Scans",
            "; ".join((f"{esc(lab)}: " if lab else "") + f'<a href="https://archive.org/details/{attr(i)}">archive.org/details/{esc(i)}</a>'
                      for i, lab in scans)
            + (f', from {esc(src["contributor"])}' if src.get("contributor") else ""))
    row("This edition", f'version {book["version"]}, {esc(book["date"])}')
    summary = book.get("summary", "")
    summary = [summary] if isinstance(summary, str) else summary
    npages = sum(1 for p in book["pages"] if not p["blank"])
    first = names[rh.reading_divisions(book)[0]["id"]] if rh.reading_divisions(book) else None
    viewer = "".join(
        f'<details class="viewer"><summary>Look through the scanned pages{" of " + esc(lab) if lab else ""} here</summary>'
        f'<iframe src="https://archive.org/embed/{attr(i)}" title="Scanned pages of the book{" (" + esc(lab) + ")" if lab else ""} at the Internet Archive" loading="lazy" allowfullscreen=""></iframe></details>'
        for i, lab in scans)
    corr = book.get("corrections", [])
    pnum = {p["leaf"]: p["number"] for p in book["pages"]}
    corr_rows = "".join(
        f'<tr><td>{esc(correction_page(book, c, pnum))}</td><td>{esc(c["printed"])}</td><td>{esc(c["corrected"])}</td></tr>' for c in corr)
    notes = "".join(f"<li>{esc(n)}</li>" for n in book.get("notes_on_text", []))
    hist = "".join(f'<li>Version {h["version"]}, {esc(h["date"])}: {esc(h["note"])}</li>' for h in book.get("history", []))
    cover = f'<img class="cover" src="images/cover.jpg" alt="{COVER_ALT.get(kind, COVER_ALT["cover"])}"/>' if has_cover else ""
    added_split = (" A long text that the book does not divide is given here in sections, each on a page of its own; "
                   "the titles of the sections were added for this edition."
                   if any(u.get("added") and u.get("kind") != "part" for u in rh.reading_divisions(book)) else "")
    start = rh.body_start(book)
    if cover and start:
        href = f'{names[start["id"]]}#{START_ID}'
        cover = (f'<div class="cover-row"><a class="cover" href="{href}" title="Start reading">{cover}</a>'
                 f'<a class="cover-label" href="{href}">Click<br/>to read</a></div>')
    body = f"""<h1><cite>{esc(book.get("short_title") or book["title"])}</cite></h1>
<p class="byline">{esc(rh.authors_text(book))}, {book.get("year", "")}</p>
{cover}
{"".join(f"<p>{esc(s)}</p>" for s in summary)}
<h2 id="read">Read</h2>
<ul class="actions">
{f'<li><a href="{first}">Read on this site</a> (contents below)</li>' if first else ''}
<li><a href="{attr(download_url(book, ".epub"))}">EPUB</a> for e-readers</li>
<li><a href="{attr(download_url(book, ".odt"))}">ODT</a> for word processors</li>
<li><a href="{slug}.json">JSON</a>: the complete transcription, including the parts left out of the other versions
(<a href="../../json-format.html">format</a>)</li>
{"".join(f'<li><a href="https://archive.org/details/{attr(i)}">The scan{" of " + esc(lab) if lab else ""} at the Internet Archive</a></li>' for i, lab in scans)}
</ul>
{viewer}
<h2 id="contents">Contents</h2>
<nav class="toc" aria-label="Contents of the book">{rh.nav_list(book, names)}</nav>
<h2 id="about-book">The book</h2>
<div class="tablewrap"><table class="bib">{"".join(rows)}</table></div>
<h2 id="text">The text</h2>
<p>Transcribed from the scan ({npages} pages with text or pictures) with the spelling, punctuation, and wording of the original;
spaces around punctuation follow modern practice. {esc(book.get("omitted_from_reading", ""))}{added_split}</p>
{f'<ul>{notes}</ul>' if notes else ''}
{f'<h3>Printer’s errors corrected</h3><div class="tablewrap"><table class="doc"><thead><tr><th scope="col">Page</th><th scope="col">Printed</th><th scope="col">Corrected to</th></tr></thead><tbody>{corr_rows}</tbody></table></div>' if corr else '<p>No corrections were made to the printed text.</p>'}
{f'<h3>Versions</h3><ul>{hist}</ul>' if hist else ''}
"""
    return page(book.get("short_title") or book["title"], body, "../../")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(REPO, "_site"))
    ap.add_argument("--bookdir", action="append", default=[], help="also build this book directory (e.g. wip/<slug>)")
    ap.add_argument("--only", help="build only the book with this id (plus the site pages)")
    a = ap.parse_args()
    out = a.out
    os.makedirs(os.path.join(out, "assets"), exist_ok=True)
    for f in sorted(os.listdir(os.path.join(REPO, "site", "assets"))):
        shutil.copyfile(os.path.join(REPO, "site", "assets", f), os.path.join(out, "assets", f))
    open(os.path.join(out, ".nojekyll"), "w").close()
    dirs = [os.path.join(REPO, "books", d) for d in sorted(os.listdir(os.path.join(REPO, "books")))
            if os.path.exists(os.path.join(REPO, "books", d, "book.json"))] if os.path.isdir(os.path.join(REPO, "books")) else []
    dirs += a.bookdir
    books, nwarn = [], 0
    for d in dirs:
        if a.only and os.path.basename(os.path.normpath(d)) != a.only:
            continue
        book, warnings = build_book(out, d)
        books.append(book)
        nwarn += len(warnings)
        print(f"built {book['id']} v{book['version']}: {len(rh.reading_divisions(book))} reading divisions, {len(warnings)} compile warnings")
    qf = os.path.join(REPO, "data", "queue.json")
    queue = json.load(open(qf, encoding="utf-8"))["books"] if os.path.exists(qf) else []
    record, cdir, have = load_carousel(), os.path.join(REPO, "site", CAROUSEL_DIR), set()
    shown = {b["id"] for b in books} & set(record)
    for f in sorted(os.listdir(cdir)) if os.path.isdir(cdir) else []:
        if f.endswith(".jpg") and f[:-4] in shown:
            os.makedirs(os.path.join(out, CAROUSEL_DIR), exist_ok=True)
            shutil.copyfile(os.path.join(cdir, f), os.path.join(out, CAROUSEL_DIR, f))
            have.add(f)
    build_index(out, carousel_html(books, record, have), len(books))
    build_books(out, books, queue, load_published_times())
    build_lists(out, books)
    md_page(out, "about.html", "About", os.path.join(REPO, "site", "about.md"))
    md_page(out, "json-format.html", "The JSON format", os.path.join(REPO, "site", "json-format.md"))
    print(f"site written to {out}: {len(books)} books")


if __name__ == "__main__":
    main()
