# 面壁智能（ModelBest）商业调研报告

> **调研日期**：2026-06-01 ｜ **方法**：6 路并行检索 + 一手来源（官网 / GitHub OpenBMB / Hugging Face / arXiv 技术报告 / 36氪·量子位等）交叉核验 ｜ 数字均标注**官方宣称 vs 平台实测/第三方**，存疑处单独提示。
>
> 官网 [modelbest.cn](https://modelbest.cn/) · [github.com/OpenBMB](https://github.com/OpenBMB) · [huggingface.co/openbmb](https://huggingface.co/openbmb)

---

## 核心结论（TL;DR）

面壁智能是清华 NLP 实验室（THUNLP）与 OpenBMB 开源社区孵化的「**高效大模型 / 端侧 AI**」公司，以开源 **MiniCPM「小钢炮」** 系列建立口碑，核心叙事是自创的 **Densing Law（密度法则）**——能力密度每约 3.3 个月翻倍，已发表于 *Nature Machine Intelligence*。商业模式是「开源引流 + To B 端侧方案变现」，最硬的落地是**汽车座舱**（长安马自达 EZ-60、吉利银河 M9 两款真实量产车）。2026 Q1 由中国电信、深创投等领投，累计融资超 10 亿元、估值迈入独角兽。

**两个核心结论：**

**① 定位就是 8B 以下端侧小模型。** 全系覆盖 0.5B / 1B / 2.4B / 4B / 8B，主力 ≤8B，押注「手机 / PC / 座舱本地能跑」（INT4 量化后最小仅 0.5GB）；多模态 MiniCPM-V/o 是手机端 VLM 标杆，自 MiniCPM4 起转 Apache-2.0 可商用。

**② agentic 能力一般，且没在正规基准上验证过。** tool-use 只在**静态 function calling（BFCL）+ 厂商自建 MCP 测试集**上报过分，**从未在正规 MCP agentic 基准（MCP-Universe、MCPMark）或 agentic coding 基准（Terminal-Bench、SWE-bench）上测过**——这些榜由前沿大模型把持（MCP-Universe 上 GPT-5 才 43.72%、Claude-4-Sonnet 29.44%），8B 端侧模型基本到不了台面。框架层 ChatDev（⭐33k）、端侧 GUI grounding（AgentCPM-GUI）算亮点，但「真实多轮 agentic 编排」无第三方背书；coding 同样非第一梯队（无专用 code 模型，真实编程榜落后 Qwen3 / Phi-4）。

---

## ① 公司概况

| 维度 | 内容 | 确定性 |
|---|---|---|
| 全称 | 北京面壁智能科技有限责任公司（英文 ModelBest） | 高 |
| 成立 | 源自清华 NLP 实验室 + OpenBMB，2021 年刘知远牵头筹组，2022 年 8 月公司化 | 高 |
| 核心人物 | 刘知远（清华副教授，联创/首席科学家）；李大海（CEO，原知乎 CTO）。知乎为早期股东 | 高 |
| 定位 | 「以高效为第一性原理的大模型公司」，主打端侧 AI / 高效大模型 | 高 |
| 商业模式 | 开源 MiniCPM 引流 + To B 行业落地（汽车座舱 / AI 手机 / AI PC / 法律政务），C 端有多模态助手「露卡 Luca」 | 高 |
| 上市 | 截至 2026-06 尚未上市，仍处一级市场融资阶段，无明显负面 | 高 |

**融资路径**（金额多为「数千万/数亿」模糊披露，估值为媒体口径）：

| 时间 | 轮次 / 规模 | 主要投资方 |
|---|---|---|
| 2023.04 | 天使，数千万元 | 知乎领投、智谱 AI 跟投 |
| 2024.04 | 数亿元 | 春华创投、华为哈勃领投，北京市 AI 产业基金跟投 |
| 2024.12 | 数亿元 | 龙芯创投、鼎晖百孚、中关村科学城、赛富领投 |
| 2025 全年 | 数亿元 | 北京国资持续加注 |
| 2026 Q1 | **累计超 10 亿元，估值迈入独角兽** | 中国电信领投；深创投、汇川产投领投（北京/深圳双城国资布局） |

> **理论壁垒 · Densing Law（密度法则）**：开源 LLM 的最大「能力密度」每约 3.3 个月翻一倍，对标摩尔定律，是「小模型打大模型」叙事的根基（arXiv [2412.04315](https://arxiv.org/abs/2412.04315)，已上 [Nature MI](https://www.nature.com/articles/s42256-025-01137-0)）。

---

## ② 重点一：模型 size 与应用场景

### 2.1 文本主线（size × 定位）

| 模型 | 参数量 | 上下文 | 发布 | 关键特性 | 许可 |
|---|---|---|---|---|---|
| MiniCPM-2B (1.0) | 2.4B | 2K→128K | 2024-02 | 首代端侧，媲美 Mistral-7B | 权重需问卷 |
| MiniCPM-S-1B | 1B | — | 2024-07 | 稀疏激活，FFN FLOPs −84% | Apache-2.0 |
| **MiniCPM3-4B** | 4B | 32K | 2024-09 | 超 Phi-3.5-mini / GPT-3.5；**原生 function call + 代码解释器** | Apache-2.0 |
| MiniCPM4-0.5B | 0.5B | 32K | 2025-06 | 端侧极小，配三值量化 BitCPM4 | Apache-2.0 |
| **MiniCPM4-8B** | 8B | 32K→128K | 2025-06 | **InfLLM v2 稀疏注意力**；端侧比 Qwen3-8B 快 ~7×；8T tokens 达 Qwen3-8B(36T) 水平 | Apache-2.0 |
| MiniCPM4.1-8B | 8B | 64K→128K+ | 2025-09 | 混合推理 `<think>`，~3× 推理加速 | Apache-2.0 |
| MiniCPM5-1B | 1B | 长上下文 | 2026-05 | SOTA 1B 端侧，原生 tool call，混合推理 | Apache-2.0 |

### 2.2 多模态 MiniCPM-V / MiniCPM-o（手机端 VLM 标杆）

| 模型 | 参数量 | 模态 | 发布 | 对标宣称（官方） |
|---|---|---|---|---|
| MiniCPM-V 2.6 | 8B | 单图/多图/视频 | 2024-08 | GPT-4V 级，OpenCompass 65.2 |
| **MiniCPM-o 2.6** | 8B | + **音频/语音/实时直播** | 2025-01 | GPT-4o 级，OpenCompass 70.2 |
| MiniCPM-V 4.5 | 8B | 高 FPS 视频 | 2025-08 | 超 GPT-4o-latest / Qwen2.5-VL 72B，77.0 |
| MiniCPM-o 4.5 | 9B | 全模态 | 2026-02 | Gemini 2.5 Flash 级 |
| MiniCPM-V 4.6 | 1.3B | 图/视频 | 2026-05 | 「手机原生」，~6GB 内存 |

> **端侧定位的硬证据**：BitCPM 三值量化位宽 −90%；MiniCPM5-1B INT4 仅 **0.5GB**；MiniCPM4-8B 在 Jetson AGX Orin 上长文本解码比 Qwen3-8B 快 **~7×**；InfLLM v2 使 128K 长文本每 token 仅计算 <5% token；官方支持 llama.cpp / Ollama / vLLM / SGLang。
> ⚠️ 网传「**220× 加速**」是极端长文本场景的营销口径，技术报告正文实测为 **5–7×**。

### 2.3 应用场景与客户（汽车座舱为最硬主线）

> 性质：✅ 量产/签约 · ⚙️ 合作/适配 · ❌ 不成立

| 案例 | 性质 | 说明 |
|---|---|---|
| **长安马自达 EZ-60** | ✅ 量产 | 2025-04 上市，「首个纯端侧模型量产车」，搭载纯端侧助手 cpmGO |
| **吉利银河 M9** | ✅ 量产 | 2025-09，与吉利中央研究院联合开发端侧 **VLA 0.9B** 多模态 |
| 瑞芯微 Rockchip | ✅ 签约 | 2026-04 战略合作，MiniCPM-o 4.5 + 芯片做座舱 AI Box |
| 英特尔 | ✅ 量产/适配 | AI PC + 「全球首个大规模量产 AI Box」（Core Ultra，最高 180 TOPS） |
| 中科创达 | ✅ 签约 | 基于滴水 OS 打造下一代智能座舱 |
| 联想 / 易来 IoT / 百度智能云 | ⚙️ 合作 | 伙伴名单级（PC / 智能家居 / 具身边缘） |
| 华为 | ⚙️ 资本+适配 | 哈勃投资 + 昇腾适配，**非整机搭载公告** |
| 招商银行 / 西门子 / 易车等 ToB | ⚠️ 中等确定 | 来自二手综述，缺一手新闻稿 |
| 梅赛德斯-奔驰 | ❌ 不成立 | 经核实无任何合作证据；奔驰走 Azure + Google 路线 |

**商业逻辑**：端侧模型主打**离线可用、低延迟、隐私安全**，参数压到 0.9–1.3B（INT4 后 0.5GB），覆盖手机/PC/座舱/IoT/机器人本地运行。2025-07 将「汽车业务线」升为一级组织，正从**模型供应商 → 「芯片+模型」座舱方案商**演进。

---

## ③ 重点二：Agentic 能力（Tool Use 与 Coding）

### 3.1 Tool use / function calling / MCP —— 有完整布局，但只在静态 / 自建基准上验证

- **MiniCPM3-4B 原生 function call**，并有微调版 **MiniCPM3-4B-FC**，入 Berkeley Function-Calling Leaderboard（**BFCL v2 = 76.0**，超 Llama3.1-8B、Qwen2-7B、GLM-4-9B）。注意：BFCL 是**静态、单轮**的 function-calling 基准，不等于真实多轮 agentic。
- **MiniCPM4-MCP（8B）**：端侧 MCP agent，跨 16 个 MCP server，func/param/value 三指标平均 88.3% / 76.1% / 51.2%——经核实，这是 OpenBMB **自建的 MCP 测试集**（仅与 gpt-4o、qwen3 比），**不是第三方基准 MCP-Universe 或 MCPMark**。
- **MiniCPM5-1B**：1B 手机本地 agent，原生 tool call，推荐 SGLang 后端（内置 parser 转 OpenAI 兼容 `tool_calls`）。

> ⚠️ **评测覆盖缺口（重要）**：面壁**未在主流真实 agentic 基准上公开成绩**——tool-use/MCP 侧的 **MCP-Universe**（231 任务、11 真实 server）、**MCPMark**，以及 agentic coding 侧的 **Terminal-Bench**、**SWE-bench**，榜单里都**没有 MiniCPM**。这些榜由前沿大模型把持（MCP-Universe 上 GPT-5 仅 43.72%、Claude-4.0-Sonnet 29.44%；Terminal-Bench 头部 Claude Sonnet 4.5 50.0%）。8B 量级端侧模型在这类多轮、长程、真实环境任务上通常接近底部，因此「agentic 强」**缺乏第三方硬基准支撑**——更准确的说法是「**function calling / 单步工具调用达到同尺寸领先，但真实 agentic 编排能力未经独立验证**」。

### 3.2 Agent 框架与端侧 GUI agent

| 项目 | 是什么 | ⭐ (2026-06) | 状态 |
|---|---|---|---|
| **ChatDev** | LLM 多智能体协作软件开发 | 33.3k | ✅ 活跃 |
| ToolBench / ToolLLM | 工具学习训练/评测平台（ICLR'24 spotlight） | 5.7k | 在更新 |
| XAgent | 自主 LLM agent | 8.5k | ⚠️ 停更(2024-08) |
| AgentVerse | 多智能体部署框架 | 5.0k | ⚠️ 停更(2024-09) |
| **AgentCPM-GUI** | 端侧手机 GUI agent（8B，操作中文 App，动作均 9.7 token） | 1.4k | ✅ 中文 App grounding SOTA 91.28% |

> **判断（已修正）**：Agentic「三层」**布局**齐全——框架层（ChatDev / ToolBench）、数据基准层（ToolBench / UltraTool）、模型原生层（MiniCPM3-4B-FC / MiniCPM4-MCP / MiniCPM5-1B / AgentCPM-GUI）。但要把「布局完整」与「能力强」分开：可验证的硬成绩集中在 ① 静态 function calling（BFCL）、② 自建 MCP 评测、③ 端侧 GUI grounding（AgentCPM-GUI 有真实 benchmark）；而真实多轮 agentic（MCP-Universe/MCPMark）与 agentic coding（Terminal-Bench/SWE-bench）**未见参评**。通用 agent 框架重心已从 XAgent/AgentVerse（均停更）转向「模型原生 agentic + 端侧」，ChatDev 是唯一仍高活跃的框架。**结论：端侧 agent 布局领先、GUI grounding 有亮点，但「真实 agentic 编排能力」尚无第三方背书。**

### 3.3 Coding 能力 —— 够用、同尺寸领先，但非第一梯队

- **无专用 code 模型**（不同于 Qwen-Coder / DeepSeek-Coder），coding 是通用能力副产品。
- MiniCPM3-4B：HumanEval+ 68.3 / MBPP+ 63.2 / **LiveCodeBench v3 仅 22.6** —— HumanEval/MBPP 刷分友好虚高，真实竞赛榜偏低。
- MiniCPM4.1-8B（深度推理）：HumanEval 95.7、AIME 领先 Qwen3-8B，但 **LiveCodeBench v5/v6 仍输 Phi-4-14B 与 R1 蒸馏版**。
- **官方自承**：极小模型「在更难的数学与编程任务上更弱，归因于模型尺寸限制推理能力」。

> ⚠️ **公认局限**：所报 coding 成绩全部是**代码生成类**（HumanEval / MBPP / LiveCodeBench），**未见 agentic coding 基准**（Terminal-Bench、SWE-bench——由 Claude Sonnet 4.5、GPT-5.5 等把持，无 MiniCPM）。复杂 coding 与 **long-horizon agent**（多步工具链、仓库级任务）是小模型结构性短板：步数增长准确率急剧下降、单步错误级联放大、长程规划弱，对端侧小模型尤其致命。

---

## ④ 开源生态（GitHub / Hugging Face）

**OpenBMB** = 清华 THUNLP（研究）+ 面壁 ModelBest（商业化）共建。GitHub 组织自我宣称总 star **13万+**（未由第三方排名站独立复核）。

| 平台 | 项目 / 组织 | 关键指标（2026-06-01） | 性质 |
|---|---|---|---|
| GitHub | ChatDev | ⭐ 33.3k | 实测 |
| GitHub | MiniCPM-V（含 MiniCPM-o） | ⭐ 25.5k，Apache-2.0 | 实测 |
| GitHub | VoxCPM（语音） | ⭐ 24k | 实测 |
| GitHub | MiniCPM | ⭐ 9.3k，Apache-2.0 | 实测 |
| GitHub | ToolBench / XAgent / AgentVerse | ⭐ 5.7k / 8.5k / 5.0k | 实测 |
| GitHub | CPM.cu（自研端侧 CUDA 推理栈） | ⭐ 240，Apache-2.0 | 实测 |
| Hugging Face | openbmb 组织 | 151 模型 / 39 数据集 / 11 Spaces | 实测 |
| Hugging Face | MiniCPM-V-4.6 | 月下载 45.9万，赞 1.08k | 实测 |
| Hugging Face | MiniCPM5-1B | 月下载 45.7k | 实测 |
| Hugging Face | Ultra-FineWeb（数据集） | 月下载 65.4k | 实测 |
| 跨平台 | MiniCPM/-V 累计下载 | 「破千万 / 近 3000 万」 | 宣称 |
| 生态 | llama.cpp / Ollama / vLLM / SGLang | 官方支持（README 明示） | 实测 |

> 许可：代码与近期模型为 Apache-2.0；早期 MiniCPM 权重用「通用模型许可协议」——学术免费，端侧部署 ≤5,000 台或 DAU<100 万可免费商用，超出需申请。整体趋向更宽松的 Apache-2.0。

---

## ⑤ 竞争格局（端侧 / 小模型赛道）

| 维度 | 面壁 MiniCPM | 阿里 Qwen3 | Google Gemma3 | MS Phi-4 | 智谱 GLM |
|---|---|---|---|---|---|
| 同尺寸综合实力 | 强 | **最强、迭代最快** | 强、多模态好 | 推理/coding 强 | 强（中文好） |
| **Coding 绝对值** | 中 | **强（有 Coder 专线）** | 中 | **强（LCB 领先）** | 中 |
| **端侧推理栈** | **最突出** | 有但非核心 | 量化友好 | 一般 | 有 GLM-Edge |
| 多模态端侧 | **手机 VLM 标杆** | Qwen-VL 强 | 强 | 弱 | — |
| 理论叙事 | **Densing Law 独家** | 工程规模化 | 安全/多模态 | 数据质量 | — |

**差异化定位**：不打「最强 coding」，而打「**端侧最高性能密度 + 最完整端侧推理软件栈（CPM.cu / InfLLM v2 / BitCPM 三值量化 / ArkInfer 多后端）+ 手机多模态**」。在纯编程 SOTA 上不与 Qwen-Coder / Phi-4 正面硬刚，而是打「同等体积下综合更强 + 跑得动在边缘芯片」。

---

## ⑥ 商业判断（SWOT）

| | |
|---|---|
| **Strengths 优势** | 性能密度真实领先（22% tokens 达 Qwen3-8B 水平）；端侧软硬一体壁垒国内最深；独家 Densing Law 叙事（上 Nature MI）+ 手机 VLM 口碑；两款真实量产车背书。 |
| **Weaknesses 劣势** | agentic / coding 硬成绩只来自静态或自建基准，真实 agentic 榜（MCP-Universe、Terminal-Bench、SWE-bench）未参评、缺第三方背书；无专用 code 模型；「以小博大」对标多为同尺寸或上一代闭源（GPT-3.5），面对 Qwen3-4B-2507 等新对手领先不稳固。 |
| **Opportunities 机会** | 座舱「芯片+模型」AI Box 方案商；AI 手机 / AI PC 端侧浪潮；具身智能 VLA；端侧 MCP/GUI agent。 |
| **Threats 威胁** | Qwen 小尺寸迭代极快且全栈布局；端侧模型授权变现天花板与商业化节奏存疑；座舱方案商竞争（高通 / 厂商自研）。 |

> **一句话**：面壁 MiniCPM 是「端侧高性能密度 + 推理工程」的标杆，coding「够用且同尺寸领先」，但**不是为复杂编程 / 长程 Agent 而生**；护城河是效率与端侧部署栈，而非编程 / agentic SOTA——后者仍由 Qwen（含 Coder 专线）与 Phi-4、以及前沿大模型把持。

---

## ⑦ 需注意的存疑点（诚实披露）

1. ❌ **奔驰合作不成立**——经核实无任何证据。
2. ⚠️ **「220× 加速」** 为营销口径，技术报告实测 5–7×。
3. 「千万 / 3000 万累计下载」「13 万 star」为**官方/媒体宣称**，HF 仅给月下载，无法逐项独立复核。
4. 招商银行 / 西门子等 ToB 客户来自二手综述，缺一手新闻稿。
5. 华为为资本 + 适配关系，**非整机搭载**；手机整机量产搭载暂无官方公告。
6. 各轮融资金额与估值均为模糊或媒体口径，公司未公布精确数字。
7. ⚠️ **agentic / coding 评测口径**：BFCL 是静态 function calling、MiniCPM4-MCP 的 88.3% 是自建 MCP 测试集；真实 agentic 基准 **MCP-Universe / MCPMark** 及 agentic coding 的 **Terminal-Bench / SWE-bench** 均**未见 MiniCPM 参评**。引用其「agentic 能力」时务必区分「单步工具调用」与「多轮真实编排」。

---

## 主要来源

- **官方**：[modelbest.cn](https://modelbest.cn/) · [GitHub OpenBMB](https://github.com/OpenBMB) · [HF openbmb](https://huggingface.co/openbmb)
- **技术报告**：[MiniCPM4 (arXiv 2506.07900)](https://arxiv.org/abs/2506.07900) · [MiniCPM (2404.06395)](https://arxiv.org/abs/2404.06395) · [Densing Law (2412.04315)](https://arxiv.org/abs/2412.04315) / [Nature MI](https://www.nature.com/articles/s42256-025-01137-0) · [AgentCPM-GUI (2506.01391)](https://arxiv.org/abs/2506.01391)
- **模型卡 / 榜单**：[MiniCPM3-4B](https://huggingface.co/openbmb/MiniCPM3-4B) · [MiniCPM4-MCP](https://huggingface.co/openbmb/MiniCPM4-MCP) · [MiniCPM-o 2.6](https://huggingface.co/openbmb/MiniCPM-o-2_6) · [BFCL Leaderboard](https://gorilla.cs.berkeley.edu/leaderboard.html)
- **真实 agentic 基准（用于对照，MiniCPM 未参评）**：[MCP-Universe](https://mcp-universe.github.io/) · [MCPMark](https://mcpmark.ai/leaderboard) · [Terminal-Bench](https://www.tbench.ai/leaderboard/terminal-bench/2.0) · [SWE-bench](https://www.swebench.com/)
- **项目 / 竞品**：[ChatDev](https://github.com/OpenBMB/ChatDev) · [AgentCPM-GUI](https://github.com/OpenBMB/AgentCPM-GUI) · [Qwen3-4B-2507](https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507)
- **公司 / 融资**：[36氪](https://www.36kr.com/p/2728647825646857) · [量子位](https://www.qbitai.com/2024/12/231764.html) · [东方财富](https://finance.eastmoney.com/a/202604093699228297.html) · [财联社](https://www.cls.cn/detail/2338712)
- **落地**：长安马自达 EZ-60（[IT之家](https://ithome.com/0/848/497.htm)）· 吉利银河 M9（[搜狐汽车](https://db.m.auto.sohu.com/model_7673/a/938174512_122362510)）· 瑞芯微（[证券时报](https://www.stcn.com/article/detail/3893255.html)）

---

*本报告由 `deep-research` 工作流（6 路并行检索 + 交叉核验）生成，仅供参考，关键商业决策请以官方一手信息二次核验 · 调研日期 2026-06-01。HTML 版见同目录 [`index.html`](./index.html)。*
