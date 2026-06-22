# AI 集群供应链科普 · 配音脚本（timed）

> **片名：** 从一句 prompt 到一座数据中心 —— AI 集群供应链 9 层全拆解
> **时长目标：** 约 3 分 40 秒（3–4 分钟）
> **风格：** 硬件小白科普、轻松、节奏明快；术语都讲人话 + 打类比
> **配音建议：** 中文普通话，亲切清晰的口播音色；语速适中偏快（约每分钟 250–280 字）；每幕之间留约 0.3 秒气口；关键术语（GPU / HBM / CoWoS / EUV / InP）略放慢、加重读。
> **画面主线：** 屏幕左侧始终是一张**竖向 9 层供应链栈**（上=离用户最近，下=最上游）；讲到哪层，哪层**点亮高亮**、其余层灰显淡出。右侧是大标题 + 旁白字幕 + 该层代表 ticker 的 chips 滑入。
> **配套：** 与动画讲解页 `index.html` 的 12 幕一一对应。

---

## 第 1 幕 · 开场（00:00 – 00:14）

- **【画面】** 黑/深底，9 层栈整体以中性色淡淡浮现（不点亮任一层）。一只手在手机上打字、AI 秒回。镜头从手机缓缓拉远，露出一座庞大的数据中心剪影。运镜：缓慢 push-in 后拉远。
- **【旁白】** 你在手机上打一行字，AI 几秒就回你一段话。可你知道吗？这背后是一条横跨十几个国家、上百家公司的超长供应链。今天我们从你这一侧出发，一层一层往上游挖，看看每层是谁在卖什么、又是谁卡谁的脖子。一共九层，发车。
- **【字幕】** 一句 prompt，怎么变成一座数据中心？｜供应链共 9 层

## 第 2 幕 · 第 1 层 应用/模型/云（00:14 – 00:33）

- **【画面】** 9 层栈中**第①层「应用/模型/云」点亮**，其余灰显。chips 滑入：MSFT、GOOGL、AMZN、META、CRWV、NBIS、IREN。配图：云 logo、机柜、"按小时租卡"的小动画。
- **【旁白】** 最上面，是花钱买单的人。微软、谷歌、亚马逊、Meta，这些「超大云厂商」砸钱建数据中心。还有一批「算力二房东」，自己买一堆显卡，再按小时租给别人，比如 CoreWeave、Nebius。记住：他们花的钱，就是下面八层所有人的饭。
- **【字幕】** 第1层 应用/模型/云：买单的人｜hyperscaler + neocloud（算力二房东）

## 第 3 幕 · 第 2 层 AI 加速芯片（00:33 – 00:54）

- **【画面】** **第②层「AI 加速芯片」点亮**。chips：NVDA、AMD、INTC、AVGO、MRVL。配图：一颗发光 GPU；旁边浮出 "CUDA" 锁形图标。
- **【旁白】** 往下一层，是真正干活的大脑——GPU，一种擅长同时算一大堆数的芯片。英伟达一家独大，AMD 在追，Intel 做 CPU 当配角。大客户嫌 GPU 贵，就自己设计专用芯片 ASIC，幕后操刀的是博通和 Marvell。而英伟达最深的护城河叫 CUDA：一套用了十几年的软件生态，换别家就得重写代码，所以很难逃。
- **【字幕】** 第2层 AI 加速芯片：大脑｜GPU(NVDA/AMD) · ASIC(AVGO/MRVL) · 护城河=CUDA

## 第 4 幕 · 第 3 层 HBM 高带宽内存（00:54 – 01:12）

- **【画面】** **第③层「HBM」点亮**。chips：SK Hynix、Samsung、MU、SNDK。配图：多层内存芯片像千层蛋糕叠起来，紧贴 GPU。
- **【旁白】** GPU 算得再快，也得有地方快速存数据。HBM，高带宽内存，就是把很多层内存芯片像千层蛋糕一样叠起来、紧贴 GPU，喂数据特别快。全世界能量产 HBM 的，只有三家：SK 海力士、三星、美光。供不应求。旁边还有存大文件的闪存 NAND。
- **【字幕】** 第3层 HBM：贴着大脑的超快记忆条｜全球仅 3 家（海力士/三星/美光MU）

## 第 5 幕 · 第 4 层 先进封装 + 代工（01:12 – 01:31）

- **【画面】** **第④层「先进封装 + 代工」点亮**。chips：TSM、Samsung、中芯、ASE。配图：GPU 与 HBM 被焊到同一块基板上，"CoWoS" 标签 + 红色"产能吃紧"警示。
- **【旁白】** GPU 和 HBM 得在一小块基板上严丝合缝拼到一起，这道工艺叫先进封装。台积电的 CoWoS 是行业标准，但产能长期吃紧，是个著名卡点。而芯片本身的"印刷"，也就是代工，也主要靠台积电，三星和中芯在追。封装环节还有日月光。
- **【字幕】** 第4层 先进封装+代工：把芯片拼起来、造出来｜CoWoS=台积电TSM 卡点

## 第 6 幕 · 第 5 层 半导体设备（01:31 – 01:50）

- **【画面】** **第⑤层「半导体设备」点亮**。chips：ASML、AMAT、LRCX、KLAC、东京电子。配图：一台巨大的 EUV 光刻机，打上"全球独家"金标。
- **【旁白】** 造芯片要用一屋子顶级机器。最关键的是光刻机——荷兰 ASML 的 EUV 极紫外光刻机，全球独此一家，一台几亿美元，先进芯片绕都绕不开。除此之外，刻蚀、薄膜、量测设备，由应用材料、泛林、科磊、东京电子分着吃。
- **【字幕】** 第5层 半导体设备：造芯片的机器｜EUV 光刻机=ASML 全球独家

## 第 7 幕 · 第 6 层 网络/互连/光（01:50 – 02:11）

- **【画面】** **第⑥层「网络/互连/光」点亮**。chips：COHR、LITE、AAOI、300308.SZ、SIVE。配图：上万张 GPU 用光纤连成一张发光大网；电信号→光信号的转换动画。
- **【旁白】** 一个 AI 集群有成千上万张 GPU，它们必须高速互相通信，否则各算各的就没意义。连接靠交换芯片，博通的 Tomahawk、Marvell；还有光模块——把电信号变成光、用光纤传，又快又省电。更前沿的 CPO，是把光直接做进芯片，还有外置的 CW 激光器，也都在起量。
- **【字幕】** 第6层 网络/光互连：让上万张卡连成一个大脑｜光模块 COHR/LITE/中际旭创

## 第 8 幕 · 第 7 层 衬底/外延（02:11 – 02:30）

- **【画面】** **第⑦层「衬底/外延片」点亮**。chips：AXTI、Sumitomo、IQE、TSEM。配图：一片特殊晶圆"地基"，上面长出薄薄一层外延膜；标"InP 磷化铟"。
- **【旁白】** 上一层那些光器件，并不是长在普通硅片上，而是长在特殊的化合物半导体衬底上，比如磷化铟 InP。能稳定供 InP 衬底的，全球只有少数几家：AXT、住友等等；在它上面再"长"一层薄膜，叫外延片。越往上游，玩家越少、越隐形，却越关键。
- **【字幕】** 第7层 衬底/外延：芯片的地基｜InP 衬底 AXTI · 供应商极少

## 第 9 幕 · 第 8 层 电力 & 散热（02:30 – 02:50）

- **【画面】** **第⑧层「电力 & 散热」点亮**。chips：VRT、ETN、VST、CEG。配图：电表狂转、数据中心吃电像一座小城；液冷管路给芯片降温。
- **【旁白】** 这么多 GPU 一开机，吃电像一座小城市。供电设备 Vertiv、Eaton，还有新一代 800 伏直流架构，都成了刚需。电从哪来？发电的公用事业公司直接受益，比如 Vistra、Constellation。芯片太热，风扇不够用，于是开始上液冷——用液体直接给芯片降温。
- **【字幕】** 第8层 电力&散热：AI 是真的"电老虎"｜供电 VRT · 电力 VST/CEG · 液冷

## 第 10 幕 · 第 9 层 上游原材料（02:50 – 03:08）

- **【画面】** **第⑨层「上游原材料」点亮**（栈底）。chips：信越/SUMCO、093370.KS、铜·光纤。配图：硅锭、气瓶、铜线、光纤卷。
- **【旁白】** 挖到最底层，是最朴素的材料：做晶圆的硅片，信越、SUMCO；刻蚀要用的特种气体，比如 WF6；还有铜、光纤这些金属和玻璃。它们便宜、不起眼，可只要断一种，上面八层全得停摆。
- **【字幕】** 第9层 上游原材料：一切的源头｜硅片 · 特气 · 铜/光纤

## 第 11 幕 · 总结 谁卡谁脖子（03:08 – 03:28）

- **【画面】** 9 层栈**自上而下逐层全部点亮**，形成一道贯通的光柱；右侧弹出 4 张红框"卡脖子卡片"。运镜：镜头沿栈缓缓下移。
- **【旁白】** 把九层连起来看，命门很清楚——越往上游，越是少数几家说了算。EUV 光刻机，ASML 全球独家；CoWoS 先进封装，台积电是主要产能瓶颈；HBM 内存，全球就三家；InP 衬底，只有少数几家能稳定供。钱从最上面的云厂商往下流，瓶颈却卡在最上游。看懂这几个点，你就看懂了整条链。
- **【字幕】** 谁卡谁脖子：EUV=ASML独家 · CoWoS=台积电 · HBM=3家 · InP=少数几家

## 第 12 幕 · 非投资建议（03:28 – 03:42）

- **【画面】** 画面收束为一张干净卡片，红色边框，居中大字"非投资建议"。9 层栈缩为右下角小图标。
- **【旁白】** 最后划重点：这期只是硬件科普，帮你看懂这条供应链长什么样、每层是谁。片里出现的所有股票代码，只是用来标位置，不是推荐你买卖任何一只。部分数字做了模糊化处理、可能过时，请以一手公告为准。本片不构成任何投资建议，投资有风险，决策请自行研究。我们下期见。
- **【字幕】** 非投资建议 · 仅作科普｜ticker 仅标注产业链位置，不构成买卖推荐

---

## 附录 A：纯旁白全文（可直接粘贴做一键 TTS）

你在手机上打一行字，AI 几秒就回你一段话。可你知道吗？这背后是一条横跨十几个国家、上百家公司的超长供应链。今天我们从你这一侧出发，一层一层往上游挖，看看每层是谁在卖什么、又是谁卡谁的脖子。一共九层，发车。

最上面，是花钱买单的人。微软、谷歌、亚马逊、Meta，这些「超大云厂商」砸钱建数据中心。还有一批「算力二房东」，自己买一堆显卡，再按小时租给别人，比如 CoreWeave、Nebius。记住：他们花的钱，就是下面八层所有人的饭。

往下一层，是真正干活的大脑——GPU，一种擅长同时算一大堆数的芯片。英伟达一家独大，AMD 在追，Intel 做 CPU 当配角。大客户嫌 GPU 贵，就自己设计专用芯片 ASIC，幕后操刀的是博通和 Marvell。而英伟达最深的护城河叫 CUDA：一套用了十几年的软件生态，换别家就得重写代码，所以很难逃。

GPU 算得再快，也得有地方快速存数据。HBM，高带宽内存，就是把很多层内存芯片像千层蛋糕一样叠起来、紧贴 GPU，喂数据特别快。全世界能量产 HBM 的，只有三家：SK 海力士、三星、美光。供不应求。旁边还有存大文件的闪存 NAND。

GPU 和 HBM 得在一小块基板上严丝合缝拼到一起，这道工艺叫先进封装。台积电的 CoWoS 是行业标准，但产能长期吃紧，是个著名卡点。而芯片本身的"印刷"，也就是代工，也主要靠台积电，三星和中芯在追。封装环节还有日月光。

造芯片要用一屋子顶级机器。最关键的是光刻机——荷兰 ASML 的 EUV 极紫外光刻机，全球独此一家，一台几亿美元，先进芯片绕都绕不开。除此之外，刻蚀、薄膜、量测设备，由应用材料、泛林、科磊、东京电子分着吃。

一个 AI 集群有成千上万张 GPU，它们必须高速互相通信，否则各算各的就没意义。连接靠交换芯片，博通的 Tomahawk、Marvell；还有光模块——把电信号变成光、用光纤传，又快又省电。更前沿的 CPO，是把光直接做进芯片，还有外置的 CW 激光器，也都在起量。

上一层那些光器件，并不是长在普通硅片上，而是长在特殊的化合物半导体衬底上，比如磷化铟 InP。能稳定供 InP 衬底的，全球只有少数几家：AXT、住友等等；在它上面再"长"一层薄膜，叫外延片。越往上游，玩家越少、越隐形，却越关键。

这么多 GPU 一开机，吃电像一座小城市。供电设备 Vertiv、Eaton，还有新一代 800 伏直流架构，都成了刚需。电从哪来？发电的公用事业公司直接受益，比如 Vistra、Constellation。芯片太热，风扇不够用，于是开始上液冷——用液体直接给芯片降温。

挖到最底层，是最朴素的材料：做晶圆的硅片，信越、SUMCO；刻蚀要用的特种气体，比如 WF6；还有铜、光纤这些金属和玻璃。它们便宜、不起眼，可只要断一种，上面八层全得停摆。

把九层连起来看，命门很清楚——越往上游，越是少数几家说了算。EUV 光刻机，ASML 全球独家；CoWoS 先进封装，台积电是主要产能瓶颈；HBM 内存，全球就三家；InP 衬底，只有少数几家能稳定供。钱从最上面的云厂商往下流，瓶颈却卡在最上游。看懂这几个点，你就看懂了整条链。

最后划重点：这期只是硬件科普，帮你看懂这条供应链长什么样、每层是谁。片里出现的所有股票代码，只是用来标位置，不是推荐你买卖任何一只。部分数字做了模糊化处理、可能过时，请以一手公告为准。本片不构成任何投资建议，投资有风险，决策请自行研究。我们下期见。

---

## 附录 B：给 AI 视频工具的视觉提示词清单（每幕一句英文 prompt，便于 Runway / 可灵 / 即梦生成 B-roll）

1. **开场：** A hand typing a prompt on a smartphone, the screen glows, camera slowly pulls back to reveal a vast futuristic data center silhouette at night, cinematic, soft blue lighting.
2. **第1层 应用/模型/云：** Floating logos of giant cloud providers above glowing server racks, "rent by the hour" GPU concept, clean tech infographic style, blue and purple palette.
3. **第2层 加速芯片：** A single glowing GPU chip on a dark surface, a translucent lock icon labeled "CUDA" hovering beside it, macro shot, dramatic rim light.
4. **第3层 HBM：** Stacked memory dies like a layered cake pressed tightly against a GPU, exploded-view 3D render, high detail, cyan glow.
5. **第4层 先进封装+代工：** A GPU and HBM stacks being bonded onto one interposer substrate, "CoWoS" label, a red "capacity bottleneck" warning, clean isometric 3D.
6. **第5层 半导体设备：** A massive EUV lithography machine in a cleanroom, workers in bunny suits, a glowing gold "world's only supplier" badge, awe-inspiring scale.
7. **第6层 网络/光互连：** Thousands of GPUs connected by glowing fiber-optic cables into one luminous mesh, electrical-to-light signal conversion animation, futuristic.
8. **第7层 衬底/外延：** A special compound-semiconductor wafer "foundation," a thin epitaxial film growing on top, label "InP", microscopic clean render, rare-and-precious mood.
9. **第8层 电力&散热：** A spinning electricity meter, a data center consuming power like a small city, liquid-cooling pipes flowing over hot chips, energy-intensive vibe.
10. **第9层 上游原材料：** Raw materials — silicon ingots, gas cylinders, copper wire, coils of optical fiber — arranged on an industrial table, humble but essential, warm light.
11. **总结 卡脖子：** A vertical 9-layer supply-chain stack lighting up top to bottom into one beam of light, four red "chokepoint" cards popping out, infographic motion graphics.
12. **非投资建议：** A clean centered card with a red border and bold text "Not Financial Advice", minimalist, the 9-layer stack shrunk to a small corner icon.

---

## 附录 C：非投资建议声明

本配音脚本及对应视频/动画仅为**硬件科普**，所有出现的股票代码（ticker）仅用于标注公司在 AI 集群供应链中的位置，**不构成任何投资建议**，不推荐买卖任何证券。部分数字已做模糊化处理或标注"约"，可能过时或有误，请以公司公告等一手资料为准。投资有风险，决策请自行研究并咨询持牌专业人士。
