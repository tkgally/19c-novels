#!/usr/bin/env python3
"""Sampled planted-error audit of a finished novel against the scans — measures the checker as well as the book.

  audit_sample.py --pages-dir DIR --images DIR --out DIR --rules prompts/transcribe.md --prepare [--n 6 | --pages p0012,p0040]
        Picks N pages at random (repeatable via --seed), plants 5 known errors per page, saves the secret answer
        key in OUT/_secret/seeds.json, and writes blind proofreading tasks in OUT/blind/ for a fresh Gemini Pro
        subagent (`Model: "pro"`).
  audit_sample.py --pages-dir DIR --images DIR --out DIR --rules prompts/transcribe.md [--score]
        Scores OUT/whole/pNNNN.txt against OUT/_secret/seeds.json, reporting planted-error recall by kind and
        listing every non-planted difference in OUT/candidates.tsv for scan-crop inspection.
"""
import argparse, difflib, hashlib, json, os, random, re, sys
from pathlib import Path

TASK = """
## Your task now: PROOFREAD a transcription against the scan (do not transcribe)

Below is a transcription of {what}, made under the rules above and shown as plain text: italics, small
capitals, footnotes, and their marks have been removed on purpose — do not report them. It may begin or end in
the middle of a sentence.

Compare it with the scan word by word and letter by letter, and report EVERY place where the transcription
does not say what the print says:
- a wrong letter or word; a spelling that has been modernized or "corrected" (the printed spelling always wins,
  even an obvious misprint — look hard at every word that looks modern: `show` for printed `shew`,
  `today` for `to-day`, `connection` for `connexion`), and at every proper name and foreign word;
- a wrong capital or lower-case initial; a missing or added word; a missing line or sentence; words that are not
  on the page; a wrong punctuation mark; a wrong paragraph break.
Do NOT report the conventions of the transcription: ligatures written as plain letters, modern spacing around
punctuation and inside quotation marks, words rejoined across line ends, omitted running heads, page numbers,
and signature marks, straight or curly quotes, dash length, tables left out.

The transcription reads fluently even where it is wrong, so do not read it for sense: check it against the
shapes on the scan. {where}
CRITICAL: Inspect ONLY the scan image `{img}` and this task file; NEVER read any other directory (`_secret/`, `pages/`, `draft/`, `verify/`, `judge/`).

Write one JSON object per difference, one per line, and nothing else, to `{out_file}`:
{{"given": "4 to 8 consecutive words copied exactly from the transcription, including the wrong part", "print": "the same words exactly as the scan prints them", "sure": "high" | "medium" | "low"}}
If you find no difference, write the single word NONE to `{out_file}`.

<transcription>
{text}
</transcription>
"""

MODERN = [(r"\b([Tt])o-(day|morrow|night)\b", r"\1o\2"), (r"\b([Ss])hew", r"\1how"), (r"\b([Cc])onnexion", r"\1onnection"),
          (r"\b([A-Za-z]{3,})our\b", r"\1or"), (r"\b([Aa])ny one\b", r"\1nyone"), (r"\b([Ee])very one\b", r"\1veryone"),
          (r"\b([Ss])ome one\b", r"\1omeone"), (r"\b([Ff])or ever\b", r"\1orever"), (r"\b([A-Za-z]{4,})ise\b", r"\1ize"),
          (r"\b([Gg])rey\b", r"\1ray"), (r"\b([A-Za-z]{3,})tre\b", r"\1ter"), (r"\b([Ww])aggon", r"\1agon"),
          (r"\b([A-Za-z]{3,})'d\b", r"\1ed")]
REAL = [("these", "those"), ("it", "if"), ("then", "than"), ("on", "or"), ("not", "nor"), ("he", "be"), ("had", "bad"),
        ("sound", "found"), ("same", "fame"), ("sit", "fit"), ("soul", "foul"), ("sight", "fight"), ("set", "let"),
        ("hear", "bear"), ("hand", "band"), ("heat", "beat"), ("this", "his"), ("when", "then"), ("were", "where")]
REALMAP = {a: b for a, b in REAL}
REALMAP.update({b: a for a, b in REAL})
LOOKALIKE = {"s": "f", "f": "s", "e": "c", "c": "e", "h": "b", "n": "u", "u": "n"}


def plain_page(t):
    out = []
    for ln in t.splitlines():
        s = ln.strip()
        if not s or re.match(r"\[\[(page|blank|image:|fn )", s) or s in ("<blockquote>", "</blockquote>", "<verse>", "</verse>"):
            continue
        s = re.sub(r"\[\[fnref [^\]]*\]\]", "", s)
        s = re.sub(r"\[\[corr ([^|\]]*)\|[^\]]*\]\]", r"\1", s)
        s = re.sub(r"\[\[supplied ([^\]]*)\]\]", r"\1", s).replace("[[gap]]", "[…]")
        if s.startswith("|") and s.endswith("|"):
            continue
        s = re.sub(r"\[\[[a-z]+\]\] ?", "", s)
        s = re.sub(r"^#{1,3} ", "", s)
        s = re.sub(r"</?[a-z]+(?: [^>]*)?>", "", s)
        out.append(s)
    return "\n\n".join(out)


def plant(text, rng):
    seeds, taken = [], []

    def free(a, b):
        return all(b + 40 < x or a - 40 > y for x, y in taken)

    def apply(kind, a, b, new):
        nonlocal text
        was = text[a:b]
        text = text[:a] + new + text[b:]
        d = len(new) - (b - a)
        for s in seeds:
            if s["at"] > a:
                s["at"] += d
        taken[:] = [(x + d, y + d) if x > a else (x, y) for x, y in taken]
        taken.append((a, a + len(new)))
        seeds.append({"kind": kind, "at": a, "was": was, "now": new,
                      "context": text[max(0, a - 30):a + len(new) + 30].replace("\n", " ")})

    def pick(cands):
        cands = [c for c in cands if free(c[0], c[1])]
        return rng.choice(cands) if cands else None

    cands = []
    for pat, rep in MODERN:
        for m in re.finditer(pat, text):
            cands.append((m.start(), m.end(), m.expand(rep)))
    c = pick(cands)
    if c:
        apply("modernized", *c)
    else:
        c = pick([(m.start(1), m.end(1), m.group(1).lower()) for m in re.finditer(r"(?<=[a-z,] )([A-Z])(?=[a-z]{4,})", text)])
        if c:
            apply("capital", *c)

    cands = []
    for m in re.finditer(r"\b[a-z]{6,}\b", text):
        idx = [i for i, ch in enumerate(m.group()) if ch in LOOKALIKE and 0 < i < len(m.group()) - 1]
        if idx:
            i = rng.choice(idx)
            cands.append((m.start() + i, m.start() + i + 1, LOOKALIKE[m.group()[i]]))
    c = pick(cands)
    if c:
        apply("letter", *c)

    c = pick([(m.start(), m.end(), REALMAP[m.group().lower()].capitalize() if m.group()[0].isupper() else REALMAP[m.group()])
              for m in re.finditer(r"\b[A-Za-z]+\b", text) if m.group().lower() in REALMAP])
    if c:
        apply("real word", *c)

    c = pick([(m.start(), m.end(), " ") for m in re.finditer(r"(?<=[a-z]) (?:the|of|and|to|a|in) (?=[a-zA-Z])", text)])
    if c:
        apply("dropped word", *c)

    c = pick([(m.start(), m.end(), ";" if m.group() == "," else ",") for m in re.finditer(r"(?<=[a-z])[,;](?= [a-z])", text)])
    if c:
        apply("punctuation", *c)
    return text, seeds


def locate(given, text):
    g = re.sub(r"\s+", " ", given).strip()
    if not g:
        return None
    m = re.search(r"\s+".join(re.escape(w) for w in g.split(" ")), text)
    if m:
        return m.start(), m.end()
    sm = difflib.SequenceMatcher(None, text, g, autojunk=False)
    blk = sm.find_longest_match(0, len(text), 0, len(g))
    if blk.size >= max(8, 0.5 * len(g)):
        return max(0, blk.a - blk.b), blk.a - blk.b + len(g)
    return None


def strips(img, d, name, n=3, overlap=0.05):
    from PIL import Image
    os.makedirs(d, exist_ok=True)
    im = Image.open(img)
    w, h = im.size
    out = []
    for k in range(n):
        f = os.path.join(d, f"{name}-{k + 1}.png")
        if not os.path.exists(f):
            im.crop((0, max(0, int(h * (k / n - overlap))), w, min(h, int(h * ((k + 1) / n + overlap))))).save(f)
        out.append(os.path.abspath(f))
    return out


def parse_findings(reply):
    out = []
    for ln in (reply or "").splitlines():
        ln = ln.strip().strip("`")
        if ln.startswith("{"):
            try:
                d = json.loads(ln)
                if d.get("given") and d.get("given") != d.get("print"):
                    out.append(d)
            except ValueError:
                pass
    return out


def _seeds_path(out_dir):
    sec = os.path.join(out_dir, "_secret", "seeds.json")
    legacy = os.path.join(out_dir, "seeds.json")
    return legacy if os.path.exists(legacy) and not os.path.exists(sec) else sec


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--pages-dir", required=True)
    ap.add_argument("--images", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--rules", required=True)
    ap.add_argument("--n", type=int, default=6)
    ap.add_argument("--pages")
    ap.add_argument("--seed")
    ap.add_argument("--model", default="gemini-pro")
    ap.add_argument("--conditions", default="whole")
    ap.add_argument("--no-seeds", action="store_true")
    ap.add_argument("--min-chars", type=int, default=800)
    ap.add_argument("--prepare", action="store_true", help="plant errors and write blind proofreading tasks")
    ap.add_argument("--score", action="store_true", help="score completed audit findings against planted seeds")
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    rules = open(a.rules, encoding="utf-8").read().split("## Output format")[0]
    seedname = a.seed or os.path.basename(os.path.abspath(os.path.dirname(os.path.abspath(a.pages_dir))))

    def image_of(p):
        for ext in (".png", ".jpg", ".jpeg"):
            f = os.path.join(a.images, p + ext)
            if os.path.exists(f):
                return os.path.abspath(f)
        return None

    plan_f = _seeds_path(a.out)
    blind_dir = os.path.join(a.out, "blind")
    os.makedirs(blind_dir, exist_ok=True)
    if os.path.exists(plan_f):
        plan = json.load(open(plan_f, encoding="utf-8"))
    else:
        os.makedirs(os.path.dirname(plan_f), exist_ok=True)
        texts = {}
        for f in sorted(os.listdir(a.pages_dir)):
            if re.fullmatch(r"p\d+[a-z]?\.txt", f):
                t = plain_page(open(os.path.join(a.pages_dir, f), encoding="utf-8").read())
                if len(t) >= a.min_chars and image_of(f[:-4]):
                    texts[f[:-4]] = t
        if a.pages:
            chosen = [p.strip() for p in a.pages.split(",") if p.strip() in texts]
        else:
            rng = random.Random(int(hashlib.sha1(seedname.encode()).hexdigest(), 16))
            chosen = sorted(rng.sample(sorted(texts), min(a.n, len(texts))))
        plan = {}
        for p in chosen:
            rng = random.Random(int(hashlib.sha1((seedname + p).encode()).hexdigest(), 16))
            given, seeds = (texts[p], []) if a.no_seeds else plant(texts[p], rng)
            open(os.path.join(blind_dir, p + ".given.txt"), "w", encoding="utf-8").write(given)
            plan[p] = seeds
        json.dump(plan, open(plan_f, "w", encoding="utf-8"), indent=1, ensure_ascii=False)

    conds = [c.strip() for c in a.conditions.split(",") if c.strip()]
    if a.prepare:
        todo = []
        for p in plan:
            given_p = os.path.join(blind_dir, p + ".given.txt")
            text = open(given_p, encoding="utf-8").read()
            img = image_of(p)
            if "whole" in conds:
                os.makedirs(os.path.join(a.out, "whole"), exist_ok=True)
                out_f = os.path.abspath(os.path.join(a.out, "whole", p + ".txt"))
                if not (os.path.exists(out_f) and os.path.getsize(out_f) > 0):
                    tf = os.path.abspath(os.path.join(blind_dir, f"task-whole-{p}.md"))
                    Path(tf).write_text(
                        rules + TASK.format(
                            what="one page",
                            where=f"Open the page image `{img}` with `view_file` first.",
                            img=img,
                            out_file=out_f,
                            text=text,
                        ),
                        encoding="utf-8",
                    )
                    todo.append((p, "whole", tf, out_f))
            if "strips" in conds:
                os.makedirs(os.path.join(a.out, "strips"), exist_ok=True)
                for k, sf in enumerate(strips(img, os.path.join(blind_dir, "_strips"), p)):
                    part = ("top", "middle", "bottom")[k]
                    out_f = os.path.abspath(os.path.join(a.out, "strips", f"{p}-{k + 1}.txt"))
                    if not (os.path.exists(out_f) and os.path.getsize(out_f) > 0):
                        tf = os.path.abspath(os.path.join(blind_dir, f"task-strips-{p}-{k + 1}.md"))
                        Path(tf).write_text(
                            rules + TASK.format(
                                what="one page",
                                where=f"The image `{sf}` shows only the {part} third of the page, enlarged. Open it with `view_file` first and check only the part of the transcription shown in this strip.",
                                img=sf,
                                out_file=out_f,
                                text=text,
                            ),
                            encoding="utf-8",
                        )
                        todo.append((f"{p}-{k + 1}", "strips", tf, out_f))
        inst = os.path.abspath(os.path.join(blind_dir, "INSTRUCTIONS.md"))
        lines = [
            f"# Blind Sampled Audit ({len(todo)} task(s))",
            "",
            "STRICT BLINDNESS RULE: Read ONLY the task files in this `blind/` directory and the scan images they reference. NEVER read `_secret/`, `pages/`, `draft/`, `verify/`, or `judge/`.",
            "",
        ] + [f"- `{nm}` ({cond}): read `{tf}` -> write `{of}`" for nm, cond, tf, of in todo]
        Path(inst).write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"audit_sample --prepare: {len(plan)} pages ({', '.join(plan)}), {len(todo)} task(s) -> {inst}")
        return

    # Score mode
    rep, cand = [], ["condition\tpage\tsure\tgiven\tprint"]
    for cond in conds:
        found, total, ncand = {}, {}, 0
        for p, seeds in plan.items():
            given_p = os.path.join(blind_dir, p + ".given.txt")
            if not os.path.exists(given_p):
                given_p = os.path.join(a.out, p + ".given.txt")
            text = open(given_p, encoding="utf-8").read()
            fs = []
            cdir = os.path.join(a.out, cond)
            for f in sorted(os.listdir(cdir)) if os.path.isdir(cdir) else []:
                if (f == p + ".txt" or f.startswith(p + "-")) and f.endswith(".txt"):
                    fs += parse_findings(open(os.path.join(cdir, f), encoding="utf-8").read())
            spans = [(locate(x["given"], text), x) for x in fs]
            hit_f = set()
            for s in seeds:
                total[s["kind"]] = total.get(s["kind"], 0) + 1
                for i, (sp, x) in enumerate(spans):
                    if sp and sp[0] - 12 <= s["at"] <= sp[1] + 12:
                        hit_f.add(i)
                        s.setdefault("found_by", [])
                        if cond not in s["found_by"]:
                            s["found_by"].append(cond)
                            found[s["kind"]] = found.get(s["kind"], 0) + 1
            seen = set()
            for i, (sp, x) in enumerate(spans):
                key = (x["given"], x.get("print"))
                if i not in hit_f and key not in seen:
                    seen.add(key)
                    ncand += 1
                    cand.append(f"{cond}\t{p}\t{x.get('sure', '')}\t{x['given']}\t{x.get('print', '')}")
        tot, fnd = sum(total.values()), sum(found.values())
        rep.append(f"{cond}: found {fnd} of {tot} planted errors ({100 * fnd / tot:.0f}%)" if tot else f"{cond}: no planted errors")
        for k in sorted(total):
            rep.append(f"    {k:14} {found.get(k, 0)}/{total[k]}")
        rep.append(f"    other differences reported (candidates to check on the scan): {ncand}")
    log_p = os.path.join(a.out, "log.jsonl")
    if not os.path.exists(log_p):
        with open(log_p, "w", encoding="utf-8") as lf:
            for p in plan:
                lf.write(json.dumps({"page": p, "condition": conds[0], "model": a.model, "cost": 0.0}) + "\n")
    rep.append(f"pages: {len(plan)} ({', '.join(plan)}); model {a.model}")
    json.dump(plan, open(plan_f, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    open(os.path.join(a.out, "report.txt"), "w", encoding="utf-8").write("\n".join(rep) + "\n")
    open(os.path.join(a.out, "candidates.tsv"), "w", encoding="utf-8").write("\n".join(cand) + "\n")
    print("\n".join(rep))


if __name__ == "__main__":
    main()
