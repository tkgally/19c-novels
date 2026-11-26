# Errata

Errors reported by Tom or readers (via GitHub Issues or direct messages) and errors found in post-publication sweeps.

## Procedure

1. Record the report below with date, source (issue number or Tom), novel slug, page/passage, and status (`open`).
2. Fetch the page image from the Drive cache (`tools/drive_cache.py fetch books/<slug>/source.json /tmp/errata --pages pNNNN`) and inspect the scan.
3. Edit `books/<slug>/pages/pNNNN.txt`, increment `version` in `book.json`, update `date`, add a `history` entry, update `audit.version` (or re-audit if substantive), run `tools/preflight.py books/<slug>` (`PASS`) and `tools/publish.py <slug>`, commit, push, merge to `main`, verify the release/site update, and mark `closed` below (closing any GitHub issue with a plain factual reply).

## Log

*(None yet.)*
