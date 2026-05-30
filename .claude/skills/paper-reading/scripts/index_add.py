#!/usr/bin/env python3
"""index_add.py — idempotently add/update one paper entry in papers.json.

papers.json is the single source of truth that the landing page (index.html)
renders into cards. This script only ever touches *metadata* keyed by slug — it
never reads or depends on the interpretation content of other papers, so it is
safe to run without violating the "each paper is read in isolation" rule.

Usage:
  index_add.py <papers.json> --slug SLUG --title TITLE [options]

Options:
  --authors STR     comma- or semicolon-separated author list (display string)
  --team STR        affiliations / lab / company
  --arxiv URL       canonical paper link (arXiv abs page or other)
  --code URL        primary code repo (optional, shown as a chip)
  --date YYYY-MM-DD read/added date (default: today)
  --published STR   paper publication date / venue (free text)
  --tldr STR        one or two sentence summary shown on the card
  --tags STR        comma-separated tags
  --path STR        link target (default: papers/<slug>/index.html)

Re-running with the same --slug updates that entry in place. Entries are kept
sorted by --date descending (newest first).
"""
import argparse
import datetime as dt
import json
import os
import sys


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("papers_json")
    ap.add_argument("--slug", required=True)
    ap.add_argument("--title", required=True)
    ap.add_argument("--authors", default="")
    ap.add_argument("--team", default="")
    ap.add_argument("--arxiv", default="")
    ap.add_argument("--code", default="")
    ap.add_argument("--date", default=dt.date.today().isoformat())
    ap.add_argument("--published", default="")
    ap.add_argument("--tldr", default="")
    ap.add_argument("--tags", default="")
    ap.add_argument("--path", default="")
    args = ap.parse_args()

    path = args.path or f"papers/{args.slug}/index.html"
    tags = [t.strip() for t in args.tags.split(",") if t.strip()]

    entry = {
        "slug": args.slug,
        "title": args.title,
        "authors": args.authors,
        "team": args.team,
        "arxiv": args.arxiv,
        "code": args.code,
        "date": args.date,
        "published": args.published,
        "tldr": args.tldr,
        "tags": tags,
        "path": path,
    }

    data = []
    if os.path.exists(args.papers_json):
        try:
            with open(args.papers_json, encoding="utf-8") as fh:
                txt = fh.read().strip()
                data = json.loads(txt) if txt else []
        except json.JSONDecodeError as e:
            sys.exit(f"ERROR: {args.papers_json} is not valid JSON: {e}")
    if not isinstance(data, list):
        sys.exit(f"ERROR: {args.papers_json} must contain a JSON array")

    # upsert by slug
    replaced = False
    for i, item in enumerate(data):
        if isinstance(item, dict) and item.get("slug") == args.slug:
            data[i] = entry
            replaced = True
            break
    if not replaced:
        data.append(entry)

    # newest first; entries without a date sink to the bottom
    data.sort(key=lambda d: d.get("date", ""), reverse=True)

    with open(args.papers_json, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)
        fh.write("\n")

    print(f"{'updated' if replaced else 'added'} '{args.slug}' "
          f"({len(data)} total) in {args.papers_json}")


if __name__ == "__main__":
    main()
