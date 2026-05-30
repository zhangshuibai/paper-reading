#!/usr/bin/env bash
# fetch_arxiv.sh — download an arXiv paper's PDF (+ LaTeX source) into a working dir.
#
# Usage:
#   fetch_arxiv.sh <arxiv_id_or_url> <workdir>
#
# Examples:
#   fetch_arxiv.sh 1706.03762 /tmp/paper-reading/attn
#   fetch_arxiv.sh https://arxiv.org/abs/2501.01234 /tmp/paper-reading/foo
#
# Produces inside <workdir>:
#   paper.pdf            the article PDF (used for reading + figure rendering)
#   source.tar.gz        the e-print source tarball (if available)
#   source/              extracted source (contains original figure files)
# and prints the normalized arXiv id plus a list of candidate figure files.
set -euo pipefail

raw="${1:?usage: fetch_arxiv.sh <arxiv_id_or_url> <workdir>}"
workdir="${2:?usage: fetch_arxiv.sh <arxiv_id_or_url> <workdir>}"

# --- normalize the arXiv id -------------------------------------------------
# Handles: bare id (2501.01234 / 2501.01234v2), abs/pdf URLs, old-style ids
# (hep-th/9901001), and trailing .pdf.
id="$raw"
id="${id#http://}"; id="${id#https://}"
id="${id#arxiv.org/}"; id="${id#www.arxiv.org/}"
id="${id#abs/}"; id="${id#pdf/}"
id="${id%.pdf}"

if [[ ! "$id" =~ ^([a-z-]+/[0-9]{7}|[0-9]{4}\.[0-9]{4,5})(v[0-9]+)?$ ]]; then
  echo "WARN: '$raw' did not look like a clean arXiv id; using '$id' as-is." >&2
fi

mkdir -p "$workdir"

echo ">> arXiv id: $id"
echo ">> workdir : $workdir"

# --- download PDF -----------------------------------------------------------
echo ">> downloading PDF ..."
curl -fSL --retry 4 --retry-delay 2 --max-time 180 \
  -o "$workdir/paper.pdf" "https://arxiv.org/pdf/$id" \
  || { echo "ERROR: failed to download PDF for $id" >&2; exit 1; }
echo "   saved $workdir/paper.pdf ($(du -h "$workdir/paper.pdf" | cut -f1))"

# --- download + extract LaTeX source (best source of original figures) ------
echo ">> downloading e-print source ..."
if curl -fSL --retry 4 --retry-delay 2 --max-time 180 \
      -o "$workdir/source.tar.gz" "https://arxiv.org/e-print/$id"; then
  mkdir -p "$workdir/source"
  if tar -xzf "$workdir/source.tar.gz" -C "$workdir/source" 2>/dev/null; then
    echo "   extracted source into $workdir/source"
  else
    # Some e-print payloads are a single gzipped .tex, not a tarball.
    echo "   note: source is not a tarball; leaving source.tar.gz as-is" >&2
  fi
else
  echo "   note: no e-print source available for $id (continuing with PDF only)" >&2
fi

# --- list candidate figure files -------------------------------------------
echo ">> candidate figure files in source/:"
if [[ -d "$workdir/source" ]]; then
  find "$workdir/source" -type f \
    \( -iname '*.png' -o -iname '*.jpg' -o -iname '*.jpeg' \
       -o -iname '*.pdf' -o -iname '*.eps' -o -iname '*.svg' -o -iname '*.gif' \) \
    -printf '   %s\t%p\n' 2>/dev/null | sort -rn | head -60 || true
else
  echo "   (none — no source extracted)"
fi

echo ">> done. id=$id"
