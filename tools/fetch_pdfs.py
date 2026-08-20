#!/usr/bin/env python3
"""Download the PDFs listed in tools/pdf-manifest.csv into the repo.

Run by the fetch-pdfs GitHub Actions workflow (or manually from the repo
root). Skips files that already exist, validates that downloads are real
PDFs, and writes a summary to tools/fetch-report.md.
"""
import csv
import os
import time
import urllib.request

MANIFEST = os.path.join(os.path.dirname(__file__), "pdf-manifest.csv")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA = "papers-and-learnings-archiver/1.0 (personal research archive; +https://github.com/in-a-quantum-world/papers-and-learnings)"

def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/pdf,*/*"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read()

def main() -> None:
    ok, skipped, failed = [], [], []
    with open(MANIFEST) as f:
        rows = list(csv.DictReader(f))
    for row in rows:
        dest = os.path.join(ROOT, row["dest_path"])
        if os.path.exists(dest) and os.path.getsize(dest) > 10_000:
            skipped.append(row)
            continue
        try:
            data = fetch(row["url"])
            if not data.startswith(b"%PDF"):
                raise ValueError(f"not a PDF (got {data[:40]!r})")
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            with open(dest, "wb") as out:
                out.write(data)
            ok.append(row)
            print(f"ok      {row['dest_path']}  ({len(data)//1024} KB)")
        except Exception as exc:  # noqa: BLE001 - report and continue
            failed.append((row, str(exc)))
            print(f"FAILED  {row['dest_path']}: {exc}")
        time.sleep(3)  # be polite to the hosts

    report = os.path.join(ROOT, "tools", "fetch-report.md")
    with open(report, "w") as f:
        f.write("# PDF fetch report\n\n")
        f.write(f"- downloaded: {len(ok)}\n- already present: {len(skipped)}\n- failed: {len(failed)}\n")
        if failed:
            f.write("\n## Failures\n\n| file | error |\n|---|---|\n")
            for row, err in failed:
                f.write(f"| `{row['dest_path']}` | {err[:120]} |\n")
    print(f"\ndone: {len(ok)} downloaded, {len(skipped)} already present, {len(failed)} failed")

if __name__ == "__main__":
    main()
