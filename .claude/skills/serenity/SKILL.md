---
name: serenity
description: >-
  Apply trader Serenity's (@aleabitoreddit) AI / semiconductor SUPPLY-CHAIN BOTTLENECK
  framework to US-stock evaluation and market judgment. Use when evaluating a stock decision
  (buy/sell/hold/size); forming an outlook on AI, semiconductor, optical/CPO, memory, power/grid,
  or neocloud names; mentioning a ticker in Serenity's universe (NBIS, AXTI, LITE, SIVE, COHR,
  AAOI, IREN, CRWV, MU, SNDK, NVDA, TSM, MRVL, AVGO, INTC, IQE, TSEM, VRT, VST, CEG, etc.);
  asking "find the chokepoint / trace the supply chain upstream / 卖铲子的上游是谁"; or asking
  "what would Serenity think". It hunts mispriced UPSTREAM single-source bottlenecks the way
  hyperscaler capex flows (ASIC → optical/CPO → substrate/InP → epiwafer → feedstock → power),
  applying a 12-principle framework + a 14-question scoring checklist + 4 workflows, classifying
  any X/news post type, and returning a structured read with a CONVICTION tier, dated catalysts,
  thesis-breakers, and source-graded facts. DECISION-SUPPORT LENS ONLY — never auto-trades,
  never financial advice, never copies unverified self-reported returns. Ported from the public
  repo yan-labs/serenity-aleabitoreddit; live per-ticker theses go stale (~30 min / regenerated
  ~biweekly) so re-confirm against primary sources before any decision.
---

# serenity

把交易员 **Serenity（@aleabitoreddit）的「AI/半导体供应链 bottleneck」框架**搬成本地 lens：
给定一个 ticker / 子赛道，**沿 hyperscaler capex 往上游追**，找「下游万亿支出、自己却小市值」的
**单点 chokepoint**，用 12 原则 + 14 题清单 + 4 工作流去判断，输出带 **conviction 档位 + 带日期催化剂 +
证伪条件 + 来源分级 + 风险框架** 的结构化结论。

**出处**：移植自公开 repo `yan-labs/serenity-aleabitoreddit`（Serenity 的 5,857 条推文 + 4 篇长文蒸馏成的
agent skill）。本地保留方法论（`references/methodology.md`）、逐票知识库快照（`references/theses.md`）、
校准与帖子分类（`references/track-record.md`）。**不搬运原始推文存档**（体量大且为第三方内容）。

**⚠️ 非投资建议（not financial advice）。** decision-support lens：**不下单、不喊单、不保证收益**。
用它「**问更好的问题，不是抄作业**」。每次输出必带免责声明。

---

## 触发条件

激活本 skill 当用户：
- 做**个股决策**（买/卖/持有/仓位）；
- 对 **AI / 半导体 / 光模块·CPO / 内存 / 电力·电网 / neocloud** 板块下判断；
- 提到 Serenity universe 里的 ticker（NBIS, AXTI, LITE, SIVE, COHR, AAOI, IREN, CRWV, MU, SNDK,
  NVDA, TSM, MRVL, AVGO, INTC, IQE, TSEM, VRT, VST, CEG, EWY 等）；
- 问「**find the chokepoint / 把供应链往上游追 / 卖铲子的上游是谁 / 这是真 bottleneck 吗**」；
- 或问「**Serenity 会怎么看**」。

**⚠️ 时效红线**：原 skill 的逐票结论**约 30 分钟即 stale**（theses 从 live X feed 约每两周重生成）。
`references/theses.md` 是**某时点快照**——用前**先回一手核实当前价格/基本面**，别拿过期结论当现状。

---

## ⛔ Non-negotiable rules

1. **Verify, don't copy.** 原作者的逐票结论与战绩是**自报 + 事后视角 + 幸存者/选择偏差**——**绝不照搬当信号**。
   任何数字回一手核实（SEC 10-K/10-Q/8-K、IR、交易所、合同公告），按来源分级标注：
   🟢 一手 / 🟡 二手(分析师/媒体) / 🔴 自述·未证实(管理层 guidance、KOL 帖、TAM 宣称、自报收益)。
2. **不混淆供应链层级（灵魂红线）。** `substrate ≠ epiwafer ≠ foundry ≠ module ≠ system`。
   画链条时每层谁控盘、占 BOM 多少、能否被绕开，分清楚。
3. **给档位 + 给证伪条件。** 输出明确 conviction 档位，并写清 **thesis-breaker（什么会推翻）**。不给虚假精度、不预测点位。
4. **诚实于偏差。** 偏好 <~$3B 微/小盘、日波动 20%+、可能用杠杆——明确写适用人群与归零风险。
5. **时效。** 标「数据截至 <日期>」，别用过时结论冒充最新。

---

## 核心 edge（一句话）

> 别买最显眼的卖铲人（NVDA）。沿 hyperscaler capex 往上游追：
> **ASIC → 光模块/CPO transceiver → 衬底 substrate/InP → 外延片 epiwafer → 原料 feedstock → 电力/散热**，
> 找那个「buyers 不惜代价也要保供、占 BOM 比例小所以能吸收涨价」的**单点 chokepoint**，
> 趁它还小市值、机构还没定价时介入。

辅助 lens：**Mag7 客户集中度**、**签约 ARR vs 市值错配**、**GAAP 毛利战**、**稀释/ATM 筛雷**、**融资质量谱**。

---

## 12 条原则（详见 `references/methodology.md`）

1. **Bottleneck hunting（核心）** — 单一/近单一来源、下游绕不开只能接受涨价的卡点。
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

**红旗 / 反模式**：纯技术分析无基本面；**混淆供应链层级**；把内部人卖出当方向信号；
基于 X/Reddit 情绪建仓；追已被抢跑的事件；只有头衔、缺供应链运营 fluency 的评论。

---

## 14 题打分清单（进场前自检，详见 references）

①真 bottleneck 有定价权？②在上游、占 BOM 比例小所以买家能吸收涨价？③能不混淆层级地画全链条？
④TAM 随 AI capex / physical-AI 扩张？⑤签约对手方 AAA 级可信？⑥GAAP 毛利撑得起质量定位？
⑦融资干净（无大额 ATM/SBC 悬顶）？⑧仍在放量前、被 TTM 营收错杀？⑨有带日期的催化剂、在可交易窗口内？
⑩市值够小（<~$3B）有机构重估空间？⑪机构覆盖仍滞后于供应链证据？⑫二元风险与仓位/工具匹配？
⑬明确持仓还是探索性提及？⑭当前宏观（利率/关税/地缘）助力还是阻力？

> 命中越多越强；②（层级混淆）或⑦（ATM 悬顶）触红旗→显著降档或否决。

---

## 4 个工作流（按用户问法选）

**(a) 单票评估** — ①查 `references/theses.md` 里他的立场/conviction 档位/演变；②对照 `references/articles.md`
（如有长文背书）；③未覆盖则跑 methodology 清单；④**标时效**、回一手确认当前价格/基本面；
⑤用校准带（见 track-record）给观点加权；⑥**以分析框架呈现，绝不当下单指令**。

**(b) 组合 / 自选审查** — 把持仓分三桶：**Agreements**（他看多/符合 lens）/ **Conflicts**（他看空或谨慎/踩红旗）/
**Gaps**（他高信念但你没覆盖的卡点）→ 出优先级讨论清单（仅建议，不生成交易）。

**(c) 前瞻板块观点** — 抓主题线（CPO/光子、HBM/内存、neocloud 融资、电力/电网、InP/化合物半导体、机器人/physical AI）→
拉相关 theses + 领先指标 → 给观点 + 置信度 + **证伪条件**。

**(d) 新帖 / 新闻信号评估** — ①**分类帖子类型**（见下）；②对历史类比（track-record）；
③**把「市场窗口」和「股票论点」分开评**；④转成纪律（watch 规则 / 限价阶梯）而非订单。

---

## Conviction 档位（输出统一用这套）

`Strongly Bullish`（强看多）/ `Bullish`（看多）/ `Catalyst Watch`（候催化）/ `Mixed`（中性混合）/
`Cautious / Commentary`（谨慎·仅评论）/ `Track Record Validated`（已被价格/基本面部分验证，**自报**）/ `Avoid`。
> 每个档位都要配 **sizing 思路**（仓位匹配信念与结局二元性；zero-or-hero 用定义风险的期权而非正股）。

## 帖子类型分类（信号评估用）+ 信号滞后
- **新 bottleneck 论点** → 最高研究权重；验证链条与定价权。
- **反复重申 / 抄底（dip-buy）** → 中等；看是否只是情绪维护。
- **供应商地图（supplier map）** → 高信息量、低即时性；用于建链条。
- **victory lap（晒单/晒收益）** → **最低权重**；幸存者偏差重灾区，绝不当入场信号。
- 典型**信号滞后**：公开论点 → 市场验证约 **5–60 个交易日**（订单/申报/媒体/机构建仓兑现）。

---

## 校准（原 skill 的 2026 自评，均为估算/自报，标 🔴/🟡）
- 30 天**方向准确率 ~61%**（30/49 dated calls）🟡
- 严格 **±10% 命中 ~41%**（20/49，30 天）🟡
- **60 天内 +20%** 占 **~54%**（29/54）🟡
- 成熟 theses 被价格/基本面**部分验证 65–75%**🟡；最强子集（AI 光子/CPO/InP/内存）**75–85%**🟡
- ⚠️ 自报**绝对收益**（如 237% @2026-02、4502.45% YTD @2026-05）**完全未经验证**🔴——**不得引用为业绩证据**。

## What this skill won't do
- 不自动交易、不下/撤单。
- 不提供投资建议。
- 不保证收益、不验证自报业绩（上面那些数字均未证实）。
- 不建议盲目照抄高毛利微/小盘仓位。

## Required risk framing（每次输出必述）
1. 收益为**自报、未验证**，存在幸存者/选择偏差；2. 校准是**估算的公开喊单准确率**，非实盘证明；
3. 多数标的日波动 20%+，杠杆打法多数人不可复制；4. theses 会衰减，下单前**重确认基本面**；
5. 这是 **decision-support lens，不是信号源、不是自动交易系统**。

---

## ⚠️ 免责声明（每次输出必带，不得删）
本分析为公开信息 + 一套供应链方法论的应用，**不构成投资建议**，不构成任何证券买卖要约。原方法来源的逐票结论与
战绩为**自报、未经验证、含幸存者/选择偏差**；本 lens 偏好高波动微/小盘，可能归零，杠杆打法多数人不可复制。
请回一手申报核实、独立判断。投资有风险，入市需谨慎。
