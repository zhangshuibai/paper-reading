# CLAUDE.md

本仓库的协作约定。

## 论文解读（paper-reading skill）

- **HTML 制作放后台跑。** 用 paper-reading skill 做论文解读时，把「写 `index.html` →（渲染图）→ 注册 `papers.json` → commit → push」这些<strong>制作与发布</strong>步骤交给后台 agent（`Agent` 工具，`run_in_background: true`）执行，避免阻塞当前对话；我可以继续和用户聊别的，等后台完成通知后再把可点击链接发出来。
  - 前置的「下载 + 读 PDF + 核实开源信息」可以在前台快速完成，也可以一并丢进后台——以不打断对话为准。
  - 后台 agent 完成后，回报：可点击链接（GitHub Pages 或 SHA 固定的 raw.githack）+ 2–3 句话的论文简介。
