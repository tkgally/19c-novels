#!/usr/bin/env python3
"""The Google Drive cache of a novel's working files (page images, IA metadata, IA OCR text).

Why: so that the Internet Archive is asked for a novel's files once, and the repository holds no scans.
Drive root folder "19C Novels" (id 1ecaIjeQldRJ8cfAD1-mGtNbofezQLbcy) / one subfolder per novel slug.

  drive_cache.py pack PAGES_DIR OUT_DIR --source SOURCE.json [--extra FILE ...] [--limit BYTES] [--append]
        Zips the page images (and extra small files) into independent parts (OUT_DIR/pages-001.zip …) and writes
        their names, contents, and sha256 into SOURCE.json under "parts".
  drive_cache.py upload SOURCE.json OUT_DIR [--slug SLUG] [--parent ROOT_FOLDER_ID]
        Uses the `gdrive` CLI to create/reuse the novel's subfolder inside "19C Novels", upload every part still
        missing a `drive_id`, and record each returned file id in SOURCE.json.
  drive_cache.py setid SOURCE.json PART_NAME DRIVE_ID
  drive_cache.py todo SOURCE.json OUT_DIR         the parts still without a drive_id
  drive_cache.py fetch SOURCE.json DEST_DIR [--pages p0010-p0040]
        Downloads the parts (all, or those holding the pages asked for) via `gdrive readonly download` (falling back
        to curl only if `gdrive` is unavailable), checks sha256, and unzips into DEST_DIR. Files already there are kept.

SOURCE.json lives in the novel's directory in the repo (wip/<slug>/source.json, later books/<slug>/).
"""
import argparse, hashlib, json, os, re, shutil, subprocess, sys, time, zipfile

ROOT_FOLDER_ID = "1ecaIjeQldRJ8cfAD1-mGtNbofezQLbcy"
LIMIT = 8_000_000


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def load(p):
    return json.load(open(p, encoding="utf-8")) if os.path.exists(p) else {}


def save(p, d):
    json.dump(d, open(p, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    open(p, "a", encoding="utf-8").write("\n")


def pack(pages_dir, out_dir, source, extra=(), limit=LIMIT, append=False):
    os.makedirs(out_dir, exist_ok=True)
    files = [os.path.join(pages_dir, f) for f in sorted(os.listdir(pages_dir))
             if re.fullmatch(r"p\d+[a-z]?\.(jpg|png)", f) or f == "leaves.json"] + list(extra)
    if append:
        have = {f for p in load(source).get("parts", []) for f in p["files"]} - {"leaves.json"}
        files = [f for f in files if os.path.basename(f) not in have]
    groups, cur, size = [], [], 0
    for f in files:
        s = os.path.getsize(f) + 300
        if s > limit:
            sys.exit(f"{f} is {s} bytes: larger than one part ({limit}). Lower --height/--quality in prep_pages.py or raise --limit.")
        if cur and size + s > limit:
            groups.append(cur); cur, size = [], 0
        cur.append(f); size += s
    if cur:
        groups.append(cur)
    src = load(source)
    old = {p["sha256"]: p for p in src.get("parts", [])}
    kept = src.get("parts", []) if append else []
    parts = list(kept)
    for i, g in enumerate(groups, len(kept) + 1):
        name = f"pages-{i:03d}.zip"
        path = os.path.join(out_dir, name)
        with zipfile.ZipFile(path, "w", zipfile.ZIP_STORED) as z:
            for f in g:
                zi = zipfile.ZipInfo(os.path.basename(f), (1980, 1, 1, 0, 0, 0))
                z.writestr(zi, open(f, "rb").read())
        h = sha(path)
        part = {"name": name, "sha256": h, "bytes": os.path.getsize(path), "files": [os.path.basename(f) for f in g]}
        if h in old and old[h].get("drive_id"):
            part["drive_id"] = old[h]["drive_id"]
        parts.append(part)
    src["parts"] = parts
    save(source, src)
    print(f"{len(parts)} parts, {sum(p['bytes'] for p in parts) / 1e6:.1f} MB, in {out_dir}")
    todo(source, out_dir)


def todo(source, out_dir):
    src = load(source)
    left = [p for p in src.get("parts", []) if not p.get("drive_id")]
    print(f"{len(left)} of {len(src.get('parts', []))} parts to upload (Drive folder id: {src.get('drive_folder_id', 'NOT SET')})")
    for p in left:
        print(f"{p['name']}\tsha256:{p['sha256']}:{os.path.abspath(os.path.join(out_dir, p['name']))}")


def setid(source, name, drive_id):
    src = load(source)
    for p in src.get("parts", []):
        if p["name"] == name:
            p["drive_id"] = drive_id
            save(source, src)
            return
    sys.exit("no such part: " + name)


def _extract_id(stdout, exclude=()):
    text = (stdout or "").strip()
    candidates = [text]
    for ch in ("{", "["):
        idx = text.find(ch)
        if idx > 0:
            candidates.append(text[idx:])
    for cand in candidates:
        try:
            j = json.loads(cand)
            if isinstance(j, list) and j:
                j = j[0]
            if isinstance(j, dict):
                for k in ("id", "fileId", "folderId"):
                    if isinstance(j.get(k), str) and j[k] and j[k] not in exclude:
                        return j[k]
                for v in j.values():
                    if isinstance(v, dict) and isinstance(v.get("id"), str) and v["id"] not in exclude:
                        return v["id"]
        except ValueError:
            pass
    for m in re.finditer(r'"id"\s*:\s*"([^"]+)"', text):
        if m.group(1) not in exclude:
            return m.group(1)
    for m in re.finditer(r"\b([A-Za-z0-9_-]{20,})\b", text):
        tok = m.group(1)
        if tok not in exclude and tok.count("-") < 3:
            return tok
    return None


def upload(source, out_dir, slug=None, parent=ROOT_FOLDER_ID):
    """Create/reuse the novel's Drive subfolder and upload any pending parts via `gdrive`."""
    if not shutil.which("gdrive"):
        sys.exit("gdrive CLI not found on PATH")
    src = load(source)
    slug = slug or os.path.basename(os.path.dirname(os.path.abspath(source)))
    folder_id = src.get("drive_folder_id")
    if not folder_id or folder_id == slug:
        ls = subprocess.run(["gdrive", "readonly", "ls", parent, "--json"], capture_output=True, text=True, check=True)
        items = json.loads(ls.stdout)
        rows = items if isinstance(items, list) else items.get("files", items.get("items", []))
        hit = next((x for x in rows if x.get("name") == slug and "folder" in (x.get("mimeType", "") + x.get("type", "")).lower()), None)
        if hit:
            folder_id = hit["id"]
        else:
            mk = subprocess.run(["gdrive", "mutate", "mkdir", slug, "--parent", parent, "--json"],
                                capture_output=True, text=True, check=True)
            folder_id = _extract_id(mk.stdout, exclude=(slug, parent))
        if not folder_id:
            sys.exit("could not determine Drive folder id for " + slug)
        src["drive_folder_id"] = folder_id
        save(source, src)
        print(f"Drive folder {slug}: {folder_id}")

    uploaded = 0
    for p in src.get("parts", []):
        if p.get("drive_id"):
            continue
        fpath = os.path.join(out_dir, p["name"])
        if not os.path.exists(fpath):
            sys.exit(f"missing part file: {fpath}")
        up = subprocess.run(
            ["gdrive", "mutate", "upload", fpath, "--parent", folder_id, "--mime-type", "application/zip", "--json"],
            capture_output=True, text=True, check=True,
        )
        fid = _extract_id(up.stdout, exclude=(p["name"], slug, folder_id))
        if not fid:
            sys.exit(f"could not parse Drive id from upload output: {up.stdout[:200]}")
        p["drive_id"] = fid
        save(source, src)
        uploaded += 1
        print(f"  uploaded {p['name']} -> {fid}")
    print(f"upload complete: {uploaded} new parts uploaded ({len(src.get('parts', []))} total)")


def page_filter(pages):
    if not pages:
        return None
    spans = []
    for item in pages.split(","):
        item = item.strip()
        m = re.fullmatch(r"(p\d{4}[a-z]?)(?:-(p\d{4}[a-z]?))?", item)
        if not m:
            sys.exit(f"--pages: '{item}' is not pNNNN or pNNNN-pNNNN")
        spans.append((m.group(1), m.group(2) or m.group(1)))

    def inside(stem, lo, hi):
        return lo <= stem and (stem <= hi or (len(hi) == 5 and stem[:5] == hi))
    return lambda f: not f.startswith("p") or any(inside(f.split(".")[0], lo, hi) for lo, hi in spans)


def _download_part(drive_id, tmp):
    if shutil.which("gdrive"):
        if os.path.exists(tmp):
            os.remove(tmp)
        r = subprocess.run(["gdrive", "readonly", "download", drive_id, "--out", tmp], capture_output=True, text=True)
        if r.returncode == 0 and os.path.exists(tmp):
            return True
    subprocess.run(["curl", "-sSL", "-o", tmp, f"https://drive.usercontent.google.com/download?id={drive_id}&export=download&confirm=t"])
    return os.path.exists(tmp)


def fetch(source, dest, pages=None):
    src = load(source)
    os.makedirs(dest, exist_ok=True)
    keep = page_filter(pages)
    for p in src.get("parts", []):
        want = [f for f in p["files"] if keep is None or keep(f)]
        if not want or all(os.path.exists(os.path.join(dest, f)) for f in want):
            continue
        if not p.get("drive_id"):
            sys.exit(f"{p['name']} has no drive_id: the cache is incomplete (fetch the novel from the Internet Archive again)")
        tmp = os.path.join(dest, "_" + p["name"])
        for attempt in range(4):
            _download_part(p["drive_id"], tmp)
            if os.path.exists(tmp) and sha(tmp) == p["sha256"]:
                break
            time.sleep(5 * (attempt + 1))
        else:
            sys.exit(f"could not fetch {p['name']} from Drive (sha256 mismatch or download failed)")
        with zipfile.ZipFile(tmp) as z:
            for n in z.namelist():
                if os.path.basename(n) != n or n.startswith("."):
                    sys.exit("unexpected name in archive: " + n)
                open(os.path.join(dest, n), "wb").write(z.read(n))
        os.remove(tmp)
    n = len([f for f in os.listdir(dest) if re.fullmatch(r"p\d+[a-z]?\.(jpg|png)", f)])
    print(f"{n} page images in {dest}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("pack"); s.add_argument("pages_dir"); s.add_argument("out_dir"); s.add_argument("--source", required=True); s.add_argument("--extra", nargs="*", default=[]); s.add_argument("--limit", type=int, default=LIMIT); s.add_argument("--append", action="store_true")
    s = sub.add_parser("upload"); s.add_argument("source"); s.add_argument("out_dir"); s.add_argument("--slug"); s.add_argument("--parent", default=ROOT_FOLDER_ID)
    s = sub.add_parser("setid"); s.add_argument("source"); s.add_argument("name"); s.add_argument("drive_id")
    s = sub.add_parser("todo"); s.add_argument("source"); s.add_argument("out_dir")
    s = sub.add_parser("fetch"); s.add_argument("source"); s.add_argument("dest"); s.add_argument("--pages")
    a = ap.parse_args()
    if a.cmd == "pack":
        pack(a.pages_dir, a.out_dir, a.source, a.extra, limit=a.limit, append=a.append)
    elif a.cmd == "upload":
        upload(a.source, a.out_dir, slug=a.slug, parent=a.parent)
    elif a.cmd == "setid":
        setid(a.source, a.name, a.drive_id)
    elif a.cmd == "todo":
        todo(a.source, a.out_dir)
    else:
        fetch(a.source, a.dest, a.pages)


if __name__ == "__main__":
    main()
