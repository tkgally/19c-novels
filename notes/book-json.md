# book.json, source.json, log.md

## book.json (in `wip/<slug>/` then `books/<slug>/`)

```json
{
 "id": "by-the-cornish-sea-isabell",
 "version": 1,
 "date": "2026-11-26",
 "title": "By the Cornish Sea",
 "subtitle": "",
 "short_title": "By the Cornish Sea",
 "authors": [{"name": "John Isabell", "sort": "Isabell, John", "born": 1856, "died": 1932}],
 "place": "London",
 "publisher": "Sampson Low, Marston, Searle, & Rivington",
 "year": 1885,
 "volumes": 2,
 "edition_statement": "First edition, in two volumes",
 "setting": "Cornwall",
 "period": "1880s",
 "subjects": ["Cornish coast", "fishing villages", "courtship"],
 "summary": "60–150 plain, factual words using serial commas and curly quotes…",
 "source": {
  "ia_identifier": "bycornishsea01isab",
  "contributor": "University of Illinois Urbana-Champaign",
  "hidden_leaves": [0],
  "items": [
   {"ia_identifier": "bycornishsea01isab", "first_leaf": "p0000", "hidden_leaves": [0], "label": "Volume I"},
   {"ia_identifier": "bycornishsea02isab", "first_leaf": "p1000", "hidden_leaves": [0], "label": "Volume II"}
  ]
 },
 "omitted_from_reading": "The half-titles, the title page of Volume II, the printed tables of contents, and the publisher’s advertisements are in the JSON only.",
 "notes_on_text": [],
 "history": [{"version": 1, "date": "2026-11-26", "note": "First publication."}],
 "audit": {"version": 1, "date": "2026-11-26", "pages": 6, "recall": "30/30", "real_errors": 0, "fixed": 0},
 "divisions": [
  {"at": "p0005", "kind": "titlepage"},
  {"at": "p0007", "kind": "contents"},
  {"at": "p1000", "kind": "front", "reading": false, "title": "Front matter (Volume II)"}
 ],
 "parts": [
  {"before": "p0009", "title": "Volume I"},
  {"before": "p1009", "title": "Volume II"}
 ]
}
```

Key notes:
- Required fields checked by `preflight.py`: `id`, `version`, `date`, `title`, `authors`, `place`, `publisher`, `year` (`1700 <= year <= 1913`), `setting`, `period`, `summary` (30–220 words), `source`, `history`, and `audit`.
- For anonymous novels, use `[{"name": "Anonymous", "sort": "Anonymous"}]` in `authors`.
- Single-volume novels need only `source.ia_identifier` and `source.hidden_leaves` (no `volumes` > 1, `source.items`, or `parts` unless divided into Parts in print).
- Optional keys: `subtitle`, `volumes`, `edition_statement`, `subjects`, `notes_on_text`, `omitted_from_reading`, `toc`, `toc_entries`, `frontispiece`, `ornaments`, `keep_hyphens`, `leaf_order`, `waivers`, `editor_images`, `body_start`, `css_extra`.

## source.json

Written and updated by `tools/drive_cache.py`:
`{"ia_identifier": "…", "drive_folder_id": "…", "parts": [{"name", "sha256", "bytes", "files", "drive_id"}]}`.

## log.md template

```markdown
# <Title> — <Author> (<year>)

IA: <identifier(s)> (<contributor>; <n> leaves).
Eligibility: re-checked <date>: …

## Status
Stage reached: … | Next step: …

## Page map
p0000 colour card · p0005 title · …
Scan check: all contact sheets and full-size sample checked <date>; problems: none / …

## Decisions
- …

## Runs
| Stage | Date | Model | Pages | Notes |
|---|---|---|---|---|

## Versions
| Version | Date | Preflight stamp | Audit | Notes |
|---|---|---|---|---|
```
