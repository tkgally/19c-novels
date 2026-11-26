#!/usr/bin/env python3
"""Page images for the pipeline from an Internet Archive page-image archive.

  prep_pages.py SRC_DIR OUT_DIR [--height 1800] [--quality 72] [--color] [--offset 0] [--workers 4]

SRC_DIR is what `ia.py fetch` wrote (…_jp2.zip or .tar, …_scandata.xml). Writes OUT_DIR/pNNNN.jpg, where NNNN is
the leaf number in the archive's file names plus `--offset` (e.g. --offset 1000 for Volume II -> p1000.jpg …,
--offset 2000 for Volume III -> p2000.jpg …), scaled to --height pixels, greyscale unless --color; and
OUT_DIR/leaves.json recording hidden leaves and asserted page numbers.
Illustrations and covers are cropped from full-size leaves:
  prep_pages.py SRC_DIR OUT_DIR [--offset 1000] --full p1012,p1045 -> OUT_DIR/full/p1012.jpg at full size, colour, quality 90
"""
import argparse, concurrent.futures as cf, io, json, os, re, sys, tarfile, zipfile
import xml.etree.ElementTree as ET


def archive(src):
    for f in sorted(os.listdir(src)):
        if re.search(r"_(jp2|tif|jpg|images)\.(zip|tar)$", f):
            return os.path.join(src, f)
    sys.exit("no page-image archive in " + src)


def members(path):
    if path.endswith(".zip"):
        names = zipfile.ZipFile(path).namelist()
    else:
        names = [m.name for m in tarfile.open(path).getmembers()]
    return [(n, path) for n in sorted(names) if re.search(r"_\d{4}\.(jp2|tif|jpg)$", n)]


def read_member(path, name):
    if path.endswith(".zip"):
        return zipfile.ZipFile(path).read(name)
    return tarfile.open(path).extractfile(name).read()


def scandata(src):
    out, hidden = {}, []
    for f in os.listdir(src):
        if f.endswith("scandata.xml"):
            root = ET.parse(os.path.join(src, f)).getroot()
            for p in root.iter("page"):
                n = int(p.get("leafNum"))
                acc = (p.findtext("addToAccessFormats") or "true").strip().lower()
                out[n] = {"type": p.findtext("pageType") or "", "number": p.findtext("pageNumber") or ""}
                if acc == "false":
                    hidden.append(n)
                    out[n]["hidden"] = True
    return out, hidden


def convert(job):
    name, read, out, height, quality, color = job
    from PIL import Image
    if os.path.exists(out):
        return
    im = Image.open(io.BytesIO(read_member(read, name)))
    im = im.convert("RGB" if color else "L")
    if height and im.height > height:
        im = im.resize((round(im.width * height / im.height), height), Image.LANCZOS)
    im.save(out + ".tmp", "JPEG", quality=quality, optimize=True)
    os.replace(out + ".tmp", out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src"); ap.add_argument("out")
    ap.add_argument("--height", type=int, default=1800)
    ap.add_argument("--quality", type=int, default=72)
    ap.add_argument("--color", action="store_true")
    ap.add_argument("--offset", type=int, default=0, help="leaf number offset for multi-volume novels (e.g. 1000 for Vol. II)")
    ap.add_argument("--full", help="comma-separated leaves to write at full size into OUT/full/")
    ap.add_argument("--workers", type=int, default=4)
    a = ap.parse_args()
    arc = archive(a.src)
    ms = members(arc)
    os.makedirs(a.out, exist_ok=True)
    jobs = []
    if a.full:
        want = set(a.full.split(","))
        os.makedirs(os.path.join(a.out, "full"), exist_ok=True)
        for n, read in ms:
            num = int(re.search(r"_(\d{4})\.\w+$", n).group(1)) + a.offset
            leaf = f"p{num:04d}"
            if leaf in want:
                jobs.append((n, read, os.path.join(a.out, "full", leaf + ".jpg"), 0, 90, True))
    else:
        for n, read in ms:
            num = int(re.search(r"_(\d{4})\.\w+$", n).group(1)) + a.offset
            leaf = f"p{num:04d}"
            jobs.append((n, read, os.path.join(a.out, leaf + ".jpg"), a.height, a.quality, a.color))
        info, hidden = scandata(a.src)
        lf_path = os.path.join(a.out, "leaves.json")
        existing = json.load(open(lf_path, encoding="utf-8")) if os.path.exists(lf_path) and a.offset else {}
        leaves_map = dict(existing.get("leaves", {}))
        for k, v in sorted(info.items()):
            leaves_map[f"p{k + a.offset:04d}"] = v
        rec = {
            "archive": os.path.basename(arc) if not existing else existing.get("archive"),
            "leaf_count": len(leaves_map) or len(ms),
            "height": a.height,
            "quality": a.quality,
            "color": a.color,
            "hidden_leaves": hidden if not existing else existing.get("hidden_leaves", []),
            "leaves": leaves_map,
        }
        if a.offset:
            vols = list(existing.get("volumes", []))
            vols.append({"offset": a.offset, "archive": os.path.basename(arc), "leaf_count": len(ms), "hidden_leaves": hidden})
            rec["volumes"] = vols
        json.dump(rec, open(lf_path, "w", encoding="utf-8"), indent=1)
    with cf.ProcessPoolExecutor(a.workers) as ex:
        list(ex.map(convert, jobs))
    target_dir = os.path.join(a.out, "full") if a.full else a.out
    files = [f for f in os.listdir(target_dir) if f.endswith(".jpg")]
    total = sum(os.path.getsize(os.path.join(target_dir, f)) for f in files)
    print(f"{len(files)} images, {total / 1e6:.1f} MB in {target_dir}")


if __name__ == "__main__":
    main()
