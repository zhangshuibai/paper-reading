#!/usr/bin/env python3
"""render_figures.py — turn a paper's PDF into web-ready figure PNGs.

Self-contained: depends only on PyMuPDF (`fitz`) and Pillow, both installable
with `pip install pymupdf pillow` (no system packages required). Use this when
the original arXiv source does not ship web-ready raster figures, or when you
want a clean crop of a figure straight from the typeset PDF.

Subcommands
-----------
  dims   <pdf>                                  list page count + page sizes (pts)
  page   <pdf> <page> <out.png> [--dpi 200]     render a whole page
  clip   <pdf> <page> <x0> <y0> <x1> <y1> <out.png> [--dpi 200]
                                                render a rectangle of a page
                                                (coords are PDF points; see dims)
  images <pdf> <outdir> [--min 10000]           dump embedded raster images
                                                (bytes >= --min) as p<page>_<i>.<ext>
  fig    <fig.pdf> <out.png> [--dpi 300]        render a standalone PDF/figure file

Pages are 1-indexed. PDF points are 1/72 inch; a US-letter page is 612x792.
"""
import argparse
import os
import sys


def _need_fitz():
    try:
        import fitz  # noqa: F401
        return fitz
    except Exception:
        sys.exit("PyMuPDF is required. Run:  pip install --quiet pymupdf pillow")


def cmd_dims(args):
    fitz = _need_fitz()
    doc = fitz.open(args.pdf)
    print(f"pages: {doc.page_count}")
    for i in range(doc.page_count):
        r = doc[i].rect
        print(f"  page {i+1}: {r.width:.0f} x {r.height:.0f} pts")


def cmd_page(args):
    fitz = _need_fitz()
    doc = fitz.open(args.pdf)
    page = doc[args.page - 1]
    zoom = args.dpi / 72.0
    pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), alpha=False)
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    pix.save(args.out)
    print(f"wrote {args.out} ({pix.width}x{pix.height}px @ {args.dpi}dpi)")


def cmd_clip(args):
    fitz = _need_fitz()
    doc = fitz.open(args.pdf)
    page = doc[args.page - 1]
    zoom = args.dpi / 72.0
    rect = fitz.Rect(args.x0, args.y0, args.x1, args.y1)
    pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), clip=rect, alpha=False)
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    pix.save(args.out)
    print(f"wrote {args.out} ({pix.width}x{pix.height}px @ {args.dpi}dpi)")


def cmd_images(args):
    fitz = _need_fitz()
    doc = fitz.open(args.pdf)
    os.makedirs(args.outdir, exist_ok=True)
    n = 0
    for pno in range(doc.page_count):
        for idx, info in enumerate(doc[pno].get_images(full=True)):
            xref = info[0]
            base = doc.extract_image(xref)
            data = base["image"]
            if len(data) < args.min:
                continue
            ext = base.get("ext", "png")
            out = os.path.join(args.outdir, f"p{pno+1}_{idx}.{ext}")
            with open(out, "wb") as fh:
                fh.write(data)
            print(f"  {out}  ({len(data)} bytes, {base.get('width')}x{base.get('height')})")
            n += 1
    print(f"extracted {n} image(s) >= {args.min} bytes into {args.outdir}")


def cmd_fig(args):
    fitz = _need_fitz()
    doc = fitz.open(args.fig)
    page = doc[0]
    zoom = args.dpi / 72.0
    pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), alpha=False)
    os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    pix.save(args.out)
    print(f"wrote {args.out} ({pix.width}x{pix.height}px @ {args.dpi}dpi)")


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("dims"); s.add_argument("pdf"); s.set_defaults(fn=cmd_dims)

    s = sub.add_parser("page")
    s.add_argument("pdf"); s.add_argument("page", type=int); s.add_argument("out")
    s.add_argument("--dpi", type=int, default=200); s.set_defaults(fn=cmd_page)

    s = sub.add_parser("clip")
    s.add_argument("pdf"); s.add_argument("page", type=int)
    s.add_argument("x0", type=float); s.add_argument("y0", type=float)
    s.add_argument("x1", type=float); s.add_argument("y1", type=float)
    s.add_argument("out"); s.add_argument("--dpi", type=int, default=200)
    s.set_defaults(fn=cmd_clip)

    s = sub.add_parser("images")
    s.add_argument("pdf"); s.add_argument("outdir")
    s.add_argument("--min", type=int, default=10000); s.set_defaults(fn=cmd_images)

    s = sub.add_parser("fig")
    s.add_argument("fig"); s.add_argument("out")
    s.add_argument("--dpi", type=int, default=300); s.set_defaults(fn=cmd_fig)

    args = p.parse_args()
    args.fn(args)


if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError:
        # tolerate `... | head` closing the pipe early
        try:
            sys.stdout.close()
        except Exception:
            pass
