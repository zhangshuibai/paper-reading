---
name: paper-reading
description: >-
  Download, deeply read, and publish a rich self-contained HTML 解读 (interpretation)
  of ONE research paper, given a title, an arXiv link/ID, or any paper URL/PDF.
  Use whenever the user hands over a paper and wants it 解读/精读/总结/分析/"帮我读一下"
  /"download and explain this paper". The note (written in 中文) covers: title/authors/
  team/link + what is actually open-sourced (code, weights, datasets, envs, benchmarks
  with verified links), motivation & contributions, the method (with original or rebuilt
  figures), the evaluation (benchmarks, metrics, gains), and the key insights. It commits
  the note to this repo and returns a click-to-view link. Each paper is read in ISOLATION —
  never influenced by other papers already in the repo.
---

# paper-reading

Turn a single paper into a polished, self-contained HTML reading note, publish it to this
repo, and hand the user a viewable link.

This skill lives in `zhangshuibai/paper-reading`. Be thorough — the user explicitly wants
*detailed* readings, not a one-paragraph abstract.

**Output language — 中文 散文，术语保留英文。** 解读的叙述/解释全部用中文，但**不要把已经约定俗成的
技术名词和专有名词翻译成中文** —— 保留研究者口头实际会说的英文形式。例如：`agent`（不要写「智能体」）、
`token`（不要「词元」）、`prompt`、`policy`、`reward shaping`、`embedding`、`benchmark`、`baseline`、
`attention`、`fine-tune`、`RL/RLHF`，以及所有模型 / 方法 / 数据集 / 机构的专名，一律保持英文；只翻译那些
本来就常用中文表达的普通词。判断准则：如果同行平时直接讲那个英文词，就保留英文，不要硬翻。标题和正文是中文，
但其中内嵌的术语名词维持英文原文。

---

## ⛔ Non-negotiable rules

1. **Read each paper in isolation.** Base the interpretation ONLY on the target paper itself
   and its *official* artifacts (the PDF, its abstract page, its real GitHub repo / Hugging
   Face / project page). **Never open, read, grep, list, or imitate any existing file under
   `papers/`** (other notes) — they must not influence this note's content, wording, or
   conclusions. The template in `templates/paper.html` is the only style reference.
   - The *only* shared file you touch is `papers.json`, and only via `scripts/index_add.py`,
     which edits metadata for you so you never read other entries' content.
2. **Self-contained output.** Each note is one `papers/<slug>/index.html` with **inline CSS**
   and **local figures** under `papers/<slug>/figures/`. It must render on its own. The only
   external refs allowed: the `../../index.html` back-link and the MathJax CDN (for formulas).
3. **Verify, don't fabricate.** Only list open-source artifacts / links you actually
   confirmed exist, and only report numbers that are in the paper. If something is unclear or
   not released, say so plainly (e.g. "代码声称将开源，截至解读日未见仓库").
4. **Work outside the repo.** Do all downloading/extraction in `/tmp/paper-reading/<slug>/`.
   Only the final `index.html` + chosen figures (+ the `papers.json` entry) land in the repo.

---

## Inputs

The user gives one of:
- an **arXiv** id or URL (`2501.01234`, `arxiv.org/abs/...`, `/pdf/...`) — best case;
- a **title** — find it on the web (prefer the arXiv/abs page), confirm authors match;
- any other **URL or PDF** (OpenReview, ACL Anthology, a project page, a direct PDF) — fetch it.

---

## Workflow

Run these steps in order. `$REPO` = repo root, `$SKILL` = this skill's dir.

```bash
REPO="$(git rev-parse --show-toplevel)"
SKILL="$REPO/.claude/skills/paper-reading"
```

### 0. Setup (isolated)
- Decide a `slug` (see *Conventions*) and `WORK=/tmp/paper-reading/<slug>`; `mkdir -p "$WORK"`.
- Ensure figure deps once: `pip install --quiet pymupdf pillow` (already works in this env).

### 1. Resolve the paper
- From the input, determine: original **title**, a concise **中文标题**, **authors**, **team /
  affiliations** (lab / company), the **canonical link**, and **venue / year**.
- For a bare title: `WebSearch` it, open the arXiv abs page with `WebFetch`, confirm it's the
  right paper. If it's not on arXiv, use the real source (OpenReview/ACL/etc.).

### 2. Download
- arXiv: `bash "$SKILL/scripts/fetch_arxiv.sh" <id-or-url> "$WORK"`
  (gets `paper.pdf`, `source/` with original figure files, and lists figure candidates).
- Non-arXiv: `curl -fSL -o "$WORK/paper.pdf" "<pdf-url>"`.

### 3. Read it deeply
- Use the **Read tool on `$WORK/paper.pdf`** (use the `pages` argument; cover intro → method →
  experiments → appendix tables). The Read tool renders PDF pages, so you also *see* the figures.
- Extract: the real problem & prior-art pain points, the core idea, the method details
  (incl. equations & hyperparameters), the eval setup, the concrete result numbers, ablations,
  and the insights/limitations.

### 4. Verify open-source artifacts
Find and **confirm** what's actually released (distinguish released vs "coming soon" vs API-only):
- **Code:** the repo is usually linked on the paper's first page / footnote / abstract. Confirm
  with the GitHub MCP tools (`search_repositories`, `get_file_contents` on the README) or
  `WebFetch`. Note scope (training? inference? eval harness?) and **license**.
- **Weights / Datasets:** search `huggingface.co` (models & datasets); confirm they exist; note
  scale & license.
- **Environment / Benchmark / Demo / project page:** record real links.
- Build the artifacts table with these verified links; mark **✘** for anything not released.

### 5. Figures (key visuals)
Pick **1–4** figures that carry the most meaning (architecture/overview + a couple of key
result/analysis figures). Save into `$REPO/papers/<slug>/figures/`.
- **Prefer original web-ready files** from `$WORK/source/` (`.png/.jpg`): just copy them.
- **PDF/EPS figure file →** `python3 "$SKILL/scripts/render_figures.py" fig <file.pdf> <out.png> --dpi 300`
- **Crop/render from the paper PDF:** `render_figures.py dims paper.pdf`, then
  `... page <pdf> <p> <out.png> --dpi 200` or `... clip <pdf> <p> x0 y0 x1 y1 <out.png>`,
  or `... images <pdf> <outdir>` to dump embedded rasters.
- Always attribute the source in the `<figcaption>` (e.g. "原文 Figure 2"). If no good figure
  exists and a schematic would help, you may hand-build a small inline `<svg>`.

### 6. Write the note
- Copy the template: `cp "$SKILL/templates/paper.html" "$REPO/papers/<slug>/index.html"`.
- Fill **every** section in 中文 (散文用中文，技术术语如 `agent` 保留英文——见上文「Output language」)
  to the quality bar below. Replace all `{{PLACEHOLDERS}}`,
  act on every `<!-- 填写 -->` comment, then delete leftover guidance comments and unused
  template rows. Reference figures as `figures/xxx.png`. Use `$...$` / `$$...$$` for math.

### 7. Register in the index (metadata only)
```bash
python3 "$SKILL/scripts/index_add.py" "$REPO/papers.json" \
  --slug "<slug>" --title "<原始标题>" --authors "<作者>" --team "<机构>" \
  --arxiv "<链接>" --code "<代码链接|留空>" --tldr "<一句话>" \
  --tags "tag1,tag2" --date "$(date +%F)" --published "<venue/year>"
```

### 8. Publish
```bash
cd "$REPO" && git add -A
git commit -m "Add 解读: <短标题>"
git push -u origin "$(git rev-parse --abbrev-ref HEAD)"   # retry 2s/4s/8s/16s on network error
```
- Default to the repo's **`main`** branch so links stay stable. If your session restricts you
  to a working branch (e.g. Claude Code on web assigns a `claude/...` branch), push there
  instead and use the **commit-SHA** link form below (branch names containing `/` break
  raw.githack.com path parsing).

### 9. Hand the user the link
Compute `owner/repo` from `git remote get-url origin`. Then give a **click-to-view** link
(this repo is public, so these render the HTML directly):

- On `main`:  `https://raw.githack.com/<owner>/<repo>/main/papers/<slug>/index.html`
- On any branch (SHA-pinned, always safe):
  `https://raw.githack.com/<owner>/<repo>/<commit-sha>/papers/<slug>/index.html`
- If GitHub Pages is enabled (nicer URL): `https://<owner>.github.io/<repo>/papers/<slug>/`

Reply with the link + a 2–3 line summary of what the paper is. The index page
(`raw.githack.com/<owner>/<repo>/main/index.html` or the Pages root) lists all notes.

---

## Content quality bar (the user wants *detailed*)

- **① 开源贡献** — a verified table: code / weights / datasets / env·benchmark / demo, each with a
  real link and one line on scope + license; ✘ where not released. Lead with one summary sentence.
- **② 动机与贡献** — spell out the prior-art landscape and its concrete failure modes, the
  author's key observation/hypothesis, and an enumerated list of contributions (specific +
  quantified where possible).
- **③ 方法** — high-level pipeline first (with the overview figure), then each component/step
  with the math written out and every symbol explained in plain words + intuition; call out
  implementation details that matter for reproduction.
- **④ 实验评估** — benchmarks (what each tests), baselines, metric definitions (and direction),
  a results table with the paper's method bolded, an honest read of *how much* it helps and
  where it doesn't, plus the decisive ablation(s).
- **⑤ 洞见** — 1–3 transferable/counter-intuitive takeaways, the limitations & future work, and
  how it relates to prior work (from this paper's own framing — do **not** consult other notes).

---

## Conventions

- **slug:** arXiv → `<arxiv-id>-<short-kebab-title>` (e.g. `2501.01234-self-rewarding-llm`);
  non-arXiv → `<YYYY-MM-DD>-<short-kebab-title>`. Kebab = lowercase English title, alnum+`-`,
  ~5–6 words max.
- **Re-reading** an existing slug is an in-place update: regenerate the HTML fresh (don't read
  the old one) and re-run `index_add.py` (it upserts by slug).

## Fallbacks
- No arXiv `source/` (figures): render straight from `paper.pdf` with `render_figures.py`.
- `pip install` blocked: copy raster originals from `source/`; if a figure is PDF-only, link to
  the original figure or rebuild a minimal SVG — never block the whole note on one figure.
- A resource is blocked by the network policy: note it ("受网络策略限制未能核实") and proceed
  with what you have. Never invent links or numbers.
