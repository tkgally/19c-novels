"""Regression tests for the 19c-novels (Forgotten Novels) tools. Fast, deterministic, no model calls, no network.

Run: tools/run_tests.sh
Rules (GEMINI.md): run at the start of every working session and after any edit under tools/;
every tool bug fixed gets a test here in the same commit; never loosen a test to get a novel published.
"""
import copy, io, json, os, re, shutil, subprocess, sys, tempfile, unittest, zipfile
from PIL import Image

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO, "tools"))
import audit_sample, build_site, carousel, compile_book, corrections, crop_image, drive_cache, inline, judge, ledger, normalize, ocr_batch, ocr_fallback, preflight, prep_pages, publish, refusal, releases, render_epub, render_html as rh, render_odt, review, running_quotes, session_meter  # noqa: E402

SAMPLE = os.path.join(REPO, "tests", "sample")
CFG = {
    "id": "t", "version": 1, "date": "2026-01-01", "title": "T",
    "authors": [{"name": "A", "sort": "A"}],
    "place": "London", "publisher": "P", "year": 1850,
    "setting": "England", "period": "1840s",
    "summary": " ".join(["word"] * 45),
    "source": {"ia_identifier": "test00auth"},
    "history": [{"version": 1, "date": "2026-01-01", "note": "First publication."}],
    "audit": {"version": 1, "date": "2026-01-01", "pages": 6, "recall": "30/30", "real_errors": 0, "fixed": 0},
}


def comp(pages, **cfg):
    c = dict(CFG, **cfg)
    return compile_book.compile_pages(c, [(f"p{i:04d}", t) for i, t in enumerate(pages, 1)])


def texts(book):
    return [s for d in book["divisions"] for b in d["blocks"] for s in rh.strings(b)]


class QuotesAndInline(unittest.TestCase):
    def test_curly_quotes(self):
        self.assertEqual(inline.smart_quotes('"Yes," he said, \'tis so; don\'t.'), "“Yes,” he said, ’tis so; don’t.")
        self.assertEqual(inline.smart_quotes("called 'a little damp.'"), "called ‘a little damp.’")
        self.assertEqual(inline.smart_quotes("<i>Paul</i>'s"), "<i>Paul</i>’s")

    def test_convert_and_plain(self):
        w = []
        s = inline.convert('A & B <i>c</i> [[corr teh|the]] p. <pref>34</pref>[[fnref *]]', w.append)
        self.assertEqual(s, 'A &amp; B <i>c</i> <corr orig="teh">the</corr> p. <pageref n="34">34</pageref><noteref mark="*"/>')
        self.assertEqual(w, [])
        self.assertEqual(inline.plain(s), "A & B c the p. 34")
        self.assertEqual(inline.plain(s, corrected=False), "A & B c teh p. 34")


class NormalizeAndCorrections(unittest.TestCase):
    def test_modern_spacing_and_contractions(self):
        raw = "[[page 1]]\n\n“ What ! ” cried he ; “ do n't say so : it cannot be ! ”\n"
        norm = normalize.norm_page(raw)
        self.assertIn("“What!” cried he; “don't say so: it cannot be!”", norm)
        fb = ocr_fallback.raw_to_markup("First para-\ngraph.\n\nSecond line.")
        self.assertIn("First paragraph.", fb)

    def test_corrections_apply(self):
        draft = "[[page 1]]\n\nHe shewed the neophyte into the parlour.\n"
        reply = '{"find": "neophyte into", "replace": "neophite into"}\n'
        out, n, sk = corrections.apply(draft, reply)
        self.assertEqual(n, 1)
        self.assertEqual(sk, [])
        self.assertIn("neophite into", out)


class CompileAndMultiVolume(unittest.TestCase):
    def test_format_identifier(self):
        book, w = comp(["[[page 1]]\n# Chapter I.\n\nIt was an autumn evening."])
        self.assertEqual(book["format"], "forgotten-novels-json/1")
        self.assertEqual(w, [])

    def test_join_and_hyphen(self):
        book, w = comp(["[[page 1]]\n# Chapter I.\n\nThe road was with-", "[[page 2]]\n[[cont]]out end, and long", "[[page 3]]\n[[cont]]as well."])
        t = texts(book)
        self.assertEqual(t[1], 'The road was with<pb n="2" leaf="p0002"/>out end, and long <pb n="3" leaf="p0003"/>as well.')
        self.assertEqual(len([x for x in w if x.startswith("hyphen join")]), 1)

    def test_multivolume_three_decker_parts_and_titlepages(self):
        """Tom (2026-11-26): multi-volume novels open with Vol. I's title page, group each volume under Volume I / II…
        as Parts keeping each volume's own chapter numbering, and keep later volumes' title pages in the JSON only."""
        pages = [
            ("p0001", "[[page ?]]\n\n[[center]] A FORGOTTEN NOVEL.\n\n[[center]] VOL. I.\n\n[[center]] LONDON: 1865."),
            ("p0002", "[[page 1]]\n# Chapter I.\n\nVolume one begins here."),
            ("p0003", "[[page 2]]\n# Chapter II.\n\nVolume one continues."),
            ("p1001", "[[page ?]]\n\n[[center]] A FORGOTTEN NOVEL.\n\n[[center]] VOL. II.\n\n[[center]] LONDON: 1865."),
            ("p1002", "[[page 1]]\n# Chapter I.\n\nVolume two restarts at chapter one."),
        ]
        cfg = dict(
            CFG,
            volumes=2,
            source={
                "ia_identifier": "novel01auth",
                "items": [
                    {"ia_identifier": "novel01auth", "first_leaf": "p0000", "hidden_leaves": [], "label": "Volume I"},
                    {"ia_identifier": "novel02auth", "first_leaf": "p1000", "hidden_leaves": [], "label": "Volume II"},
                ],
            },
            divisions=[
                {"at": "p0001", "kind": "titlepage"},
                {"at": "p1001", "kind": "front", "reading": False, "title": "Title Page (Volume II)"},
            ],
            parts=[
                {"before": "p0002", "title": "Volume I"},
                {"before": "p1002", "title": "Volume II"},
            ],
        )
        book, w = compile_book.compile_pages(cfg, pages)
        self.assertEqual(w, [])
        # JSON keeps Vol. II's title page, while reading divisions omit it
        all_kinds = [(d["kind"], d["title"], d["reading"]) for d in book["divisions"]]
        self.assertIn(("front", "Title Page (Volume II)", False), all_kinds)
        rd = rh.reading_divisions(book)
        self.assertEqual([d["title"] for d in rd], ["Title Page", "Volume I", "Chapter I", "Chapter II", "Volume II", "Chapter I"])
        # TOC nests each volume's chapters under its Volume Part
        tree = rh.toc_tree(book)
        self.assertEqual(tree[0][0], "Title Page")
        self.assertEqual(tree[1][0], "Volume I")
        self.assertEqual([c[0] for c in tree[1][3]], ["Chapter I", "Chapter II"])
        self.assertEqual(tree[2][0], "Volume II")
        self.assertEqual([c[0] for c in tree[2][3]], ["Chapter I"])
        # EPUB and ODT render cleanly with multi-volume scan links and added part bookmarks
        epub_bytes = render_epub.render(book, None)
        odt_bytes = render_odt.render(book, None)
        with zipfile.ZipFile(io.BytesIO(epub_bytes)) as zf:
            title_xhtml = zf.read("OEBPS/text/title.xhtml").decode("utf-8")
            self.assertIn("novel01auth", title_xhtml)
            self.assertIn("novel02auth", title_xhtml)
            self.assertIn("Forgotten Novels edition", title_xhtml)
        with zipfile.ZipFile(io.BytesIO(odt_bytes)) as zf:
            content_xml = zf.read("content.xml").decode("utf-8")
            self.assertIn('text:name="div-d002"', content_xml)
            self.assertIn('text:name="div-d006"', content_xml)


class SampleBookAndPreflight(unittest.TestCase):
    def test_sample_builds_and_passes_preflight_without_external_jars(self):
        verdict, report, res = preflight.run(SAMPLE, skip_epubcheck=True, skip_odt=True)
        self.assertEqual(verdict, "INCOMPLETE", report)
        for k, (mode, _) in preflight.CHECKS.items():
            if mode == "enforce" and k not in ("epubcheck", "odt"):
                self.assertEqual(res[k], [], f"{k} failed: {res[k]}")

    def test_sample_passes_full_preflight_when_epubcheck_and_soffice_present(self):
        jar = os.environ.get("EPUBCHECK_JAR") or "/home/antigravity/.local/share/epubcheck/epubcheck-5.1.0/epubcheck.jar"
        if not (os.path.exists(jar) and shutil.which("soffice")):
            self.skipTest("epubcheck or soffice not installed in this environment")
        verdict, report, _ = preflight.run(SAMPLE, epubcheck=jar)
        self.assertEqual(verdict, "PASS", report)

    def test_italic_brackets_observe_check(self):
        items = preflight.check_italic_brackets([
            ("p0001", "[[page 1]]\n\nHe spoke (<i>aside</i>) and then <i>(loudly)</i> left."),
        ])
        self.assertEqual(len(items), 1)
        self.assertIn("<i>(loudly)</i>", items[0])

    def test_year_range_check(self):
        bad_late = dict(CFG, id="sample", year=1915)
        self.assertTrue(any("1700–1913" in x for x in preflight.check_meta(bad_late, SAMPLE)))
        bad_early = dict(CFG, id="sample", year=1688)
        self.assertTrue(any("1700–1913" in x for x in preflight.check_meta(bad_early, SAMPLE)))
        good_18c = dict(CFG, id="sample", year=1749)
        self.assertEqual(preflight.check_meta(good_18c, SAMPLE), [])


class SiteAndReleases(unittest.TestCase):
    def test_site_build_and_lists(self):
        with tempfile.TemporaryDirectory() as tmp:
            subprocess.run([sys.executable, os.path.join(REPO, "tools", "build_site.py"), "--out", tmp, "--bookdir", SAMPLE],
                           check=True, capture_output=True, text=True)
            idx = open(os.path.join(tmp, "index.html"), encoding="utf-8").read()
            self.assertIn("Forgotten Novels", idx)
            self.assertNotIn("Travel Books", idx)
            self.assertNotIn("japan-as-they-saw-it", idx)
            books_html = open(os.path.join(tmp, "books.html"), encoding="utf-8").read()
            self.assertIn("Wiltshire · 1850s", books_html)
            self.assertIn('href="dates.html"', books_html)
            dates_html = open(os.path.join(tmp, "dates.html"), encoding="utf-8").read()
            self.assertIn("1860s", dates_html)
            bpage = open(os.path.join(tmp, "books", "sample", "index.html"), encoding="utf-8").read()
            self.assertIn("https://github.com/tkgally/19c-novels/releases/download/book-sample/sample-v1.epub", bpage)
            self.assertIn("Click<br/>to read", bpage)
            # Releases removal leaves site without .epub/.odt binaries
            removed = releases.remove(tmp)
            self.assertEqual(removed, 2)
            self.assertFalse(os.path.exists(os.path.join(tmp, "books", "sample", "sample.epub")))


class SubagentPipelineTools(unittest.TestCase):
    def test_ocr_batch_review_judge_and_audit_roundtrip(self):
        with tempfile.TemporaryDirectory() as tmp:
            img_dir = os.path.join(tmp, "images")
            os.makedirs(img_dir)
            Image.new("L", (400, 600), 240).save(os.path.join(img_dir, "p0001.jpg"))
            draft_dir = os.path.join(tmp, "draft")
            verify_dir = os.path.join(tmp, "verify")
            judge_dir = os.path.join(tmp, "judge")
            audit_dir = os.path.join(tmp, "audit")

            subprocess.run([sys.executable, os.path.join(REPO, "tools", "ocr_batch.py"), "prepare-draft",
                            "--images", img_dir, "--prompt", os.path.join(REPO, "prompts", "transcribe.md"), "--out", draft_dir],
                           check=True, capture_output=True)
            self.assertTrue(os.path.exists(os.path.join(draft_dir, "batches", "batch-01.md")))

            long_para = (
                "[[page 1]]\n\n# Chapter I.\n\n"
                "It was on a grey morning to-day when Arthur shewed his connexion with the old squire, and walked "
                "quietly through the village street towards the grey church tower where these bells had rung for ever "
                "so many winters, and every one in the parish knew that those fields belonged to the manor house, "
                "though neither steward nor tenant spoke of the matter; for the family had kept their counsel through "
                "good fortune and bad, and the neighbours respected their silence in all seasons of the year, waiting "
                "until the young heir himself should return from London to claim his own inheritance at last.\n"
            )
            open(os.path.join(draft_dir, "p0001.txt"), "w", encoding="utf-8").write(long_para)
            subprocess.run([sys.executable, os.path.join(REPO, "tools", "ocr_batch.py"), "check-draft",
                            "--images", img_dir, "--out", draft_dir], check=True, capture_output=True)

            subprocess.run([sys.executable, os.path.join(REPO, "tools", "ocr_batch.py"), "prepare-verify",
                            "--images", img_dir, "--draft", draft_dir, "--prompt", os.path.join(REPO, "prompts", "verify.md"), "--out", verify_dir],
                           check=True, capture_output=True)
            open(os.path.join(verify_dir, "p0001.corr"), "w", encoding="utf-8").write(
                '{"find": "quietly through", "replace": "slowly through"}\n'
            )
            subprocess.run([sys.executable, os.path.join(REPO, "tools", "ocr_batch.py"), "apply-verify",
                            "--draft", draft_dir, "--out", verify_dir], check=True, capture_output=True)

            spots_p = os.path.join(tmp, "spots.json")
            subprocess.run([sys.executable, os.path.join(REPO, "tools", "review.py"), draft_dir, verify_dir, "--out", spots_p],
                           check=True, capture_output=True)
            spots = json.load(open(spots_p, encoding="utf-8"))
            self.assertEqual(len(spots["p0001"]), 1)

            # Blind judge prepare + apply
            subprocess.run([sys.executable, os.path.join(REPO, "tools", "judge.py"),
                            "--spots", spots_p, "--verified", verify_dir, "--images", img_dir, "--out", judge_dir, "--prepare"],
                           check=True, capture_output=True)
            self.assertTrue(os.path.exists(os.path.join(judge_dir, "tasks", "p0001.md")))
            self.assertIn("NEVER call `run_command`", open(os.path.join(judge_dir, "tasks", "INSTRUCTIONS.md"), encoding="utf-8").read())
            pick_draft = "A" if judge.labels("p0001", 1) else "B"
            open(os.path.join(judge_dir, "raw", "p0001.txt"), "w", encoding="utf-8").write(
                json.dumps({"n": 1, "is": pick_draft, "print": "quietly through", "sure": "high"}) + "\n"
            )
            subprocess.run([sys.executable, os.path.join(REPO, "tools", "judge.py"),
                            "--spots", spots_p, "--verified", verify_dir, "--images", img_dir, "--out", judge_dir, "--apply"],
                           check=True, capture_output=True)
            self.assertIn("quietly through", open(os.path.join(judge_dir, "p0001.txt"), encoding="utf-8").read())

            # Blind audit prepare + score (seeds stored under _secret/, tasks under blind/)
            subprocess.run([sys.executable, os.path.join(REPO, "tools", "audit_sample.py"),
                            "--pages-dir", judge_dir, "--images", img_dir, "--out", audit_dir,
                            "--rules", os.path.join(REPO, "prompts", "transcribe.md"), "--min-chars", "200", "--prepare"],
                           check=True, capture_output=True)
            self.assertTrue(os.path.exists(os.path.join(audit_dir, "_secret", "seeds.json")))
            self.assertFalse(os.path.exists(os.path.join(audit_dir, "blind", "seeds.json")))
            seeds = json.load(open(os.path.join(audit_dir, "_secret", "seeds.json"), encoding="utf-8"))["p0001"]
            self.assertGreaterEqual(len(seeds), 3)
            given = open(os.path.join(audit_dir, "blind", "p0001.given.txt"), encoding="utf-8").read()
            findings = []
            for s in seeds:
                lo = max(0, s["at"] - 10)
                hi = min(len(given), s["at"] + len(s["now"]) + 10)
                # Snap to whole words around the planted error
                words_around = given[lo:hi].strip()
                findings.append(json.dumps({"given": words_around, "print": s["was"], "sure": "high"}))
            open(os.path.join(audit_dir, "whole", "p0001.txt"), "w", encoding="utf-8").write("\n".join(findings) + "\n")
            res = subprocess.run([sys.executable, os.path.join(REPO, "tools", "audit_sample.py"),
                                  "--pages-dir", judge_dir, "--images", img_dir, "--out", audit_dir,
                                  "--rules", os.path.join(REPO, "prompts", "transcribe.md"), "--min-chars", "200", "--score"],
                                 check=True, capture_output=True, text=True)
            self.assertIn(f"found {len(seeds)} of {len(seeds)} planted errors (100%)", res.stdout)


class PrepAndDriveCache(unittest.TestCase):
    def test_prep_pages_offset_and_drive_pack(self):
        with tempfile.TemporaryDirectory() as tmp:
            src1, src2, pages_out, parts_out = (os.path.join(tmp, x) for x in ("v1", "v2", "pages", "parts"))
            os.makedirs(src1); os.makedirs(src2)
            for sdir, arcname in ((src1, "book01_jp2.zip"), (src2, "book02_jp2.zip")):
                buf = io.BytesIO()
                Image.new("RGB", (200, 300), (220, 220, 220)).save(buf, "JPEG")
                with zipfile.ZipFile(os.path.join(sdir, arcname), "w") as zf:
                    zf.writestr("leaf_0001.jpg", buf.getvalue())
            subprocess.run([sys.executable, os.path.join(REPO, "tools", "prep_pages.py"), src1, pages_out, "--workers", "1"],
                           check=True, capture_output=True)
            subprocess.run([sys.executable, os.path.join(REPO, "tools", "prep_pages.py"), src2, pages_out, "--offset", "1000", "--workers", "1"],
                           check=True, capture_output=True)
            self.assertTrue(os.path.exists(os.path.join(pages_out, "p0001.jpg")))
            self.assertTrue(os.path.exists(os.path.join(pages_out, "p1001.jpg")))
            source_json = os.path.join(tmp, "source.json")
            drive_cache.pack(pages_out, parts_out, source_json)
            src_data = json.load(open(source_json, encoding="utf-8"))
            self.assertEqual(len(src_data["parts"]), 1)
            self.assertIn("p1001.jpg", src_data["parts"][0]["files"])

    def test_extract_id_ignores_long_hyphenated_slug(self):
        slug = "browns-and-the-smiths-davies"
        banner_out = f'Created folder "{slug}"\n[{{"id": "1IZzd2wsmJwRPMe2aMuGKuCwGL9XxYO-C", "name": "{slug}"}}]\n'
        self.assertEqual(drive_cache._extract_id(banner_out, exclude=(slug,)), "1IZzd2wsmJwRPMe2aMuGKuCwGL9XxYO-C")
        plain_out = f'Created folder {slug} (id: 1IZzd2wsmJwRPMe2aMuGKuCwGL9XxYO-C)'
        self.assertEqual(drive_cache._extract_id(plain_out, exclude=(slug,)), "1IZzd2wsmJwRPMe2aMuGKuCwGL9XxYO-C")


class RepoLedgerAndPublishedBooks(unittest.TestCase):
    def test_ledger_consistency(self):
        q, b = ledger.load(REPO)
        self.assertEqual(ledger.check(q, b, REPO), [])
        self.assertEqual(len(b.get("books", [])), 50)

    def test_all_published_books_compile_cleanly(self):
        bdir = os.path.join(REPO, "books")
        if not os.path.isdir(bdir):
            return
        for slug in sorted(os.listdir(bdir)):
            full = os.path.join(bdir, slug)
            if not os.path.exists(os.path.join(full, "book.json")):
                continue
            _, warnings = compile_book.compile_book(full)
            blockers = [w for w in warnings if not w.startswith("hyphen join")]
            self.assertEqual(blockers, [], f"{slug} has compile warnings: {blockers}")
            for img in os.listdir(os.path.join(full, "images")) if os.path.isdir(os.path.join(full, "images")) else []:
                if img.lower().endswith((".jpg", ".jpeg", ".png")):
                    im = Image.open(os.path.join(full, "images", img))
                    self.assertLessEqual(max(im.size), 1000, f"{slug}/images/{img} exceeds 1000 px: {im.size}")


if __name__ == "__main__":
    unittest.main()
