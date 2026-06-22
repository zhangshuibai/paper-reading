---
name: tech-explainer
description: >-
  Build ONE self-contained, INTERACTIVE technical-explainer HTML for any system / architecture /
  pipeline / protocol / supply chain — centered on a RELATIONSHIP DIAGRAM (modules = nodes,
  connections & dependencies = labeled edges) with optional multi-scale views, a step-through
  DATA/CONTROL-FLOW ANIMATION, click/hover NODE DETAIL panels (what it is / connects to / why),
  a "dependencies & mutual-constraints" deep section, novice-friendly plain-language mental
  models, source-graded facts, auto light/dark theme and accessibility. Use whenever the user
  wants to 讲明白 / 可视化 / 拆解 how the parts of a system relate, connect, depend on, or talk to
  each other — hardware (AI cluster, CPU, network), software architecture, ML/data pipelines,
  protocol stacks, distributed systems, supply chains, even biological pathways. It commits the
  note to this repo (papers/<slug>/) and returns a click-to-view link.
---

# tech-explainer

把一个**技术系统**做成一篇打磨过、**可交互**的自包含 HTML 讲解：核心是一张**关系图**（模块=节点、
连接/依赖=带标注的边），配**数据流动画**、**点节点看详情**、**依赖与相互制约**深入层，让读者既能
**建立直觉**又能**理解机制**。脱胎自 `papers/2026-06-17-ai-cluster-architecture/` 那篇的配方，做成通用能力。

**输出语言 — 中文散文，术语保留英文**（`bandwidth`、`latency`、`API`、`bus`、`RDMA`、`pipeline`、
`protocol`、`ontology` 等专名）。

---

## ⛔ Non-negotiable rules

1. **关系图是主角。** 一定要有「节点 + 带标注的边」的关系图；**每个节点都能点开**看「是什么 / 连谁 / 为什么这么连」；
   **至少一个 step-through 流程动画**演示一次代表性过程（数据流 / 请求链 / 信号路径 / 控制流）。
2. **技术准确 > 炫。** 数字会随代际/版本变——一律用「**约 / 数量级 / 视代际/版本**」并尽量标代表型号/版本；拿不准就**定性**描述。
   每条关键事实标来源等级：🟢 一手(官方文档/规范/论文) / 🟡 二手(媒体/博客/分析) / 🔴 自述·未证实。**绝不编精确值。**
3. **两层讲清。**（a）**直觉层**：关系图 + 数据流动画 + 通俗类比 + 心智模型；（b）**机制层**：「**依赖与相互制约**」——
   谁靠什么接口连谁、谁的能力卡住谁，把约束串成一条因果链。
4. **领域背景速补（CLAUDE.md）。** 若属非 LLM/ML 核心领域，**必须**加一节，用通俗中文讲清关键术语（是什么/为什么难/与本篇关系），靠前放。
5. **Self-contained + 可达性。** 单个 `papers/<slug>/index.html`，**inline CSS/JS/SVG**、无外部依赖；
   **自动浅/深主题**、响应 `prefers-reduced-motion`、键盘可操作、移动端响应式。
6. **诚实边界。** 若图里列了公司/产品/股票 → 加一句「非投资建议/非背书」；模型化的系统有简化 → 注明「示意、非穷尽」。

---

## Inputs
用户给一个**系统/主题**（可能附「讲清各模块关系 / 画个关系图或动画 / 它们怎么依赖、怎么交互」）。
先**界定范围与粒度**：哪些算「模块」、有没有**多个尺度/层级**（如 芯片→节点→机柜→集群、或 client→网关→服务→数据库）。

---

## Workflow

`$REPO = $(git rev-parse --show-toplevel)`；复用脚本 `$SKILL_PR="$REPO/.claude/skills/paper-reading"`。

### 1. 把系统建模成「数据」（这是关键，先想清再写）
- **nodes**：每个模块——`id / label / 一句话 desc / 属于哪个尺度`。
- **edges**：模块间连接/依赖——`from / to / 标注(带宽·协议·介质·延迟等) / kind(分类着色)`，并想清**方向与含义**（数据流？依赖？控制？）。
- **views/scales**（可选）：若系统分层级，按尺度切几个视图，每视图聚焦该层的节点与边。
- **flow**：一条**代表性流程**拆成有序 step（每 step 点亮哪些边 + 一句字幕），如「一次请求/一次训练迭代/一个信号路径」。

### 2. 核实与分级
多源核实关键事实（WebSearch/WebFetch/官方文档/规范）；数字标来源等级、不确定就「约/数量级」；**层级/接口别混淆**（这是技术图最常见错误）。

### 3. 写 HTML（套模板，填数据 + 散文）
- 复制骨架：`cp "$REPO/.claude/skills/tech-explainer/templates/explainer.html" "$REPO/papers/<slug>/index.html"`。
- 模板是**数据驱动**的：在底部 `MODEL = {...}` 里填 `views`(节点坐标/边/标注) 与 `flow`(步骤)，引擎自动渲染关系图、节点详情面板、视图切换、流程动画。**保留引擎逻辑，别破坏控件/主题/a11y。**
- 填散文区：`领域背景速补`、`连接对比表`、`心智模型/类比`、`依赖与相互制约`、`延伸阅读/出处`。处理每个 `{{...}}` 与 `<!-- 填写 -->`、删示例行。
- 自检：`grep -c '{{' papers/<slug>/index.html` = 0；无 `填写/TODO/占位/示例` 残留；内联 JS 过 `node --check`。

### 4. 注册索引
```bash
python3 "$SKILL_PR/scripts/index_add.py" "$REPO/papers.json" \
  --slug "<slug>" --title "<系统名>：关系图与数据流动画（技术讲解）" --authors "—" \
  --team "技术科普" --arxiv "" --code "" \
  --tldr "<一句话：讲清哪个系统的各模块如何连接/依赖/交互 + 有交互关系图与流程动画 + 一个关键洞察>" \
  --tags "explainer,interactive,diagram,architecture,<领域tag>" \
  --date "$(date +%F)" --published "技术科普 $(date +%Y)"
```
（**不加 `competitive-landscape`**，除非它同时是市场地图——避免误进首页「公司调研」置顶组。）

### 5. 发布（CLAUDE.md：制作发布放后台）
```bash
cd "$REPO" && git add -A && git commit -m "Add 技术科普: <系统名> 关系图与数据流动画"
# 推 main，non-fast-forward 时 fetch→rebase（papers.json 冲突 python 合并保留两边、勿 --ours/--theirs）→ push；网络错误退避 2s/4s/8s/16s
```
回报：raw.githack（SHA 固定）链接 + 视图/SVG 数、是否含流程动画 + 2–3 句话（讲了什么系统 / 关系图与动画演示什么 / 一个关键依赖洞察）。

---

## 报告骨架
1. **TL;DR + 一句话**（这是什么系统、关系图能看到什么）
2. **领域背景速补**（非 LLM 领域必带）
3. **交互关系图**（节点+边，可点节点看详情；多尺度则给视图切换）
4. **数据流/控制流动画**（▶ 播放/暂停/单步/复位 + 步骤字幕）
5. **连接/接口对比表**（按 介质·带宽·延迟·距离·作用 或 协议·方向·用途 对比）
6. **心智模型 / 类比**（给小白）
7. **依赖与相互制约（深入）**（谁靠什么接口连谁、谁卡住谁、约束因果链 + 可配电↔光这类转换小图）
8. **延伸阅读 / 出处**（相对链接到 repo 内相关篇；外部来源按🟢🟡🔴）

## Conventions
- slug：`YYYY-MM-DD-<topic-kebab>`。
- `--published` 写「技术科普 YYYY」便于与论文/公司调研区分。
- 标题点明「关系图 / 数据流 / 技术讲解」以示这是 tech-explainer。

## Fallbacks
- **系统太大**：选一个清晰边界 + 一句「本篇聚焦 X，未含 Y」；用多尺度视图分解。
- **无公认数字**：定性描述 + 标「随实现/版本而变」，绝不编。
- **纯软件/抽象系统**：节点=组件/服务，边=调用/依赖/数据流；flow=一次请求生命周期。
- **资源被网络策略挡**：写「受网络策略限制未能核实」，用已知信息继续，绝不编。
