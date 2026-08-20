#!/usr/bin/env python3
"""Add a new item to a collection, in the same format as the rest of the repo.

Appends a formatted entry to `<collection>/README.md` (just above that
collection's "Learnings" section) and, if a PDF URL is given, queues it in
`tools/pdf-manifest.csv` so the fetch-pdfs GitHub Action downloads it on push.

Examples
--------
List the available collections:
    python3 tools/add.py --list

Add a link-only item:
    python3 tools/add.py ml-research \
        --title "Attention Is All You Need" \
        --url "https://arxiv.org/abs/1706.03762" \
        --tags "Transformers,NLP" \
        --note "The original transformer paper."

Add an item and queue its open-access PDF for auto-download:
    python3 tools/add.py ml-research \
        --title "Attention Is All You Need" \
        --url "https://arxiv.org/abs/1706.03762" \
        --pdf-url "https://arxiv.org/pdf/1706.03762" \
        --note "The original transformer paper."
"""
import argparse
import csv
import datetime as _dt
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST = os.path.join(ROOT, "tools", "pdf-manifest.csv")


def collections() -> list[str]:
    """Every collection folder (a directory that has a README.md)."""
    out = []
    for name in sorted(os.listdir(ROOT)):
        path = os.path.join(ROOT, name)
        if name.startswith(".") or name == "tools":
            continue
        if os.path.isdir(path) and os.path.exists(os.path.join(path, "README.md")):
            out.append(name)
    return out


def slugify(text: str) -> str:
    """Turn a title into a filename-safe slug, matching existing PDF names."""
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug[:60].strip("-") or "item"


def build_block(args: argparse.Namespace, pdf_rel: str | None) -> str:
    """Render one item in the repo's standard markdown format."""
    lines = [f"### [{args.title}]({args.url})", ""]

    meta = f"- **Saved:** {args.saved}"
    if args.tags:
        tags = " ".join(f"`{t.strip()}`" for t in args.tags.split(",") if t.strip())
        meta += f" · **Tags:** {tags}"
    lines.append(meta)

    if pdf_rel:
        lines.append(f"- **PDF:** [`{pdf_rel}`]({pdf_rel})")
    if args.note:
        lines.append(f"- **My note:** {args.note}")
    if args.excerpt:
        lines.append(f"- **Excerpt:** {args.excerpt}")

    return "\n".join(lines) + "\n"


def insert_item(readme: str, block: str) -> str:
    """Insert an item block just before the Learnings section (or at the end)."""
    marker = readme.find("\n## 📝 Learnings")
    if marker != -1:
        # Rewind past the "---" divider that precedes the Learnings heading.
        divider = readme.rfind("\n---", 0, marker)
        cut = divider if divider != -1 else marker
        return readme[:cut].rstrip("\n") + "\n\n" + block + readme[cut:]
    return readme.rstrip("\n") + "\n\n" + block


def bump_count(readme: str) -> str:
    """Best-effort increment of the "N items" count in the header line."""
    def repl(m: re.Match) -> str:
        return f"{int(m.group(1)) + 1} items"

    return re.sub(r"(\d+)\s+items", repl, readme, count=1)


def queue_pdf(dest_rel: str, url: str) -> bool:
    """Append a row to the PDF manifest. Returns False if it's already there."""
    existing = set()
    if os.path.exists(MANIFEST):
        with open(MANIFEST, newline="") as f:
            for row in csv.DictReader(f):
                existing.add(row["dest_path"])
    if dest_rel in existing:
        return False
    with open(MANIFEST, "a", newline="") as f:
        csv.writer(f).writerow([dest_rel, url])
    return True


def main() -> None:
    p = argparse.ArgumentParser(
        description="Add an item to a collection README.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    p.add_argument("collection", nargs="?", help="collection folder, e.g. ml-research")
    p.add_argument("--list", action="store_true", help="list collections and exit")
    p.add_argument("--title", help="item title")
    p.add_argument("--url", help="item URL")
    p.add_argument("--tags", help="comma-separated tags, e.g. 'RL,Robotics'")
    p.add_argument("--note", help="your own note about the item")
    p.add_argument("--excerpt", help="a quoted excerpt/summary of the item")
    p.add_argument("--saved", help="save date YYYY-MM-DD (default: today)")
    p.add_argument("--pdf-url", help="direct PDF URL to queue for auto-download")
    p.add_argument("--pdf-name", help="PDF slug (default: derived from title)")
    args = p.parse_args()

    if args.list or not args.collection:
        print("Collections:")
        for c in collections():
            print(f"  {c}")
        if not args.list:
            print("\nPass a collection plus --title and --url to add an item.")
        return

    if args.collection not in collections():
        sys.exit(f"error: no collection '{args.collection}'. Run --list to see options.")
    if not args.title or not args.url:
        sys.exit("error: --title and --url are required to add an item.")

    if not args.saved:
        args.saved = _dt.date.today().isoformat()

    pdf_link = None  # collection-relative path shown in the README
    if args.pdf_url:
        slug = slugify(args.pdf_name or args.title)
        pdf_link = f"pdfs/{slug}.pdf"
        dest_rel = f"{args.collection}/{pdf_link}"  # repo-root path for the manifest
        if queue_pdf(dest_rel, args.pdf_url):
            print(f"queued PDF  {dest_rel}  (fetched on next push to main)")
        else:
            print(f"PDF already queued: {dest_rel}")

    readme_path = os.path.join(ROOT, args.collection, "README.md")
    with open(readme_path, encoding="utf-8") as f:
        readme = f.read()
    readme = insert_item(readme, build_block(args, pdf_link))
    readme = bump_count(readme)
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme)

    print(f"added '{args.title}' to {args.collection}/README.md")
    print("\nNext: review, then commit & push:")
    print(f"  git add -A && git commit -m 'Add: {args.title}' && git push")


if __name__ == "__main__":
    main()
