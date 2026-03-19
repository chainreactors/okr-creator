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
```

## 2. GitHub Action 模板

Action 模板以独立文件形式存放在 `templates/` 目录下，部署时直接复制：

| 模板文件 | 部署路径 | 功能 |
|---------|---------|------|
| `templates/okr-review.yml` | `.github/workflows/okr-review.yml` | 每日 UTC 02:00 自动评估 + 手动触发 |
| `templates/okr-chat.yml` | `.github/workflows/okr-chat.yml` | Issue 评论 `@claude`/`@codex` 触发对话 |
| `templates/okr-review.md` | `.github/prompts/okr-review.md` | Codex 专用评审 prompt |

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
