#!/usr/bin/env python3
"""Copy the shared head / nav / footer from _partials/ into every site page.

Edit _partials/*.html once, then run (from the PersonalPage folder):
    python3 _tools/sync_layout.py
Each page keeps its own <title> and meta description; those feed the link-preview
(Open Graph) tags. Only text between <!-- BEGIN SHARED:x --> / <!-- END SHARED:x -->
is replaced. Folders starting with "_" are not published by GitHub Pages.
"""
import datetime, html, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGES = ["index.html", "research.html", "teaching.html", "publications.html", "contact.html"]
PARTS = {n: (ROOT / "_partials" / f"{n}.html").read_text(encoding="utf-8").rstrip("\n")
         for n in ("head", "nav", "footer")}
UPDATED = datetime.date.today().strftime("%B %Y")


def fill(name, page, text):
    out = PARTS[name]
    if name == "head":
        title = re.search(r"<title>(.*?)</title>", text, re.S).group(1).strip()
        m = re.search(r'<meta name="description" content="([^"]*)"', text)
        desc = m.group(1) if m else ""
        out = out.replace("{title}", title).replace("{description}", desc)
        out = out.replace("{page}", "" if page == "index.html" else page)
    elif name == "nav":
        out = re.sub(r"\{active:([^}]+)\}", lambda m: " active" if m.group(1) == page else "", out)
    elif name == "footer":
        out = out.replace("{updated}", UPDATED)
    return out


def main():
    for page in PAGES:
        p = ROOT / page
        text = p.read_text(encoding="utf-8")
        for name in PARTS:
            pat = re.compile(rf"(<!-- BEGIN SHARED:{name} -->).*?([ \t]*<!-- END SHARED:{name} -->)", re.S)
            if not pat.search(text):
                sys.exit(f"{page}: marker SHARED:{name} missing")
            text = pat.sub(lambda m: m.group(1) + "\n" + fill(name, page, text) + "\n" + m.group(2), text)
        p.write_text(text, encoding="utf-8")
        print("synced", page)


if __name__ == "__main__":
    main()
