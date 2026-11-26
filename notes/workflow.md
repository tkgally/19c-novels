# Workflow (current method)

`$R` = `/home/antigravity/tkgally/19c-novels`, `$S` = `/tmp/novels`, `$W` = `$R/wip/<slug>`, `$B` = `$S/<slug>`.

## Pipeline stages and roles

| Stage | Who | Why |
|---|---|---|
| Draft, every leaf | Gemini Pro subagents (`Model: "pro"`), `prompts/transcribe.md` | strongest visual reading of pre-1914 typography |
| Second pass, every leaf | Gemini Flash subagents (`Model: "flash"`), `prompts/verify.md` (JSONL corrections list) | differently-biased second model reading; catches dropped lines, wrong words, and tag errors |
| Judge, every spot where Pro and Flash differ in words or punctuation | Fresh Gemini Pro subagent (`Model: "pro"`), readings shuffled blindly as A/B (`tools/judge.py`) | settles disagreements without reading every leaf in the main session |
| Scan check of uncertain judge spots and preflight observe lists | Main session or `pro` subagent on crops (`tools/crop_spot.py`) | judges err ~1 time in 6–30; catches unmarked printed misprints and rare spellings |
| Blind sampled audit, 6 random pages with 5 planted errors each | Fresh Gemini Pro subagent (`Model: "pro"`) on `audit/blind/` (`tools/audit_sample.py`) | measures both the book’s residual error rate and the proofreader’s recall |

Never publish a single-model text; never let the same model act as both writer and sole checker.

## 0. Environment

```bash
$R/tools/setup_env.sh
export EPUBCHECK_JAR=/home/antigravity/.local/share/epubcheck/epubcheck-5.1.0/epubcheck.jar
$R/tools/run_tests.sh        # must say OK
```

## 1. Start a novel

1. Pick from `data/queue.json` (`python3 $R/tools/ledger.py`) and re-check eligibility (`notes/selection.md` §“Before starting”). Set the row to `"in progress"` with `"started": "YYYY-MM-DD"`.
2. Create `$W`, write initial `$W/book.json` (`version`: 1), `$W/log.md`, and `$W/source.json`.
3. Fetch from IA once into `$B/src` (or `$B/src-v1`, `$B/src-v2`, `$B/src-v3` for multi-volume novels) and prepare working greyscale page images:
   ```bash
   python3 $R/tools/ia.py fetch <id_v1> $B/src-v1
   python3 $R/tools/prep_pages.py $B/src-v1 $B/pages                 # p0000.jpg …
   # For multi-volume novels:
   python3 $R/tools/ia.py fetch <id_v2> $B/src-v2
   python3 $R/tools/prep_pages.py $B/src-v2 $B/pages --offset 1000   # p1000.jpg …
   python3 $R/tools/contact_sheets.py $B/pages $B/sheets
   ```
4. **Completeness and quality check — before spending subagent runs.** Inspect ALL contact sheets (`$B/sheets/sheet-*.jpg`) and at least a dozen full-size leaves across the novel. Verify printed page numbers run continuously with no missing, duplicated, clipped, or obscured leaves. Write the complete leaf/page map in `$W/log.md`.
5. **Cache in Google Drive (“19C Novels”, `1ecaIjeQldRJ8cfAD1-mGtNbofezQLbcy`):**
   ```bash
   python3 $R/tools/drive_cache.py pack $B/pages $B/parts --source $W/source.json
   python3 $R/tools/drive_cache.py upload $W/source.json $B/parts --slug <slug>
   ```
   Later sessions restore working leaves via `python3 $R/tools/drive_cache.py fetch $W/source.json $B/pages`.
6. Extract `--full` colour leaves for `images/cover.jpg` (cover if title is clearly readable, otherwise Volume I’s title page) and any illustrations or ornaments (`tools/crop_image.py`, longest side ≤ 1000 px, JPEG quality 75). Visually verify every crop with `view_file`.
7. Commit and push `$W`.

## 2. Draft (`Model: "pro"`)

```bash
python3 $R/tools/ocr_batch.py prepare-draft --images $B/pages --prompt $R/prompts/transcribe.md --out $W/draft --pages <range> --batch-size 25
# Invoke parallel Gemini Pro subagents (Model: "pro") on each $W/draft/batches/batch-NN.md
# If any page hits a recitation filter:
python3 $R/tools/ocr_fallback.py prepare --images $B/pages --draft $W/draft
# (run Gemini Pro subagent on $W/draft/_fallback/task.md, then:)
python3 $R/tools/ocr_fallback.py apply --draft $W/draft
python3 $R/tools/ocr_batch.py check-draft --images $B/pages --out $W/draft --pages <range>
python3 $R/tools/normalize.py $W/draft
```
Commit and push after the draft is normalized.

## 3. Second pass (`Model: "flash"`), review, and blind judge (`Model: "pro"`)

```bash
python3 $R/tools/ocr_batch.py prepare-verify --images $B/pages --draft $W/draft --prompt $R/prompts/verify.md --out $W/verify --batch-size 25
# Invoke parallel Gemini Flash subagents (Model: "flash") on each $W/verify/batches/batch-NN.md
python3 $R/tools/ocr_batch.py apply-verify --draft $W/draft --out $W/verify
python3 $R/tools/normalize.py $W/verify
python3 $R/tools/review.py $W/draft $W/verify --out $W/spots.json
python3 $R/tools/judge.py --spots $W/spots.json --verified $W/verify --images $B/pages --out $W/judge --prepare
# Invoke a fresh Gemini Pro subagent (Model: "pro") on $W/judge/tasks/INSTRUCTIONS.md
python3 $R/tools/judge.py --spots $W/spots.json --verified $W/verify --images $B/pages --out $W/judge --apply
python3 $R/tools/normalize.py $W/judge
mkdir -p $W/pages && cp $W/judge/p*.txt $W/pages/
```
Inspect every unapplied correction, length outlier, `[[cont]]` change, and `judge/report.txt` item against scan crops (`tools/crop_spot.py`), editing `$W/pages/` where needed.

## 4. Structure, spot-reads, and preflight

1. Configure `divisions` (and `parts` / `source.items` for multi-volume novels) in `$W/book.json` (`notes/book-json.md`).
2. Run `python3 $R/tools/preflight.py $W` and inspect its `observe` lists (`misprints`, `rare-forms`, `missing-stop`, `accents`, `italic-brackets`, `openings`, `joins`, `hyphen-joins`, `folios`, `contents`) on scan crops, marking unmistakable printer’s errors `[[corr printed|corrected]]` and fixing any real transcription errors.
3. Spot-read front matter (especially Volume I’s title page), footnote pages, verse, letters, and foreign passages against the scan.

## 5. Blind sampled audit and publication

```bash
python3 $R/tools/audit_sample.py --pages-dir $W/pages --images $B/pages --out $W/audit --rules $R/prompts/transcribe.md --prepare
# Invoke a fresh Gemini Pro subagent (Model: "pro") strictly on $W/audit/blind/INSTRUCTIONS.md
python3 $R/tools/audit_sample.py --pages-dir $W/pages --images $B/pages --out $W/audit --rules $R/prompts/transcribe.md --score
```
Inspect every candidate in `$W/audit/candidates.tsv` on a scan crop (`tools/crop_spot.py`), fix any confirmed transcription error in `$W/pages/`, record `"audit"` in `$W/book.json`, re-run `python3 $R/tools/preflight.py $W` (must end `PASS`), inspect the built HTML pages, then publish:
```bash
python3 $R/tools/publish.py <slug>
python3 $R/tools/carousel.py add <slug> --kind cover|title|page
```
Update `books/<slug>/log.md`, `notes/metrics.md`, `notes/lessons.md` (if anything new was learned), and `notes/sessions.md`; run `$R/tools/run_tests.sh` and `python3 $R/tools/ledger.py check`; commit, push, merge to `main`, and verify the GitHub Actions deploy and GitHub Release downloads.

## When a check is wrong

1. Confirm from the scan that the page files are right and the check is raising a false alarm.
2. Single item → add a `waivers` entry in `book.json` (`check`, `match`, `why`), note it in `metrics.md`, and publish.
3. Systematic false alarm for a class of novels → finish the novel’s audit and leave it `in progress` (`ready to publish when check X is fixed`), then write a regression test with invented text first, fix the check, verify `tools/run_tests.sh` and `preflight.py` on all `books/`, and commit the check + test on their own. **The next session publishes the novel.**
