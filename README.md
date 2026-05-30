# 📚 paper-reading

个人文献阅读与整理仓库。给一篇论文的**标题**或**链接**，由 `paper-reading` skill 自动：
下载 → 精读 → 生成一篇**自包含的中文解读 HTML** → 发布到本仓库 → 返回一个可点击查看的链接。

> 在线目录（发布到 `main` 后）：
> <https://raw.githack.com/zhangshuibai/paper-reading/main/index.html>
> 启用 GitHub Pages 后还可用：`https://zhangshuibai.github.io/paper-reading/`

## 怎么用

在本仓库的 Claude Code 会话里，直接把论文丢给我，例如：

```
帮我读一下 https://arxiv.org/abs/2501.01234
解读《Attention Is All You Need》
```

我会运行 `paper-reading` skill，完成后给你一个链接，点开即是这篇论文的解读。

## 每篇解读包含

1. **开源贡献** — 原文标题 / 作者 / 团队 / 链接，以及**核实过的**开源清单（代码 / 模型权重 /
   数据集 / 环境 / benchmark / demo，含真实链接与许可证）。
2. **动机与贡献** — 领域痛点、本文切入点、核心 contribution。
3. **方法** — 整体框架 + 逐模块拆解，配原文图或重绘示意图，公式逐符号解释。
4. **实验评估** — benchmark、baseline、metric、主结果与提升幅度、关键消融。
5. **洞见** — 可迁移的 takeaway、局限与未来方向。

## 结构

```
index.html                      在线目录（读取 papers.json 渲染卡片）
papers.json                     目录数据源（由脚本维护，唯一可被跨篇修改的文件）
papers/<slug>/index.html        某篇论文的解读（自包含，内联 CSS + 本地图片）
papers/<slug>/figures/          该篇用到的图片
.claude/skills/paper-reading/   skill 本体
  SKILL.md                      工作流与规则
  templates/paper.html          解读 HTML 模板（5 个板块）
  scripts/fetch_arxiv.sh        下载 arXiv PDF + 源码（取原图）
  scripts/render_figures.py     用 PyMuPDF 把 PDF 渲染/裁剪成 PNG
  scripts/index_add.py          幂等地往 papers.json 增改一条（仅元数据）
```

## 两条原则

- **隔离解读**：解读某篇时**只**依据该篇本身及其官方开源物，绝不参考仓库里其他已有解读，避免相互串味。
- **自包含**：每篇解读单独成页，内联样式、图片本地化，单独打开也能正常显示。

## 查看链接说明

仓库是公开的，所以无需任何配置即可用 [raw.githack.com](https://raw.githack.com) 直接渲染 HTML：
`https://raw.githack.com/zhangshuibai/paper-reading/<分支或commit>/papers/<slug>/index.html`。
若想要更干净的固定网址，可在仓库 **Settings → Pages** 里把 Source 设为 `main` 分支的根目录，启用
GitHub Pages 后即可用 `https://zhangshuibai.github.io/paper-reading/...` 访问。

---
*解读由 AI 生成，仅作辅助，细节以原文为准。*
