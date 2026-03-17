---
name: okr
description: "本项目的 OKR 目标和关键结果。每次开始新任务前参考此 OKR 确保工作方向一致。生成时间：2026-03-17。基于项目诊断 + 用户意图共同生成。"
license: MIT
---

# chainreactors/okr — OKR

> 本文件由 okr-creator skill 自动生成，基于对项目的全面分析和与项目负责人的对齐。
> 生成时间：2026-03-17
> 时间范围：2026-Q2（2026-04-01 ~ 2026-06-30）
> 建议每季度重新运行 /okr 更新。

## 项目概况

**okr-creator** 是一个 AI Agent skill，分析任何项目后自动生成定制化 OKR，并部署 GitHub Action 进行每日自动追踪。支持 Claude Code、OpenAI Codex CLI、CodeBuddy。当前版本 v1.0.0，处于初始发布向快速成长的过渡阶段。核心交付物是一个 700+ 行的 SKILL.md 文件。

## 六维诊断摘要

| 维度 | 现状评分 (1-5) | 关键发现 |
|------|--------------|---------|
| 项目愿景 | 4 | 愿景清晰但无 roadmap，v1.0 之后方向不明 |
| 交付质量 | 2 | 零自动化测试，E2E 依赖手动操作不可复现 |
| 历史债务 | 4 | 代码库干净，无 TODO/FIXME，但设计仍在摸索 |
| 结构架构 | 3 | SKILL.md 700 行巨石文件，Action 模板内嵌，维护困难 |
| 文档完善 | 3 | README 详尽但缺 CONTRIBUTING.md、CHANGELOG |
| 自动化 | 3 | 有 lint + release CI，但核心交付物无质量门禁 |

## 用户意图

方向：**全维度自举** — 质量闭环 + 架构可维护 + 生态扩张全部推进。
投入：**全力冲刺**，本季度主力项目。
底线（P0）：
1. OKR Creator 自己有可运行的 OKR，每日 Action 能跑通
2. SKILL.md 的修改有 CI 门禁，不会悄悄坏掉
3. 至少一个平台（Claude Code）完成 E2E 自动化

## OKR

### O1: 完成自举闭环 — OKR Creator 用自己的 OKR 管理自己

> 一个帮别人定 OKR 的工具，自己没有 OKR，这叫什么？叫笑话。

| KR | Baseline | Target | Harness（验收方法） | 优先级 |
|----|----------|--------|-------------------|-------|
| KR1.1 项目自身的 OKR skill 存在且格式合规 | 不存在 | `.claude/skills/okr/SKILL.md` 存在，frontmatter 包含 name/description/license 字段 | `head -5 .claude/skills/okr/SKILL.md \| grep -c '^---'` 返回 2；`grep -c '^name:' .claude/skills/okr/SKILL.md` 返回 1 | P0 |
| KR1.2 每日 OKR Review Action 成功运行 | Action 未部署 | `okr-review.yml` 存在且最近 7 天内至少有 1 次成功运行 | `gh run list --workflow=okr-review.yml --status=success --limit=1 --json createdAt --jq '.[0].createdAt'` 返回 7 天内日期 | P0 |
| KR1.3 OKR Review Issue 存在且有评估评论 | 无 Issue | 存在带 `okr-review` label 的 open Issue，且至少有 3 条评估评论 | `gh issue list --label okr-review --state open --json number --jq '.[0].number'` 返回 Issue 编号；`gh api repos/:owner/:repo/issues/{number}/comments --jq 'length'` >= 3 | P0 |

### O2: 建立核心交付物质量门禁 — SKILL.md 改了不会悄悄坏

> 你的核心产品是 SKILL.md。改坏了没人拦，等用户发现再修？这叫"面向投诉编程"。

| KR | Baseline | Target | Harness（验收方法） | 优先级 |
|----|----------|--------|-------------------|-------|
| KR2.1 SKILL.md 结构化验证 CI | 仅有 frontmatter 字段检查 | CI 验证：(1) frontmatter 必填字段 (2) 必须包含 Step 1-8 关键章节 (3) Action 模板 YAML 语法合法 (4) 模板占位符无残留 | `lint.yml` 中存在 `skill-structure-check` job；PR 修改 SKILL.md 时该 job 自动触发且 pass | P0 |
| KR2.2 Markdown lint 零 warning | 当前未统计 | `markdownlint` 对所有 .md 文件报告 0 warning | `npx markdownlint-cli2 '**/*.md' 2>&1 \| grep -c 'MD'` 返回 0 | P1 |
| KR2.3 SKILL.md 变更需有配套 README 更新 | 无规范 | CI 检查：如果 PR 修改了 `skills/okr-creator/SKILL.md`，则必须同时修改 `README.md`（防止文档与实现脱节） | `lint.yml` 中存在 `doc-sync-check` job | P1 |

### O3: E2E 自动化可复现 — 不靠人肉验证

> 你在外部 repo 手动跑了一次就叫"E2E 验证通过"？换个项目呢？换个版本呢？换个人呢？

| KR | Baseline | Target | Harness（验收方法） | 优先级 |
|----|----------|--------|-------------------|-------|
| KR3.1 Claude Code 平台 E2E workflow | 手动验证 | GitHub Action 自动化 E2E：创建临时 repo → 运行 /okr --auto → 验证输出文件存在且格式合规 → 清理 | `.github/workflows/e2e.yml` 存在；`gh run list --workflow=e2e.yml --status=success --limit=1` 返回结果 | P0 |
| KR3.2 E2E 覆盖核心输出验证 | 0 个检查点 | E2E 至少验证 5 个检查点：(1) SKILL.md 生成 (2) frontmatter 合规 (3) 至少 1 个 Objective (4) 每个 KR 有 baseline+target (5) Action 文件生成 | E2E workflow 的 step 中包含以上 5 个 assert | P0 |
| KR3.3 第二平台 E2E | 0 平台 | Codex CLI 或 CodeBuddy 平台完成 E2E 自动化 | 对应 workflow 存在且有成功运行记录 | P2 |

### O4: 架构可维护 — SKILL.md 不再是巨石

> 700 行的单文件，改一个 Action 模板要上下翻 300 行找位置。这叫"代码"还是叫"文学作品"？

| KR | Baseline | Target | Harness（验收方法） | 优先级 |
|----|----------|--------|-------------------|-------|
| KR4.1 Action 模板外置 | 3 个模板内嵌在 SKILL.md 中 | Action 模板（okr-review.yml、okr-chat.yml、okr-review.md）存放在独立目录 `templates/` 下，SKILL.md 引用路径而非内嵌全文 | `ls templates/okr-review.yml templates/okr-chat.yml templates/okr-review.md` 全部存在；SKILL.md 中不再包含完整 YAML 模板 | P1 |
| KR4.2 SKILL.md 行数控制 | 700+ 行 | SKILL.md 主体 <= 400 行（不含被引用的外部文件） | `wc -l skills/okr-creator/SKILL.md` <= 400 | P1 |
| KR4.3 PUA 风味包可扩展 | 硬编码在 SKILL.md 中 | PUA 风味包独立为 `flavors/` 目录下的 .md 文件，新增风味只需加文件 | `ls flavors/*.md \| wc -l` >= 5 | P2 |

### O5: 生态与社区就绪 — 让别人能参与进来

> 你想让别人贡献，连 CONTRIBUTING.md 都没有？门都找不到怎么进？

| KR | Baseline | Target | Harness（验收方法） | 优先级 |
|----|----------|--------|-------------------|-------|
| KR5.1 贡献者文档 | 不存在 | CONTRIBUTING.md 存在，包含：开发流程、SKILL.md 修改规范、PUA 风味新增流程、测试方法 | `test -f CONTRIBUTING.md && grep -c '## ' CONTRIBUTING.md` >= 4 | P1 |
| KR5.2 CHANGELOG 启动 | 不存在 | CHANGELOG.md 存在，记录 v1.0.0 及后续变更 | `test -f CHANGELOG.md && grep -c '## ' CHANGELOG.md` >= 1 | P2 |
| KR5.3 Marketplace 上架率 | Claude Code 已配置，CodeBuddy 已配置 | 至少 2 个平台 marketplace 实际可安装（非仅有配置文件） | 在各平台尝试安装并验证 skill 加载成功 | P2 |

## 工作指引

当你在本项目工作时，请参考以上 OKR：

- 新的工作应与某个 Objective 对齐
- 每次交付建议标注关联的 KR（如 `[O2-KR2.1]`）
- 遇到优先级冲突时，按 O 的排序决策（O1 > O2 > O3 > O4 > O5）
- P0 是底线——做不到就算季度失败
- 发现与 OKR 不一致的方向时，主动提出讨论
- 自举验证：本 OKR 本身就是 O1-KR1.1 的交付物
