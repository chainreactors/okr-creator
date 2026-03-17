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
claude plugin install okr-creator@okr-creator

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
codebuddy plugin install okr-creator@okr-creator

# 方式二：手动安装
mkdir -p ~/.codebuddy/skills/okr-creator
curl -o ~/.codebuddy/skills/okr-creator/SKILL.md \
  https://raw.githubusercontent.com/chainreactors/okr-creator/main/skills/okr-creator/SKILL.md
```

## 使用

在任何项目中输入 `/okr`，skill 会自动完成全部流程：

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
使用 /okr 并加上 --auto 参数，不要与人类确认，直接执行
```

AI 会基于诊断数据自主判断方向并生成 OKR，标注 `[Auto-generated]`。

## How It Works

```
┌─────────────────────────────────────────────────────┐
│                    /okr 触发                         │
└──────────┬──────────────────────────────────────────┘
           ▼
┌──────────────────┐     ┌──────────────────┐
│  Step 1-2        │     │  Step 3          │
│  读项目 → 六维诊断 │────▶│  拷问用户意图     │
└──────────────────┘     └────────┬─────────┘
                                  ▼
┌──────────────────┐     ┌──────────────────┐
│  Step 4          │     │  Step 5-6        │
│  制定 OKR        │────▶│  生成 SKILL.md    │
│  (Harness 驱动)  │     │  写入 & 验证      │
└──────────────────┘     └────────┬─────────┘
                                  ▼
┌──────────────────────────────────────────────┐
│  Step 7: 部署 GitHub Action                   │
│                                               │
│  okr-review.yml → 每日自动评估，创建 Issue     │
│  okr-chat.yml   → @claude/@codex 对话续接     │
│  okr-review.md  → Codex 评审 prompt           │
│  okr-review label → 自动创建                   │
└──────────────────────────────────────────────┘
           ▼
┌──────────────────────────────────────────────┐
│  每日闭环                                     │
│                                               │
│  UTC 02:00 → Claude/Codex 评估每个 KR         │
│  → 运行 Harness 验证 → Issue 追加评估评论      │
│  → Maintainer @claude 讨论 → AI 回复          │
└──────────────────────────────────────────────┘
```

## 核心能力

1. **全面诊断** — 六维分析项目现状（愿景、质量、债务、架构、文档、自动化）
2. **共建 OKR** — PUA 话术引导用户明确方向，结合诊断生成可量化的 OKR
3. **Harness 驱动** — 每个 KR 必须有可验证的验收方法，没有 harness 的 KR = 废纸
4. **落地为 Skill** — 输出到 `.claude/skills/okr/SKILL.md`，AI 每次工作都能参考
5. **自动部署 Action** — 一键写入 workflow + prompt + label，用户只需配置 API Key
6. **每日自动评估** — GitHub Action 每天跑 Harness 验收，Issue 追踪进度
7. **对话续接** — Maintainer 在 Issue 中 `@claude` / `@codex` 直接与 AI 讨论 OKR

## 三个核心理念

| 理念 | 含义 |
|------|------|
| **端到端交付** | 从诊断到制定到落地到追踪，全链路闭环。"做了"不算完成，"做到了且能证明"才算 |
| **主观能动性** | 主动发现问题、主动引导用户思考、主动提出改进方向 |
| **构造 Harness** | 每个 KR 都有可验证的验收框架——"我怎么知道这个 KR 完成了"的具体方法 |

## Dogfooding: OKR Creator 用自己管理自己

OKR Creator 正在用自己生成的 OKR 来驱动自身的迭代改进——这就是**自举（bootstrapping）**。

我们对 okr-creator 自身运行了 `/okr`，完成了六维诊断，生成了 5 个 Objectives / 14 个 Key Results，并部署了每日自动评估 Action。现在，每天 UTC 02:00，Claude 会自动检查 okr-creator 自身的 OKR 完成进度，逐条运行 Harness 验收，并在 Issue 中追加评估报告。Maintainer 可以直接在 Issue 中 `@claude` 讨论进度和调整方向。

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
| Workflow 总耗时 | ~2 分钟 |

**评估输出示例**（来自真实 Issue #54）：

> KR1: 定义至少 5 个 E2E 测试场景 — 进度 0% — `tests/` 目录不存在
>
> **PUA 点评**：你花了多少精力在"追踪 OKR 的工具"上？你建了一个完美的 OKR 仪表盘，用来实时播报"一事无成"。建议关掉这个文件，去写第一个测试场景。

### 案例二：自举 — okr-creator 自身

OKR Creator 对自身运行 `/okr`，完成全链路闭环（详见上方 [Dogfooding](#dogfooding-okr-creator-用自己管理自己) 章节）：

| 步骤 | 结果 |
|------|------|
| 六维诊断 + OKR 生成 (5O/14KR) | Pass |
| 每日评估 Action 运行 | Pass (~2 分钟) |
| 季度 Issue 创建 + 评估评论 | Pass ([Issue #1](https://github.com/chainreactors/okr-creator/issues/1)) |
| `@claude` 对话续接 + AI 回复 | Pass ([Issue #1 评论](https://github.com/chainreactors/okr-creator/issues/1)) |
| Claude 自证型重新评估 | Pass（接受运行本身作为 KR 完成证据） |

## GitHub Action

`/okr` 运行后自动部署以下文件到目标项目：

```
.github/
├── workflows/
│   ├── okr-review.yml     # 每日 UTC 02:00 自动评估
│   └── okr-chat.yml       # Issue 评论 @claude/@codex 对话
└── prompts/
    └── okr-review.md      # Codex 评审 prompt
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
git add .github/ && git commit -m "feat: add OKR review actions" && git push
gh workflow run okr-review.yml
```

### 每日评估

- 每天 UTC 02:00 自动运行（也可手动触发）
- Claude/Codex 读取 OKR → 逐条运行 Harness → 生成 Markdown 评估报告
- 自动创建季度 Issue `[OKR Review] YYYY-QN 进度追踪`
- 每日追加评估评论，包含进度、证据、建议、PUA 点评

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

### 技术细节

- 使用 `npm install -g @anthropic-ai/claude-code` 安装 CLI，**不依赖 GitHub App**
- `claude -p` 非交互模式 + `--output-format text`
- 支持 `ANTHROPIC_BASE_URL` 自定义 API 端点（兼容代理）
- Codex 使用 `codex exec --approval-mode full-auto`
- 自动创建 `okr-review` label

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
├── skills/okr-creator/SKILL.md    # 核心 skill（含 Action 模板）
├── commands/okr.md                # /okr slash 命令
├── .claude/skills/okr/SKILL.md    # 自举：本项目自身的 OKR（dogfooding）
├── .claude-plugin/                # Claude Code marketplace 配置
├── .codebuddy-plugin/             # CodeBuddy marketplace 配置
├── .github/workflows/
│   ├── okr-review.yml             # 每日 OKR 自动评估（自举用）
│   ├── okr-chat.yml               # Issue 评论 @claude/@codex 对话
│   ├── release.yml                # Tag 触发自动发布
│   └── lint.yml                   # Markdown lint + frontmatter 校验
├── .github/prompts/
│   └── okr-review.md              # Codex 评审 prompt
├── .markdownlint.json             # Markdown lint 规则
├── README.md
├── LICENSE
└── .gitignore
```

## License

MIT

## Credits

By [chainreactors](https://github.com/chainreactors) & [M09ic](https://github.com/M09ic)
