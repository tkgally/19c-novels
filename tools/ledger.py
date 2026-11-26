#!/usr/bin/env python3
"""The ledger of novels (data/queue.json) and the 2021 blog seed list (data/blog_2021.json): a short report and a consistency check.

  ledger.py            what is published, in progress, waiting, and queued
  ledger.py check      problems only (exit 1 if any); also run by the tests on the real data

Standard library only.
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
STATUSES = ("queued", "in progress", "published", "waiting", "rejected")
NEED = ("slug", "title", "author", "year", "status", "eligibility")
MIN_QUEUED = 6


def load(repo=REPO):
    q = json.load(open(os.path.join(repo, "data", "queue.json"), encoding="utf-8"))
    bf = os.path.join(repo, "data", "blog_2021.json")
    b = json.load(open(bf, encoding="utf-8")) if os.path.exists(bf) else {"books": []}
    return q, b


def check(q, b=None, repo=REPO):
    """A list of problems in data/queue.json and between it and books/, wip/, data/published.json."""
    b = b or {"books": []}
    out, seen, seen_blog = [], set(), set()
    blog_nums = {x["n"] for x in b.get("books", [])}
    if len(blog_nums) != len(b.get("books", [])):
        out.append("blog_2021.json: two entries share a number")
    for r in q.get("books", []):
        name = r.get("slug") or r.get("title") or "?"
        for k in NEED:
            if r.get(k) in (None, ""):
                out.append(f"{name}: no `{k}`")
        if r.get("status") not in STATUSES:
            out.append(f"{name}: status {r.get('status')!r} is not one of {', '.join(STATUSES)}")
        if r.get("slug") in seen:
            out.append(f"{name}: slug used twice")
        seen.add(r.get("slug"))
        if not (r.get("ia") or r.get("ia_items") or r.get("status") == "rejected"):
            out.append(f"{name}: no `ia` or `ia_items` identifier")
        if "blog_2021" in r:
            n = r["blog_2021"]
            if blog_nums and n not in blog_nums:
                out.append(f"{name}: `blog_2021` ({n!r}) is not a number in data/blog_2021.json")
            if n in seen_blog:
                out.append(f"{name}: blog_2021 number {n} is on two rows")
            seen_blog.add(n)
        if r.get("from") not in (None, "blog_2021", "tom"):
            out.append(f"{name}: `from` is {r.get('from')!r}; known values: blog_2021, tom")
        where = {"published": "books", "in progress": "wip", "waiting": "wip"}.get(r.get("status"))
        cfg = None
        for d in ("books", "wip"):
            f = os.path.join(repo, d, r.get("slug") or "?", "book.json")
            if os.path.exists(f):
                cfg = json.load(open(f, encoding="utf-8"))
                if d != where:
                    out.append(f"{name}: is in {d}/ but its status is {r.get('status')!r}")
        if r.get("status") == "published" and cfg is None:
            out.append(f"{name}: published but books/{r.get('slug')}/book.json is missing")
    pf = os.path.join(repo, "data", "published.json")
    times = json.load(open(pf, encoding="utf-8")) if os.path.exists(pf) else {}
    for r in q.get("books", []):
        if r.get("status") == "published" and r.get("slug") not in times:
            out.append(f"{r.get('slug')}: published but has no time in data/published.json (publish.py writes it)")
    for d in ("books", "wip"):
        dd = os.path.join(repo, d)
        for slug in sorted(os.listdir(dd)) if os.path.isdir(dd) else []:
            if os.path.exists(os.path.join(dd, slug, "book.json")) and slug not in seen:
                out.append(f"{d}/{slug}: no row in data/queue.json")
    return out


def report(q, b=None, repo=REPO):
    rows = q.get("books", [])
    by = {s: [r for r in rows if r.get("status") == s] for s in STATUSES}
    lines = []

    def show(title, rs, extra=lambda r: ""):
        lines.append(f"{title} ({len(rs)})")
        for r in rs:
            tag = " [blog]" if r.get("from") == "blog_2021" else (" [Tom]" if r.get("from") == "tom" else "")
            vols = f", {r['volumes']}v" if r.get("volumes", 1) and int(r.get("volumes", 1)) > 1 else ""
            lines.append(f"  {r.get('slug')}{tag} — {r.get('author')} ({r.get('year')}{vols}){extra(r)}")

    show("Published", by["published"], lambda r: f"  v{r.get('version', '?')} {r.get('published', '')}")
    show("In progress", by["in progress"])
    show("Waiting", by["waiting"], lambda r: f"  — {r.get('waiting_for', '')}"[:120])
    show("Queued", by["queued"], lambda r: f"  {r.get('images', '?')} leaves")
    lines.append(f"Rejected rows: {len(by['rejected'])}; rejected before queuing (queue.json `rejected`): {len(q.get('rejected', []))}")
    if len(by["queued"]) < MIN_QUEUED:
        lines.append(f"\nFewer than {MIN_QUEUED} novels queued: find and vet more (skill select-novel)")
    npub = len(by["published"])
    if npub and npub % 5 == 0:
        lines.append(f"{npub} novels published: a review session is due if the last review covered fewer (notes/improvement.md)")
    return "\n".join(lines)


def main():
    q, b = load()
    problems = check(q, b)
    if sys.argv[1:] == ["check"]:
        print("\n".join(problems) or "ledger: no problems")
        sys.exit(1 if problems else 0)
    print(report(q, b))
    if problems:
        print("\nPROBLEMS\n" + "\n".join("  " + p for p in problems))


if __name__ == "__main__":
    main()
