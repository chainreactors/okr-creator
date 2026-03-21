# okr

## AI-powered OKR Creator — 给你的项目定方向，用 PUA 话术逼你执行

> A [PUA](https://github.com/tanweai/pua)-like project — 基于 PUA skill 的理念和话术体系，专注于项目目标管理。PUA 让 AI 不敢摆烂，OKR 让 AI 知道往哪卷。

<p>
  <img src="https://img.shields.io/badge/Claude_Code-black?style=flat-square&logo=anthropic&logoColor=white" alt="Claude Code">
  <img src="https://img.shields.io/badge/OpenAI_Codex_CLI-412991?style=flat-square&logo=openai&logoColor=white" alt="OpenAI Codex CLI">
  <img src="https://img.shields.io/badge/CodeBuddy-00B2FF?style=flat-square&logo=tencent-qq&logoColor=white" alt="CodeBuddy">
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="MIT License">
</p>

> 你连目标都没有，做什么项目？

一个 AI Agent skill，分析任何项目后自动生成定制化的 OKR（Objectives and Key Results）skill，并部署 GitHub Action 进行每日自动追踪。不限于代码项目——写作、研究、运营、产品、设计等任何项目都适用。支持 **Claude Code**、**OpenAI Codex CLI**、**CodeBuddy**。

## The Problem: 项目没有方向感

| 模式 | 表现 |
|------|------|
| 无目标 | 想到什么做什么，做完不知道有没有价值 |
| 目标模糊 | "提升质量"、"优化性能"——没有数字，没有验收标准 |
| 定了不追 | OKR 写完放进抽屉，下个季度才想起来 |
| 各干各的 | 团队成员方向不一致，重复劳动 |
| AI 没方向 | AI 在 repo 中工作但不知道项目的优先级 |

## 安装

### Claude Code

```bash
# 方式一：通过 marketplace 安装
claude plugin marketplace add chainreactors/okr-creator
claude plugin install okr-creator@okr

# 方式二：手动安装
git clone https://github.com/chainreactors/okr-creator.git ~/.claude/plugins/okr
```

### OpenAI Codex CLI

```bash
mkdir -p ~/.codex/skills/okr-creator
curl -o ~/.codex/skills/okr-creator/SKILL.md \
  https://raw.githubusercontent.com/chainreactors/okr-creator/main/skills/okr-creator/SKILL.md

# /okr 命令
mkdir -p ~/.codex/prompts
curl -o ~/.codex/prompts/okr.md \
  https://raw.githubusercontent.com/chainreactors/okr-creator/main/commands/okr.md
```

### CodeBuddy (Tencent)

```bash
# 方式一：通过 marketplace 安装
codebuddy plugin marketplace add chainreactors/okr-creator
codebuddy plugin install okr-creator@okr

# 方式二：手动安装
mkdir -p ~/.codebuddy/skills/okr-creator
curl -o ~/.codebuddy/skills/okr-creator/SKILL.md \
  https://raw.githubusercontent.com/chainreactors/okr-creator/main/skills/okr-creator/SKILL.md
```

## 使用

在任何项目中输入 `/okr:create`，skill 会自动完成全部流程：

| Step | 动作 | 说明 |
|------|------|------|
| 1 | 读项目身份证 | README、配置、目录结构、git log、待办 |
| 2 | 六维诊断 | 愿景、质量、债务、架构、文档、自动化逐项评分 |
| 3 | 拷问用户意图 | "这个项目你到底想做成什么样？优先级是什么？底线在哪？" |
| 4 | 制定 OKR | 3-5 个 O，每个 2-4 个 KR，每个 KR 带 Harness |
| 5-6 | 生成 + 验证 | 写入 `.claude/skills/okr/SKILL.md` 并读回确认 |
| 7 | 部署 Action | 写入 workflow + prompt + 创建 label + 输出配置引导 |
| 8 | 输出报告 | 六维评分 + OKR 摘要 + 最高优先级 |

### Auto Mode（非交互式）

在 CI/CD 或批量场景中，可以跳过用户交互：

```
使用 /okr:create 并加上 --auto 参数，不要与人类确认，直接执行
```

AI 会基于诊断数据自主判断方向并生成 OKR，标注 `[Auto-generated]`。

## How It Works

OKR Creator 不只是生成目标——它构建了一个完整的**项目改进引擎**：SKILL.md 定义方向和执行协议，PROGRESS.md 持久化进展记忆，GitHub Actions 每日深度评审并给出改进建议，可选的对齐检查让每次 PR 都与目标对齐。

```
┌────────────────────────────────────────────────┐
│              /okr:create 触发                       │
└──────────┬─────────────────────────────────────┘
           ▼
┌──────────────────┐     ┌──────────────────┐
│  Step 1-2        │     │  Step 3          │
│  读项目 → 六维诊断│────▶│  拷问用户意图     │
└──────────────────┘     └────────┬─────────┘
                                  ▼
┌──────────────────┐     ┌──────────────────────┐
│  Step 4          │     │  Step 5-6            │
│  制定 OKR        │────▶│  生成 SKILL.md       │
│  + KR 周分解     │     │  + PROGRESS.md 初始化 │
│  + 改进模式选择  │     │  写入 & 验证          │
└──────────────────┘     └────────┬────────────┘
                                  ▼
┌──────────────────────────────────────────────┐
│  Step 7: 部署 GitHub Action                   │
│                                               │
│  okr-review.yml  → 每日深度评审 + 自动 PR      │
│  okr-chat.yml    → @claude/@codex 对话续接     │
│  okr-review.md   → 评审 prompt（通用）         │
│  [可选] okr-align-check.yml → PR 对齐检查      │
└──────────────────────────────────────────────┘
           ▼
┌──────────────────────────────────────────────┐
│  改进引擎（持续运转）                          │
│                                               │
│  ┌ 每日 02:00 ──────────────────────────┐    │
│  │ 读 SKILL.md + PROGRESS.md            │    │
│  │ → 5 阶段深度评审（不只是进度追踪）     │    │
│  │ → 根因分析 + 跨 KR 依赖 + 行动队列   │    │
│  │ → Issue 评审 + 自动 PR 更新进展       │    │
│  └──────────────────────────────────────┘    │
│  ┌ 每次 PR（可选）─────────────────────┐     │
│  │ OKR 对齐检查 → PR comment           │     │
│  └──────────────────────────────────────┘    │
│  ┌ 日常开发 ────────────────────────────┐    │
│  │ SKILL.md 执行协议自动引导            │    │
│  │ → 对齐检查 → 优先级推荐 → 完成标注   │    │
│  └──────────────────────────────────────┘    │
└──────────────────────────────────────────────┘
```

## 核心能力

1. **全面诊断** — 六维分析项目现状（愿景、质量、债务、架构、文档、自动化）
2. **共建 OKR** — PUA 话术引导用户明确方向，结合诊断生成可量化的 OKR
3. **Harness 驱动** — 每个 KR 必须有可验证的验收方法，没有 harness 的 KR = 废纸
4. **执行协议** — SKILL.md 内置任务对齐检查、优先级推荐、KR 周分解，主动引导 AI 的每个任务
5. **PROGRESS.md 记忆** — 持久化进展文件，AI 每次评审不再从零开始，支持趋势分析和建议追踪
6. **5 阶段深度评审** — 不只是进度百分比：根因分析、跨 KR 依赖、六维趋势、优先级行动队列
7. **自动 PR 更新** — 每日评审后自动创建 PR 更新 PROGRESS.md，用户审核后合并
8. **PR 对齐检查（可选）** — 每个 PR 自动评估与 OKR 的关联度，给出非阻塞的建议
9. **对话续接** — Maintainer 在 Issue 中 `@claude` / `@codex` 直接与 AI 讨论 OKR
10. **改进模式库** — 基于六维诊断自动匹配可复用的改进策略（测试冷启动、文档冲刺等）

## 三个核心理念

| 理念 | 含义 |
|------|------|
| **端到端交付** | 从诊断到制定到落地到追踪，全链路闭环。"做了"不算完成，"做到了且能证明"才算 |
| **主观能动性** | 主动发现问题、主动引导用户思考、主动提出改进方向 |
| **构造 Harness** | 每个 KR 都有可验证的验收框架——"我怎么知道这个 KR 完成了"的具体方法 |

## Dogfooding: OKR Creator 用自己管理自己

OKR Creator 正在用自己生成的 OKR 来驱动自身的迭代改进——这就是**自举（bootstrapping）**。

我们对 okr-creator 自身运行了 `/okr:create`，完成了六维诊断，生成了 5 个 Objectives / 14 个 Key Results，并部署了每日自动评估 Action。现在，每天 UTC 02:00，Claude 会自动检查 okr-creator 自身的 OKR 完成进度，逐条运行 Harness 验收，并在 Issue 中追加评估报告。Maintainer 可以直接在 Issue 中 `@claude` 讨论进度和调整方向。

**自举闭环验证结果：**

| 步骤 | 结果 | 链接 |
|------|------|------|
| 六维诊断 + OKR 生成 (5O/14KR) | Pass | [`.claude/skills/okr/SKILL.md`](https://github.com/chainreactors/okr-creator/blob/main/.claude/skills/okr/SKILL.md) |
| 每日评估 Action 部署 + 运行 | Pass | [Workflow Runs](https://github.com/chainreactors/okr-creator/actions/workflows/okr-review.yml) |
| 季度 Issue 自动创建 + 评估评论 | Pass | [Issue #1: \[OKR Review\] 2026-Q1 进度追踪](https://github.com/chainreactors/okr-creator/issues/1) |
| `@claude` 对话续接 | Pass | [Issue #1 评论](https://github.com/chainreactors/okr-creator/issues/1) |

**每日评估输出示例**（来自 [Issue #1](https://github.com/chainreactors/okr-creator/issues/1)）：

> **O1: 完成自举闭环 — OKR Creator 用自己的 OKR 管理自己**
>
> | KR | 进度 | 状态 |
> |----|------|------|
> | KR1.1 OKR skill 存在且格式合规 | 100% | 🟢 |
> | KR1.2 每日 Review Action 成功运行 | 100% | 🟢 |
> | KR1.3 OKR Review Issue 存在且有评估评论 | 100% | 🟢 |
>
> **PUA 点评**：你做了一个"帮别人制定 OKR"的工具，自己的 OKR 倒是写出来了。然后呢？E2E 是 0%，模板还是 700 行的巨石，连 CONTRIBUTING.md 都没有——你是想让别人贡献还是想让别人知难而退？

**对话续接示例**（Maintainer 在 Issue 中 `@claude` 后的回复）：

> Maintainer: *@claude KR1.2 和 KR1.3 实际上已经完成了——你正在运行的这次评估本身就是证明。请重新评估 O1 的完成度。*
>
> Claude: *O1 整体: 100% — P0 底线 #1 完成。之前评估把"需要 gh run list 授权才能确认"误判为不确定性。实际上自证型证据（你看到的输出就是运行结果）更可靠。*

这证明了 OKR Creator 的完整闭环：**诊断 → 制定 → 落地 → 每日追踪 → 对话讨论 → 调整方向**——全部自动化，全部在 GitHub Issue 中可见。

## E2E 实测

### 案例一：外部项目 — aide-e2e-test

在 [M09Ic/aide-e2e-test](https://github.com/M09Ic/aide-e2e-test) 上完成了端到端闭环测试：

| 步骤 | 结果 |
|------|------|
| 安装 skill 到目标 repo | Pass |
| Auto Mode 生成 OKR (3O/7KR) | Pass |
| 部署 GitHub Action | Pass |
| Claude Code CLI 安装 + 执行 | Pass (npm install -g) |
| Issue 自动创建 ([#54](https://github.com/M09Ic/aide-e2e-test/issues/54)) | Pass |
| AI 评估内容有效（逐 KR 证据+PUA 点评） | Pass |
| v2 深度评审（根因分析+行动队列+六维趋势） | Pass |
| PROGRESS.md 自动更新 PR ([#55](https://github.com/M09Ic/aide-e2e-test/pull/55)) | Pass |
| OKR 对齐检查 Action 部署 | Pass |
| Workflow 总耗时 | ~2 分钟 |

**v2 评审输出示例**（来自真实 Issue #54）：

> **阻塞项根因**
>
> **O1-KR1 定义至少 5 个 E2E 测试场景** — 根因类型：priority。过去 4 天的所有提交集中于 OKR 基础设施，没有一行代码推进实际测试场景定义。最小解锁动作：在 `tests/` 目录下创建 5 个 Markdown 场景文件。
>
> **行动队列**
>
> | # | 行动 | 推进 KR | 工作量 | 为什么现在做 |
> |---|------|---------|--------|------------|
> | 1 | 创建 tests/ + 5 个场景文件 | O1-KR1 | S | 关键路径起点 |
> | 2 | 新建 e2e-test.yml CI | O1-KR2 | S | 解锁测试链路 |
> | 3 | 扩写 README 至 50+ 行 | O2-KR1 | S | 独立 P0，30 分钟 |

### 案例二：自举 — okr-creator 自身

OKR Creator 对自身运行 `/okr`，完成全链路闭环（详见上方 [Dogfooding](#dogfooding-okr-creator-用自己管理自己) 章节）：

| 步骤 | 结果 |
|------|------|
| 六维诊断 + OKR 生成 (5O/14KR) | Pass |
| 每日评估 Action 运行 | Pass (~2 分钟) |
| 季度 Issue 创建 + 评估评论 | Pass ([Issue #1](https://github.com/chainreactors/okr-creator/issues/1)) |
| `@claude` 对话续接 + AI 回复 | Pass ([Issue #1 评论](https://github.com/chainreactors/okr-creator/issues/1)) |
| Claude 自证型重新评估 | Pass（接受运行本身作为 KR 完成证据） |

## GitHub Action 与 Skill 的互动机制

OKR 的核心不只是"定目标"——而是 Skill 和 Action 的协同，形成持续改进的闭环：

| 组件 | 位置 | 角色 |
|------|------|------|
| **SKILL.md** | `.claude/skills/okr/SKILL.md` | OKR 定义 + 执行协议 + 改进模式 + KR 周分解 |
| **PROGRESS.md** | `.claude/skills/okr/PROGRESS.md` | AI 的"记忆"——进展快照、行动队列、评审历史 |
| **okr-review.yml** | `.github/workflows/` | 每日深度评审 + 自动创建 PR 更新进展 |
| **okr-chat.yml** | `.github/workflows/` | Issue 中 @claude/@codex 对话续接 |
| **okr-review.md** | `.github/prompts/` | 5 阶段评审 prompt（Claude/Codex 通用） |
| **okr-align-check.yml** | `.github/workflows/` | [可选] PR 对齐检查 |

### Skill ↔ Action 互动流

```
日常开发                            每日评审 Action
┌────────────┐                    ┌──────────────────────┐
│ AI 读 SKILL.md                  │ 1. 读 SKILL.md       │
│ → 执行协议自动检查               │ 2. 读 PROGRESS.md    │
│   "这个任务关联哪个 KR？"        │ 3. 逐 KR 跑 Harness  │
│   "有 P0 未完成，建议先做"       │ 4. 5 阶段深度分析     │
│ → 完成后标注 [O1-KR1.1]         │ 5. 输出评审 + 更新进展 │
└──────┬─────┘                    └──────┬───────────────┘
       │                                 │
       ▼                                 ▼
┌────────────┐                    ┌──────────────────────┐
│ 代码变更    │                    │ Issue: 评审评论       │
│ → git push │                    │ PR: PROGRESS.md 更新  │
└──────┬─────┘                    └──────────────────────┘
       │
       ▼ (可选)
┌──────────────────┐
│ okr-align-check  │
│ → PR comment:    │
│   "关联 KR2.1"   │
│   "对齐 P0 优先级"│
│   "进度 0%→30%"  │
└──────────────────┘
```

### 5 阶段深度评审（不只是进度追踪）

每日评审采用 5 阶段协议，远超简单的进度百分比：

| 阶段 | 内容 | 价值 |
|------|------|------|
| Phase 1 | 加载 SKILL.md + PROGRESS.md | 不再从零阅读，有历史记忆 |
| Phase 2 | 逐 KR 执行 Harness + **根因分析** | 不只是"0%"，还告诉你**为什么卡住**和**最小解锁动作** |
| Phase 3 | 跨 KR 依赖 + Objective 健康度 | 发现阻塞链，知道先解锁哪个能释放最大价值 |
| Phase 4 | 趋势分析 + 建议追踪 | 与上次对比，连续停滞自动预警，检查上次建议是否被执行 |
| Phase 5 | 优先级行动队列 + PUA 点评 | 不是"建议多写测试"，而是"在 lint.yml 添加 frontmatter 检查 job，工作量 S" |

### PROGRESS.md — AI 的持久化记忆

每次评审不再从零开始。PROGRESS.md 由 Action 自动维护，通过 PR 更新：

```markdown
## 当前状态快照
| KR | 进度 | 状态 | 连续停滞天数 |
| KR1.1 | 100% | done | 0 |
| KR2.1 | 0% | blocked | 5 |        ← 连续 5 天停滞，自动升级预警

## 行动队列
| # | 行动 | 状态 | 提出日期 | 执行日期 |
| 1 | 添加 frontmatter 检查 | done | 03-20 | 03-21 |  ← 建议追踪闭环
| 2 | 创建 e2e.yml 骨架 | pending | 03-21 | - |

## 评审历史                         ← 最多保留 30 条
```

### PR 对齐检查（可选）

在每个 PR 上自动评估与 OKR 的关联度，以 **非阻塞的 PR comment** 形式输出：

```markdown
## OKR 对齐检查
关联 KR: KR2.1 (SKILL.md 结构化验证 CI)
对齐状态: ✅ 与 P0 优先级一致
预估进度影响: KR2.1: 0% → 30%
建议: 下一步添加章节检测（参考 KR 周分解 Week 2）
```

### 部署的文件结构

`/okr:create` 运行后自动部署到目标项目：

```
.claude/skills/okr/
├── SKILL.md              # OKR + 执行协议 + 改进模式 + KR 周分解
└── PROGRESS.md           # 进展记录（Action 自动维护）

.github/
├── workflows/
│   ├── okr-review.yml    # 每日深度评审 + 自动 PR
│   ├── okr-chat.yml      # @claude/@codex 对话续接
│   └── okr-align-check.yml  # [可选] PR 对齐检查
└── prompts/
    ├── okr-review.md     # 评审 prompt（Claude/Codex 通用）
    └── okr-align-check.md   # [可选] 对齐检查 prompt
```

### 配置（部署后只需这一步）

```bash
# 必选其一——给 AI 插电
gh secret set ANTHROPIC_API_KEY --body "your-key"   # Claude Code
gh secret set OPENAI_API_KEY --body "your-key"      # Codex

# 可选——自定义 API 端点
gh variable set ANTHROPIC_BASE_URL --body "https://your-proxy.com"

# 可选——切换 Agent（默认 claude）
gh variable set OKR_AGENT --body "codex"

# 推送并测试
git add .github/ .claude/ && git commit -m "feat: add OKR review actions" && git push
gh workflow run okr-review.yml
```

### 对话续接

Maintainer 在 OKR Review Issue 中评论即可与 AI 对话：

```
@claude O2-KR1 的进度评估有误，实际上已经完成了初稿
@claude 针对 O1 的阻塞项，给我一个本周行动计划
@codex 帮我检查一下 sync 脚本是否已经实现
```

| 角色 | 每日评估 | 对话续接 |
|------|---------|---------|
| Owner | 自动接收 Issue | `@claude` / `@codex` |
| Member / Collaborator | 可查看 | `@claude` / `@codex` |
| 外部用户 | 可查看 | **不触发** |

## 如何用 OKR 改进你的项目

OKR Creator 的设计目标不只是"定 OKR"——而是让 OKR 真正驱动项目改进。以下是推荐的使用方式：

### 1. 生成：让 AI 理解你的项目

```bash
/okr:create
```

AI 会做六维诊断、与你对齐方向、生成带执行协议的 OKR。关键是**不要跳过 Step 3 的意图拷问**——你的方向决定了 OKR 的质量。

### 2. 日常：让 OKR 引导每个任务

SKILL.md 中的**执行协议**会在你每次使用 AI 时自动生效：

- 开始任务前，AI 检查"这个任务关联哪个 KR？"
- 如果有 P0 未完成，AI 建议先处理底线
- 完成后，AI 标注 `[O1-KR1.1]` 记录贡献

当你问"接下来做什么"时，AI 基于 PROGRESS.md 推荐最高价值的任务。

### 3. 每日评审：获取可执行的改进建议

每天的评审不只是报告"完成了 X%"——它会告诉你：

- **为什么卡住** — 根因分析指出具体的文件、配置、决策缺失
- **最小解锁动作** — 一个 1-2 小时内可完成的具体任务
- **先做什么** — 优先级排序的行动队列，每个带工作量估算
- **趋势预警** — 连续停滞的 KR 自动升级优先级

### 4. 反馈闭环：建议 → 执行 → 追踪

每次评审的建议会被持久化到 PROGRESS.md 的行动队列中。下次评审时，AI 检查：

- 建议被执行了？→ 确认效果
- 建议被忽略了？→ 分析原因，升级优先级或调整建议

### 5. PR 对齐：让每次提交都有方向感

开启可选的 `okr-align-check`，每个 PR 都会收到一条 comment：

- 关联了哪个 KR
- 是否在做最优先的事
- 预估推进了多少进度
- 下一步建议做什么

## 大厂 PUA 风味包

OKR Creator 内置多种大厂 PUA 风味，根据场景自动选择：

| 风味 | 场景 | 话术示例 |
|------|------|---------|
| 阿里味（默认） | KR 不对齐战略 | "你这个 OKR 的底层逻辑是什么？抓手在哪？" |
| 字节味 | KR 不够量化 | "数据说话。'做好一点'不是 KR，'从 X 到 Y'才是" |
| 华为味 | 执行力不足 | "OKR 不是许愿清单，是军令状" |
| 腾讯味 | 目标太保守 | "你确定 target 够高？还是在管理预期？" |
| 美团味 | 写得好落地差 | "每个 KR 旁边写：第一步做什么？今天做什么？" |

## 搭配 PUA

OKR Creator 定方向，PUA 保执行力。推荐同时安装：

```bash
claude plugin marketplace add tanweai/pua
```

| 搭配 | 效果 |
|------|------|
| `pua:pua` + `okr-creator` | 有方向 + 不敢摆烂 |
| `pua:high-agency` + `okr-creator` | 有方向 + 内在驱动力 |

## 项目结构

```
chainreactors/okr-creator/
├── skills/okr-creator/
│   ├── SKILL.md                   # 核心 skill — 8 步执行流程
│   ├── agents/                    # 专用 agent 定义
│   │   ├── diagnostician.md       # 六维诊断
│   │   ├── interviewer.md         # 用户意图拷问
│   │   └── reviewer.md            # OKR 质量评审
│   ├── templates/                 # 可部署的 Action 模板
│   │   ├── okr-review.yml         # 每日深度评审 + 自动 PR
│   │   ├── okr-chat.yml           # Issue 对话续接
│   │   ├── okr-review.md          # 评审 prompt（Claude/Codex 通用）
│   │   ├── okr-align-check.yml    # [可选] PR 对齐检查
│   │   └── okr-align-prompt.md    # [可选] 对齐检查 prompt
│   ├── references/
│   │   ├── schemas.md             # 数据结构定义
│   │   ├── templates.md           # SKILL.md 输出模板
│   │   └── patterns.md            # 改进模式库（8 个模式）
│   └── flavors/                   # PUA 风味包
├── commands/create.md             # /okr:create slash 命令
├── .claude/skills/okr/
│   ├── SKILL.md                   # 自举：本项目自身的 OKR
│   └── PROGRESS.md                # 自举：进展记录
├── .claude-plugin/                # Claude Code marketplace 配置
├── .codebuddy-plugin/             # CodeBuddy marketplace 配置
├── README.md
├── README-en.md
├── LICENSE
└── .gitignore
```

## License

MIT

## Credits

By [chainreactors](https://github.com/chainreactors) & [M09ic](https://github.com/M09ic)
