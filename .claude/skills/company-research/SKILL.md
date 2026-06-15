---
name: company-research
description: >-
  Research ONE company and publish a self-contained HTML 调研 (in 中文) focused on its
  COMPETITIVE LANDSCAPE, how EARLY/CROWDED its market is, and BORROWABLE STARTUP IDEAS.
  Use whenever the user hands over a company name or website and wants 调研/研究/competitive
  landscape/"这家公司是干嘛的、有哪些竞品、赛道格局、是不是早期、有没有可借鉴的 idea". The note
  covers: one-line positioning + market; a market map + an explicit EARLINESS verdict
  (nascent/emerging/crowded/mature); a competitor comparison MATRIX; a positioning chart;
  a FUNDING TIMELINE; a compact company snapshot (what/product/team); and an IDEA-SCOUTING
  section (whitespace, unmet needs, why-now, borrowable patterns, risks). Every fact is
  tagged by source grade (🟢 first-party / 🟡 secondary / 🔴 self-claimed/unverified).
  It commits the note to this repo (papers/<slug>/) and returns a click-to-view link.
---

# company-research

Turn a single company into a polished, self-contained HTML 调研 note aimed at **idea scouting**:
判断这家公司所在**赛道是否早期、拥挤度如何**，并提炼**可借鉴的创业 idea / whitespace**。重心是
**竞争格局**，不是单纯的公司简介。

**输出语言 — 中文散文，术语保留英文**（`agent`、`benchmark`、`MoE`、`SaaS`、`open-source`、
`moat`、`whitespace`、`GTM`、`seed/Series A` 等；公司/产品/投资机构专名一律英文）。

---

## ⛔ Non-negotiable rules

1. **来源分级是这个 skill 的灵魂。** 公司信息满是营销口径——**每条关键事实都标来源等级**：
   🟢 **一手**（官网 / SEC / 招股书 / 官方 newsroom / 创始人公开发言）、
   🟡 **二手**（媒体报道 / 融资数据库 / 分析师）、
   🔴 **自述 / 未证实**（市场宣传、未经独立验证的能力或客户声明）。
   竞品的指标尤其危险（口径不一、benchmark 樱桃挑选）——标清「谁的口径 / 什么时间」，
   差异大就并列，**不替对手美化、也不替目标公司注水**。
2. **Verify, don't fabricate.** 只写核实过的链接 / 数字 / 客户 / 融资。没核到就标🔴或写「未披露/未找到」。
   数字打架（融资额 / 估值 / 员工数）→ 全列 + 标来源，**不擅自取一个**。
3. **Self-contained output.** 一个 `papers/<slug>/index.html`，**inline CSS**，图（若有）放 `figures/`。
   定位图 / 融资 timeline 优先用**内联 `<svg>` 自绘**（注明「本调研重绘」），不要盗用版权图。
4. **不读其它解读。** 只依据对目标公司的检索；唯一共享文件是 `papers.json`，且只经 `index_add.py`。
5. **诚实于阶段。** 早期 / stealth 公司信息少 → 明确写「能核实的只有团队 + 方向，产品实效未验证」。

---

## Inputs

用户给：一个**公司名**或**官网域名**（可能附「有哪些竞品 / 赛道格局 / 是不是早期 / 有没有 idea 可借鉴」）。
先**消歧**（重名公司很多）：确认 canonical 官网与所指主体。

---

## Workflow

`$REPO = $(git rev-parse --show-toplevel)`；复用 paper-reading 的脚本：`$SKILL_PR="$REPO/.claude/skills/paper-reading"`。

### 0. 决定 slug 与赛道
- slug = `YYYY-MM-DD-<company-kebab>`（如 `2026-06-15-unreasonable-labs`）。
- 一句话确定它属于**哪个 category / 赛道**——这是后续找竞品、判早期度的锚。

### 1. 多源 fan-out（并行搜，尽量一手）
- **官网**：about / 产品 / 团队·careers / news / pricing / customers。
- **融资**：新闻稿 + Crunchbase/PitchBook 口径（走报道）；记录**每一轮**（日期、金额、轮次、领投/跟投）。
- **团队**：创始人背景（LinkedIn / 过往公司 / 论文）——深科技公司的 research 血统很关键。
- **竞品 & 赛道**：搜「<category> companies / alternatives / vs / landscape / market map」。
- **深科技额外**：GitHub / HuggingFace / arXiv（开源、论文、专利）。

### 2. 界定竞品集（最容易做歪，务必做对）
- 别只抄公司**自己宣称**的对手；找「**用户真会拿来二选一**」的。
- 三类都要：**直接竞品**（同产品同客户）/ **替代品**（不同形态解决同需求）/ **上下游**（可能向你这层渗透）。
- **强制覆盖四象限**：现有巨头 / 垂直创业公司 / 大厂顺手做 / 开源免费方案——漏掉最大威胁往往就在后两类。

### 3. 选对比维度（MECE 且决定性）
从「维度库」按行业挑 **5–8 个**最能拉开差距的：
> 产品形态 · 技术路线 · 目标客户 · 商业模式 · 开源/闭源 · 规模&融资 · 关键硬指标(benchmark/性能/价格) · 生态绑定 · 上市/独立性 · 数据/壁垒来源
（默认通用集 + 行业覆写：AI/模型偏「技术路线·开源·硬指标·算力」；SaaS 偏「客户·定价·GTM·留存」；硬件偏「规格·量产·供应链」；生物偏「靶点/管线·临床阶段·监管」。）

### 4. 判断赛道「早期度」（核心增值之一）
给一个明确档位 + 信号：**nascent（萌芽，几乎没人做）/ emerging（新兴，少数创业公司、巨头未进）/
crowded（拥挤，玩家多、同质化）/ mature（成熟，巨头主导）**。判断信号：
玩家数量与新增速度、融资热度与轮次分布、**巨头是否进场**、**开源/免费替代是否存在**、客户认知是否成型、是否有公认 benchmark/标准。

### 5. 提炼可借鉴的创业 idea（核心增值之二，对齐用户目标）
- **whitespace / 空白**：矩阵里没人占的格子、被忽视的客户细分或场景。
- **unmet needs / 痛点**：现有玩家共同的短板（从差评、缺失功能、价格痛点找）。
- **why now**：为什么这个赛道现在值得做（技术拐点 / 成本下降 / 政策 / 新需求）。
- **borrowable patterns**：目标公司哪些打法/切入点可迁移到别处。
- **adjacent ideas**：相邻赛道、上下游、垂直化、换商业模式的衍生机会。
- **风险**：拥挤度、巨头碾压、开源免费、监管等——诚实给。

### 6. 写 HTML
- 复制模板：`cp "$REPO/.claude/skills/company-research/templates/company.html" "$REPO/papers/<slug>/index.html"`。
- 填满每节，处理每个 `{{...}}` 与 `<!-- 填写 -->`，删多余示例行。**定位图与融资 timeline 用内联 SVG。**
- 每条关键事实加来源等级 badge（模板已带 `.src-a/.src-b/.src-c` 样式与 legend）。

### 7. 注册索引（复用脚本）
```bash
python3 "$SKILL_PR/scripts/index_add.py" "$REPO/papers.json" \
  --slug "<slug>" --title "<公司名>：竞争格局与赛道早期度调研" --authors "—" \
  --team "公司调研" --arxiv "<官网 URL>" --code "" \
  --tldr "<一句话：它干嘛 + 赛道早期度 + 一个可借鉴点>" \
  --tags "company,competitive-landscape,market-map,startup-idea,<行业tag>" \
  --date "$(date +%F)" --published "公司调研 $(date +%Y)"
```

### 8. 发布（遵守 CLAUDE.md：制作发布放后台）
```bash
cd "$REPO" && git add -A
git commit -m "Add 调研: <公司名> 竞争格局与早期度"
# 推 main，non-fast-forward 时 fetch→rebase（papers.json 冲突保留两边条目，勿 checkout --ours/--theirs）→ push；网络错误退避 2s/4s/8s/16s
```
回报：raw.githack（SHA 固定）或 GitHub Pages 链接 + 2–3 句话（它干嘛 / 赛道多早 / 一个可借鉴 idea）。

---

## 报告骨架（竞争格局 + idea 向）

1. **一句话定位 + 赛道**
2. **① 赛道地图 + 早期度判断**（玩家分群四象限 + nascent/emerging/crowded/mature 的明确 verdict 与信号）
3. **② 竞品对照矩阵**（5–8 维 × N 竞品，每格带来源等级；目标公司一列加粗）
4. **③ 定位图**（内联 SVG 2 轴象限，并标出 whitespace 空位；轴从预设里选：开源↔闭源 / 通用↔垂直 / 自建↔集成 / 低价↔高端 等）
5. **④ 融资 timeline**（目标公司逐轮 SVG 时间线 + 明细表；可附「赛道整体融资热度」一句）
6. **⑤ 公司速览**（what / 产品 / 团队 / 商业模式——压缩）
7. **⑥ 创业 idea 借鉴**（whitespace / unmet needs / why-now / borrowable / adjacent / 风险）
8. **⑤现实判断 + 存疑**（目标公司在格局里的胜算与软肋；来源分级提醒）

---

## Conventions
- slug：`YYYY-MM-DD-<company-kebab>`。重复同名公司加后缀区分。
- 同一 `papers.json`，公司条目与论文混排（`--published` 写「公司调研 YYYY」便于区分）。
- 标题里点明「竞争格局 / 赛道」以示这是 company-research 而非 paper。

## Fallbacks
- **早期/stealth**：信息少 → 早期度大概率判 nascent/emerging，并标「产品实效未验证」。
- **官网 JS 渲染 / 付费墙**：抓不到就退二手报道，标🟡/🔴。
- **赛道太新没竞品**：列最接近的替代方案 + 标「尚无直接竞品」（这本身就是「早期」的强信号，且是 idea 机会）。
- **target 跨多赛道**：选主赛道，或分赛道各出一张矩阵。
- **信息不对称**（开源透明 vs 闭源黑箱）：矩阵标「闭源未披露」，别用空白冒充劣势。
- 资源被网络策略挡：写「受网络策略限制未能核实」，用已有信息继续，绝不编。
