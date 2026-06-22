---
name: serenity
description: >-
  Apply "Serenity's" AI / semiconductor SUPPLY-CHAIN BOTTLENECK lens to evaluate a stock,
  ticker, or sub-sector — hunt mispriced UPSTREAM single-source chokepoints that hyperscaler
  capex must flow through (ASIC → optical/CPO → substrate/InP → feedstock → power), where a
  small market cap is misaligned with downstream trillion-dollar spend. Use when the user is
  evaluating a semiconductor / AI-infra / optical / memory / power / neocloud name, asks
  "is this a real bottleneck", "trace the supply chain upstream", "find the chokepoint",
  "卖铲子的上游是谁", "这只票值不值得看 (供应链角度)", or "what would Serenity think". It applies a
  12-principle framework + a 14-question scoring checklist, classifies any X/news post type,
  and returns a structured bottleneck read with a CONVICTION tier, catalysts, thesis-breakers,
  and source-graded facts. It is a DECISION-SUPPORT LENS, NOT financial advice; it never places
  trades and never copies unverified track records. Pairs with the stock-research skill for a
  full one-pager. Distilled (methodology only) from Serenity (@aleabitoreddit) via the public
  repo yan-labs/serenity-aleabitoreddit.
---

# serenity

把 **Serenity（@aleabitoreddit）的「AI/半导体供应链 bottleneck」选股视角**做成一个可复用的 lens：
给定一个 ticker / 子赛道，**沿 hyperscaler capex 往上游追**，找「下游万亿支出、自己却小市值」的
**单点 chokepoint**，用一套 12 原则 + 14 题清单过筛，输出带 **conviction 档位 + 催化剂 + 证伪条件 +
来源分级** 的结构化判断。

**出处与边界**：方法论蒸馏自公开 repo `yan-labs/serenity-aleabitoreddit`（Serenity / @aleabitoreddit 的
供应链研究打包成的 agent skill）。本地 skill **只固化可迁移的方法论层**（principles / checklist / workflows /
risk framing），**不搬运**原 skill 里会过期的逐票 `theses`（~30 分钟即 stale、约两周重生成）和**未经验证的
自报战绩**（如 237% / 4502% YTD）。需要具体票的实时立场请回到原 repo 或一手数据。

**⚠️ 非投资建议（not financial advice）。** 这是 decision-support lens，**不下单、不喊单、不保证收益**；
用它「**问更好的问题，而不是抄作业**」。每篇分析必带免责声明。

---

## ⛔ Non-negotiable rules

1. **Verify, don't copy.** 原作者的战绩与逐票结论是**自报 + 事后视角 + 幸存者/选择偏差**——**绝不照搬当信号**。
   任何数字（营收/ARR/毛利/合同/市值/做空比例/IV）都要**回一手核实**（SEC 10-K/10-Q/8-K、IR、交易所），
   并按来源分级标注：🟢 一手 / 🟡 二手(分析师/媒体) / 🔴 自述/未证实(管理层 guidance、KOL 帖、TAM 宣称)。
2. **不混淆供应链层级。** 这是这套方法的灵魂红线：**substrate ≠ epiwafer ≠ foundry ≠ module ≠ system**。
   画链条时每一层谁控盘、占 BOM 多少、能不能被绕开，要分清楚，别把不同层的公司当同一个 bottleneck。
3. **给档位 + 给证伪条件。** 输出明确 conviction 档位，并写清「**什么信号会推翻这个判断（thesis-breaker）**」。
   不给虚假精度、不预测点位。
4. **诚实于偏差。** 这套 lens 偏好 <~$3B 微/小盘、日波动 20%+、可能用杠杆——**明确写出适用人群与归零风险**。
5. **时效。** 供应链格局变化快；标注「数据截至 <日期>」，别用过时结论冒充最新。

---

## 核心 edge（一句话）

> 别买最显眼的卖铲人（NVDA）。沿 hyperscaler capex 往上游追：
> **ASIC → 光模块/CPO transceiver → 衬底 substrate/InP → 外延片 epiwafer → 原料 feedstock → 电力/散热**，
> 找那个「buyers 不惜代价也要保供、占 BOM 比例小所以能吸收涨价」的**单点 chokepoint**，
> 趁它还小市值、机构还没定价时介入。

辅助 lens：**Mag7 客户集中度**、**签约 ARR vs 市值错配**、**GAAP 毛利战**、**稀释/ATM 筛雷**、**融资质量谱**。

---

## 12 条原则（详见 `references/methodology.md`）

1. **Bottleneck hunting（核心）** — 找单一/近单一来源、下游绕不开只能接受涨价的卡点。
2. **多跳 BOM / OSINT 供应链测绘** — 从 capex 画到 feedstock，看每层谁控盘。
3. **签约 ARR vs 市值错配** — 用锁定 take-or-pay 合同的前瞻 ARR 定价，而非 trailing 倍数。
4. **Mag7 客户集中度筛子** — 多个大厂同时是客户 = 需求耐久（配对手方质量）。
5. **GAAP 毛利战** — 只比审计后 GAAP 毛利，别被 cherry-pick 的 non-GAAP 误导。
6. **认证周期 vs TTM 营收** — 在 design-win / 晶圆认证期就进，趁业绩未体现。
7. **稀释/ATM 日历 = 否决项** — 大额 ATM + 高管股权激励 = 股价结构性天花板。
8. **融资质量谱** — 按对手方信用排序：NVDA 背书 > colo > ATM > 债务。
9. **逼空（盈利成长股变体）** — 高做空比例 + 基本面改善的盈利公司 = 上行异常。
10. **关税/宏观冲击 = 买点** — 算法砸盘但多年 capex 合同未受影响时进场。
11. **机构滞后 / flow 阅读** — 散户发现 chokepoint 通常领先机构建仓 4–6 周。
12. **Vega / IV 错价（期权）** — IV 仍按旧历史波动定价、但标的有结构性新波动源时，买长期 call。

**红旗 / 反模式**：纯技术分析无基本面催化；**混淆供应链层级**；把内部人卖出当方向信号；
基于 X/Reddit 情绪建仓；追已被抢跑的事件；只有头衔、缺供应链运营 fluency 的评论。

---

## 14 题打分清单（进场前自检，详见 references）

①真 bottleneck 有定价权？②在上游、占 BOM 比例小所以买家能吸收涨价？③能不混淆层级地画全链条？
④TAM 随 AI capex / physical-AI 扩张？⑤签约对手方 AAA 级可信？⑥GAAP 毛利撑得起质量定位？
⑦融资干净（无大额 ATM/SBC 悬顶）？⑧仍在放量前、被 TTM 营收错杀？⑨有带日期的具体催化剂、在可交易窗口内？
⑩市值够小（<~$3B）有机构重估空间？⑪机构覆盖仍滞后于供应链证据？⑫二元风险与仓位/工具（股票 vs 期权）匹配？
⑬是否明确持仓、还是探索性提及？⑭当前宏观（利率/关税/地缘）是助力还是阻力？

> 命中越多越强；任一红旗（尤其②层级混淆、⑦ATM 悬顶）出现要显著降档或否决。

---

## 4 个工作流（按用户问法选）

**(a) 单票评估** — ①画上游供应链、定位它在第几层；②跑 12 原则相关项 + 14 题清单；③回一手核实关键数字（标来源等级）；
④给 conviction 档位（Strongly Bullish / Bullish / Mixed / Cautious / Avoid）+ 催化剂（带日期）+ **thesis-breaker**；
⑤写风险框架（微盘/波动/杠杆/归零）。**只作分析框架，绝不当下单指令。**

**(b) 组合 / 自选审查** — 把标的分三桶：**Agreements**（符合 bottleneck lens 的）/ **Conflicts**（明显踩红旗的）/
**Gaps**（链条上高价值但你没覆盖的卡点），出优先级讨论清单。

**(c) 前瞻板块观点** — 抓主题线（CPO/光子、HBM/内存、neocloud 融资、电力/散热、InP/化合物半导体、机器人/physical AI），
拉出每层的卡点候选 + 领先指标，给观点 + 置信度 + **证伪条件**。

**(d) 新帖 / 新闻信号评估** — 先**分类**：新 bottleneck 论点 | 反复重申/抄底 | 供应商地图 | **victory lap 晒单**；
对历史类比；**把「市场窗口」和「股票论点」分开评**；转成纪律（watch 规则 / 限价阶梯）而非订单。
（典型信号滞后：公开论点到市场验证约 **5–60 个交易日**。）

---

## 覆盖的子赛道（context，非推荐）

光子/光模块/CPO · 化合物半导体（InP 衬底/外延片）· HBM/NAND 内存 · 先进封装/玻璃基板 · neocloud 融资 ·
AI 数据中心电力/散热（800V DC）· 特种材料（WF₆ 等）· 机器人/physical AI。
（原 skill 的逐票 conviction 会过期且为自报——本 lens 只用赛道结构，不固化具体 ticker 结论。）

---

## 输出与配合
- **默认**：直接给结构化的 bottleneck 分析（链条图/层级 + 清单打分 + conviction + 催化剂 + thesis-breaker + 风险 + 来源分级）。
- **要深做一篇**：把结论接力给 **stock-research skill** 出完整一页（回一手财报做多空与估值）——本 lens 负责「**去哪找标的 + 怎么过筛**」，stock-research 负责「**回一手做估值与多空**」。

## ⚠️ 免责声明（每次输出必带，不得删）
本分析为公开信息 + 一套供应链方法论的应用，**不构成投资建议**，不构成任何证券买卖要约。原方法来源的战绩为
**自报、未经验证、含幸存者/选择偏差**；本 lens 偏好高波动微/小盘，可能归零，杠杆打法多数人不可复制。
请回一手申报核实、独立判断。投资有风险，入市需谨慎。
