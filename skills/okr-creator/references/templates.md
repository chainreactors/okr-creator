# OKR Creator — 输出模板

## 1. SKILL.md 输出模板

生成的 OKR skill 文件必须严格遵循此模板。

```markdown
---
name: okr
description: "本项目的 OKR 目标和关键结果。每次开始新任务前参考此 OKR 确保工作方向一致。生成时间：{日期}。基于项目诊断 + 用户意图共同生成，可手动调整。"
license: MIT
---

# {owner}/{repo} — OKR

> 本文件由 okr-creator skill 自动生成，基于对项目的全面分析和与项目负责人的对齐。
> 生成时间：{日期}
> 时间范围：{quarter}（{start} ~ {end}）
> 建议每季度重新运行 /okr:create 更新。

## 项目概况

{项目简介、技术栈/内容体系、当前阶段}

## 六维诊断摘要

| 维度 | 现状评分 (1-5) | 关键发现 |
|------|--------------|---------|
| 项目愿景 | {分} | {一句话} |
| 交付质量 | {分} | {一句话} |
| 历史债务 | {分} | {一句话} |
| 结构架构 | {分} | {一句话} |
| 文档完善 | {分} | {一句话} |
| 自动化   | {分} | {一句话} |

## 用户意图

方向：**{方向}**
投入：**{投入级别}**
底线（P0）：

1. {底线1}
2. {底线2}
3. {底线3}

## OKR

### O1: {Objective 1 标题}

> {PUA 风格点评}

| KR | Baseline | Target | Harness（验收方法） | 优先级 |
|----|----------|--------|-------------------|-------|
| {KR1.1 描述} | {当前值} | {目标值} | {验收命令/条件} | P0/P1/P2 |

### O2: {Objective 2 标题}

...

## 优先级基线

- P0（底线）：{KR 列表}
- P1（重要）：{KR 列表}
- P2（可选）：{KR 列表}

## 工作指引

当你在本项目工作时，请参考以上 OKR：

- 新的工作应与某个 Objective 对齐
- 每次交付建议标注关联的 KR（如 `[O2-KR2.1]`）
- 遇到优先级冲突时，按 O 的排序决策（O1 > O2 > ...）
- P0 是底线——做不到就算季度失败
- 发现与 OKR 不一致的方向时，主动提出讨论

## 执行协议

开始任何任务前，执行以下检查：

1. **对齐检查** — 这个任务与哪个 KR 相关？如果找不到对应 KR，提醒用户这项工作可能不在当前季度优先级内。
2. **优先级检查** — 是否有更高优先级的 P0 KR 尚未完成？如果有，建议先处理 P0。
3. **阻塞检查** — 这个 KR 是否依赖其他 KR？如果被依赖的 KR 未完成，提醒用户。
4. **进展感知** — 读取 `.claude/skills/okr/PROGRESS.md`（如果存在）了解当前进展，避免重复工作。
5. **完成标注** — 完成任务后，标注 `[Ox-KRx.x]` 并说明对进度的影响。

### 任务推荐规则

当用户问"接下来做什么"时，按以下优先级推荐：

1. 被多个 KR 依赖的阻塞项（解锁价值最大）
2. P0 KR 中进度最低的（底线优先）
3. 投入产出比最高的（小 effort 大 impact）
4. 时间敏感项（即将到期）

### 改进模式

基于六维诊断，以下改进模式适用于本项目（由 okr-creator 基于诊断自动选择）：

{根据六维诊断分数，从 `references/patterns.md` 中选择 2-4 个适用模式嵌入此处}

## KR 分解（Weekly Focus）

{为每个 P0 和 P1 KR 生成 4 周 breakdown}

### {KR ID} {KR 描述}
- Week 1: {具体任务}
- Week 2: {具体任务}
- Week 3: {具体任务}
- Week 4: {具体任务}

## 进展追踪

- 进展文件：`.claude/skills/okr/PROGRESS.md`
- 由每日评审 Action 自动维护，包含：KR 状态快照、六维趋势、行动队列、评审历史
- AI 在开始任何任务前应读取此文件了解当前进展
- 完成任务后应建议更新相关 KR 的进度
```

## 2. GitHub Action 模板

Action 模板以独立文件形式存放在 `templates/` 目录下，部署时直接复制：

| 模板文件 | 部署路径 | 功能 | 必选 |
|---------|---------|------|------|
| `templates/okr-review.yml` | `.github/workflows/okr-review.yml` | 每日自动评估 + PROGRESS.md 更新 PR | 是 |
| `templates/okr-chat.yml` | `.github/workflows/okr-chat.yml` | Issue 评论 `@claude`/`@codex` 触发对话 | 是 |
| `templates/okr-review.md` | `.github/prompts/okr-review.md` | 评审 prompt（5 阶段协议，Claude/Codex 通用） | 是 |
| `templates/okr-align-check.yml` | `.github/workflows/okr-align-check.yml` | PR/push OKR 对齐检查 | 可选 |
| `templates/okr-align-prompt.md` | `.github/prompts/okr-align-check.md` | 对齐检查 prompt | 可选 |

### 技术要点

- 使用 `npm install -g @anthropic-ai/claude-code` 安装 CLI，不依赖 GitHub App
- `claude -p` 非交互模式 + `--output-format text`
- 支持 `ANTHROPIC_BASE_URL` 自定义 API 端点
- 支持 `CLAUDE_MODEL` 变量指定模型（默认 `claude-sonnet-4-6`）
- Codex 使用 `codex exec --approval-mode full-auto`
- Issue body 通过文件写入（`--body-file`）避免 shell 转义问题
- 自动创建 `okr-review` label
- 对话续接仅允许 OWNER / MEMBER / COLLABORATOR 触发

## 3. 部署配置引导

见 SKILL.md Step 7 中的配置引导模板。
