---
name: stock-research
description: >-
  Research ONE publicly-traded company (a stock) and publish a self-contained HTML 股票调研
  (in 中文) aimed at an INVESTMENT DECISION: should I buy / hold / avoid this stock. Use
  whenever the user hands over a ticker or listed company and wants 股票调研/投资分析/估值/
  财报分析/"这只股票值不值得买、基本面如何、竞争对手是谁、财务健康吗、贵不贵". The note
  covers: a clear investment rating + thesis; mission/vision & business model (how it makes
  money); industry & competitors (comparison MATRIX + market position); a FINANCIAL HEALTH
  check (income statement / balance sheet / cash flow key lines + trends + ratios, or for
  pre-revenue names: cash runway / burn / dilution / milestones); VALUATION (multiples vs
  peers + bull/base/bear scenario target ranges); an explicit BULL vs BEAR thesis; CATALYSTS
  & timeline; RISK FACTORS (from 10-K/10-Q); ownership / insiders / institutions / short
  interest; and a final BUY/HOLD/AVOID verdict with what would change the thesis. Every
  figure is tagged by source grade (🟢 SEC/IR first-party / 🟡 analyst/media secondary /
  🔴 management-guidance/unverified). NOT financial advice — disclaimer is mandatory.
  It commits the note to this repo (papers/<slug>/) and returns a click-to-view link.
---

# stock-research

把一只**已上市股票**做成一篇打磨过、自包含的中文 HTML 调研，落点是**投资决策**：
判断**该不该买入 / 持有 / 回避**，并说清**为什么、什么会推翻这个判断**。重心是
**基本面 + 估值 + 多空论点**，不是泛泛的公司简介。

**⚠️ 这不是投资建议（not financial advice）。** 每篇必须带免责声明：本调研仅为公开信息的梳理与分析，
不构成任何买卖要约或投资建议；作者不对依据本文做出的决策负责；投资有风险，请自行核实并独立判断。

**输出语言 — 中文散文，术语保留英文**（`ticker`、`P/E`、`EV/Sales`、`FCF`、`guidance`、`moat`、
`TAM`、`dilution`、`runway`、`short interest`、`10-K/10-Q/8-K`、`bull/bear` 等；公司/产品/机构专名英文）。

---

## ⛔ Non-negotiable rules

1. **来源分级是这个 skill 的灵魂。** 财务与市场信息满是口径差异和管理层叙事——**每条关键数字都标来源等级**：
   🟢 **一手**（SEC 申报：10-K / 10-Q / 8-K / S-1 / proxy；公司 IR / earnings call / press release；交易所披露）、
   🟡 **二手**（卖方分析师 / 媒体 / 数据终端 estimates / Macrotrends 等）、
   🔴 **管理层指引 / 自述 / 未证实**（guidance、TAM 宣称、未经独立验证的运营指标、网络传闻）。
   尤其当心：**non-GAAP vs GAAP**、**财年口径**、**adjusted EBITDA**、**bookings vs revenue**、**TAM 注水**。
2. **Verify, don't fabricate.** 只写**核实过**的数字 / 日期 / 申报。数字打架（营收/EPS/现金/股本/估值）→ **全列 + 标口径与期间**，
   绝不擅自取一个、绝不编。核不到就写「未披露 / 未找到」。引用财报数字优先回到**SEC 原文**而非二手摘要。
3. **不预测股价、不给虚假精度。** 估值给**情景区间（bull / base / bear）+ 明确假设**，而不是单点目标价；
   说清「在什么假设下值多少」，并强调假设的不确定性。
4. **多空都要硬。** Bull thesis 和 Bear thesis **都要写到最强版本**，不替自己偏好的一方注水、也不替另一方稻草人。
5. **诚实于阶段。** Pre-revenue / story stock（如卫星、生物科技、早期硬科技）→ 重点转向**现金 runway、烧钱速度、
   摊薄、里程碑兑现概率、融资依赖**，明确写「估值靠叙事、基本面未兑现」。
6. **Self-contained output.** 一个 `papers/<slug>/index.html`，**inline CSS**，图用**内联 `<svg>` 自绘**
   （营收/现金/股本趋势、估值情景、催化剂 timeline），注明「本调研重绘」，不盗版权图。

---

## Inputs

用户给：一个 **ticker** 或**上市公司名**（可能附「值不值得买 / 财报如何 / 竞争对手 / 贵不贵 / 风险」）。
先**消歧**：确认交易所与代码（如 `ASTS` = AST SpaceMobile, NASDAQ；注意 ADR、双重上市、同名公司）。

---

## Workflow

`$REPO = $(git rev-parse --show-toplevel)`；复用 paper-reading 的脚本：`$SKILL_PR="$REPO/.claude/skills/paper-reading"`。

### 0. 定 slug 与画像
- slug = `YYYY-MM-DD-<ticker-lower>`（如 `2026-06-17-asts`）。
- 一句话定位：哪个行业 / 处在什么阶段（pre-revenue 叙事股？成长股？价值股？周期股？）——决定后面分析的重心。

### 1. 多源 fan-out（尽量回到一手 SEC / IR）
- **申报**：最新 10-K（年报）、最近几个 10-Q（季报）、近期 8-K（重大事件）、S-1/招股书（次新股）、DEF 14A（proxy，薪酬/股权）。
- **业绩**：最近 4–8 个季度的 revenue / 毛利 / 经营利润 / 净利 / EPS / 经营现金流 / FCF / 现金与债务 / 股本（稀释股数）。
- **指引与电话会**：management guidance、earnings call 要点（标🔴/🟡）。
- **竞争与行业**：竞品财务对照、市场份额、TAM/SAM（TAM 宣称标🔴）。
- **持仓与情绪**：机构持股、内部人买卖、**short interest**、近期融资 / ATM / 可转债 / warrant（摊薄来源）。

### 2. 财务体检（核心增值之一）
按公司阶段选重点：
- **有营收公司**：增长（YoY/QoQ）、毛利率/经营利润率趋势、净利与 EPS、经营现金流与 **FCF**、资产负债（现金、债务、净现金/净负债）、关键比率（毛利率、营业利润率、ROE/ROIC、负债率、current ratio、Rule of 40 适用时）。
- **Pre-revenue / 烧钱公司**：**cash runway**（现金 ÷ 季度净烧钱）、burn rate 趋势、累计赤字、**摊薄**（股本逐年/逐季膨胀、warrant/期权/可转债）、capex 与产能里程碑、对外部融资的依赖。
- 三表关键行用**内联 SVG 折线/柱状**画趋势（营收、现金、稀释股数 至少各一）。

### 3. 行业与竞争对手（竞品对照矩阵）
选 5–8 个**决定性维度**，对照直接竞品 + 替代品 + 上下游巨头；目标公司一列加粗。
维度按行业挑：规模&营收 · 增长 · 盈利能力 · 资产负债健康 · 技术/产品壁垒 · 市占率/卡位 · 估值倍数 · 监管/牌照。
每格尽量带来源等级；信息不对称处标「未披露」而非空白冒充。

### 4. 估值（核心增值之二，给区间不给单点）
- **倍数法**：P/E、P/S、EV/Sales、EV/EBITDA、P/B、P/FCF——与**同业**和**自身历史**对比，说清用 forward 还是 trailing、GAAP 还是 adjusted。
- **情景法**：bull / base / bear 三档，**写清每档的关键假设**（收入兑现、利润率、摊薄、折现率/倍数），给市值或每股价值**区间**。
- pre-revenue 用「里程碑兑现 × 终局 TAM 渗透 × 摊薄后股数」的粗框架，强调对假设极度敏感。

### 5. 多空论点（都写到最强）
- **Bull thesis**：最有说服力的看多逻辑（TAM、卡位、技术领先、拐点、催化剂）。
- **Bear thesis**：最致命的看空逻辑（摊薄、执行风险、竞争、监管、现金枯竭、估值透支、会计红旗）。
- **催化剂 & timeline**：未来 6–24 个月可验证的节点（财报、产品/发射/审批、融资、解禁），内联 SVG 时间线。

### 6. 风险因素
从 10-K/10-Q「Risk Factors」与现金/摊薄/竞争/监管/客户集中/诉讼/关键人/地缘等提炼**真正重要的**（别照抄全清单），各标来源。

### 7. 投资判断（明确结论）
给一个**明确档位**：**买入(Buy) / 增持(Accumulate) / 持有(Hold) / 减持(Reduce) / 回避(Avoid)**，并写：
适合什么**风险偏好**与**时间维度**、关键**前提假设**、**什么信号会推翻论点**（thesis-breaker）。不喊单、不给虚假确定性。

### 8. 写 HTML
- 复制模板：`cp "$REPO/.claude/skills/stock-research/templates/stock.html" "$REPO/papers/<slug>/index.html"`。
- 填满每节，处理每个 `{{...}}` 与 `<!-- 填写 -->`，删多余示例行。**趋势图/估值情景/催化剂 timeline 用内联 SVG。**
- 每条关键数字加来源等级 badge（模板已带 `.src-a/.src-b/.src-c` 与 legend）。**免责声明区块不得删。**

### 9. 注册索引（复用脚本）
```bash
python3 "$SKILL_PR/scripts/index_add.py" "$REPO/papers.json" \
  --slug "<slug>" --title "<公司名>（<TICKER>）：基本面 / 估值 / 是否值得买入" --authors "—" \
  --team "股票调研" --arxiv "<IR 或 SEC EDGAR URL>" --code "" \
  --tldr "<一句话：它干嘛 + 评级档位 + 最关键的多空点>" \
  --tags "stock,equity-research,valuation,<行业tag>" \
  --date "$(date +%F)" --published "股票调研 $(date +%Y)"
```
（注：`--published "股票调研 YYYY"` 用于和论文/公司调研区分；默认**不**进首页「公司调研·中国创业机会」置顶组。）

### 10. 发布（遵守 CLAUDE.md：制作发布放后台）
```bash
cd "$REPO" && git add -A
git commit -m "Add 股票调研: <公司名> <TICKER> 基本面与估值"
# 推 main，non-fast-forward 时 fetch→rebase（papers.json 冲突用 python 合并保留两边条目，勿 checkout --ours/--theirs）→ push；网络错误退避 2s/4s/8s/16s
```
回报：raw.githack（SHA 固定）或 GitHub Pages 链接 + 2–3 句话（它干嘛 / 评级 / 最关键的一个多空点）+ **重申非投资建议**。

---

## 报告骨架（投资决策向）

1. **投资速览 + 评级**（一句话评级 Buy/Hold/Avoid + 情景目标区间 + 最关键支撑与最致命风险）
2. **① 公司是什么**（mission / vision / 业务模式：怎么赚钱、谁付费、单位经济）
3. **② 行业与竞争对手**（竞品对照矩阵 5–8 维 + 市场卡位）
4. **③ 财务体检**（三表关键行 + 趋势 SVG + 关键比率；pre-revenue 则 runway/burn/摊薄）
5. **④ 估值**（倍数 vs 同业/历史 + bull/base/bear 情景区间 + 假设）
6. **⑤ 多空论点**（Bull thesis vs Bear thesis，都写到最强）
7. **⑥ 催化剂 & timeline**（未来可验证节点，内联 SVG）
8. **⑦ 风险因素**（10-K 提炼，按重要性，不照抄）
9. **⑧ 股权 / 内部人 / 机构 / short interest**
10. **⑨ 投资判断**（明确档位 + 适合谁 + thesis-breaker）
11. **免责声明 + 出处**

---

## Conventions
- slug：`YYYY-MM-DD-<ticker-lower>`；同名/多上市地加后缀（如 `-adr`、`-hk`）。
- 同一 `papers.json`，股票条目与论文/公司调研混排（`--published` 写「股票调研 YYYY」便于区分）。
- 标题里点明 ticker 与「是否值得买入 / 基本面 / 估值」以示这是 stock-research。

## Fallbacks
- **次新股 / SPAC 上市**：财报历史短 → 重点看 S-1/招股书、PIPE、warrant、解禁与摊薄。
- **Pre-revenue 叙事股**：基本面未兑现 → 主线改为 runway / 烧钱 / 里程碑兑现概率 / 摊薄；明确「估值靠故事」。
- **数字打架**（GAAP vs non-GAAP、不同终端 estimates）：全列 + 标口径，绝不取一个。
- **财报刚发 / 静默期**：标注「截至 <日期> 最新可得」，别用过时数据冒充最新。
- **做空报告 / 多头小作文**：标🔴并交叉验证，既不照单全收也不无视。
- 资源被网络策略挡：写「受网络策略限制未能核实」，用已核信息继续，绝不编。

## ⚠️ 免责声明（每篇必带，不得删）
本调研为公开信息的整理与分析，**不构成投资建议**，不构成任何证券买卖的要约或招揽。所有数据可能有误或过时，
请以官方申报为准并自行独立核实。作者不持有相关持仓披露义务、亦不对依据本文做出的任何决策负责。投资有风险，入市需谨慎。
