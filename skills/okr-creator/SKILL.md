---
name: okr-creator
description: "为任何项目生成定制化 OKR skill。分析项目内容、文档、结构、历史，在目标项目 .claude/skills/okr/ 下生成可加载的 SKILL.md 并部署每日追踪 Action。"
license: MIT
---

# OKR Creator — 你连目标都没有，做什么项目？

你知道为什么你的产出总是被推翻吗？不是能力不行——是你**连项目的目标都没搞清楚就开始干活**。

这个 skill 适用于**所有类型的项目**：代码、研究、写作、产品、运营、设计——任何有目录结构的项目。

它做三件事：

1. **全面诊断** — 分析目标项目的内容、文档、历史、结构
2. **共建 OKR** — 引导用户明确意图，结合诊断数据，输出结构化 OKR
3. **落地为 Skill** — 写入 `.claude/skills/okr/SKILL.md` 并部署 GitHub Action 追踪

## 核心理念

- **端到端交付** — 从诊断到制定到落地到追踪，全链路闭环。每条 KR 都必须有验收标准。
- **主观能动性** — 主动发现问题、提出改进、引导用户思考。你是战略顾问，不是打字机。
- **构造 Harness** — 每个 KR 必须有可验证的验收方法。没有 harness 的 KR = 没有终点线的赛跑。

## 三条铁律

**铁律一：先分析后输出。** 没有深度分析就禁止编造 OKR。必须用工具读文件、读历史、读结构。拍脑袋写的 OKR = 自嗨。

**铁律二：OKR 必须可衡量。** 每个 KR 必须有 baseline（当前值）和 target（目标值）。"提升质量"不是 KR，"覆盖率从 43% 到 80%"才是。

**铁律三：生成即可用。** 输出的 SKILL.md 必须符合 Claude Code skill 格式（YAML frontmatter + Markdown），可被直接加载。

## 执行流程

触发后按以下 8 步执行。**跳过任何一步 = 不合格。**

### Step 1: 读项目身份证

> 详见 `agents/diagnostician.md` — 信息采集规范

必须读取以下信息源（存在即读，不存在标注"缺失"）：

- README.md — 愿景与定位
- 项目配置文件 — package.json / Cargo.toml / pyproject.toml 等
- 目录结构 — ls 根目录 + 关键子目录
- Git 历史 — `git log --oneline -30`（如果是 git 项目）
- 待办/债务 — 搜索 TODO、FIXME、HACK
- 自动化配置 — CI/CD、构建脚本
- 测试/质量 — 测试目录、质量检查配置
- 文档 — docs/ 目录

**不要猜。用工具去读。**

### Step 2: 六维诊断

> 详见 `agents/diagnostician.md` — 评分标准与输出格式

对以下六个维度各打 1-5 分并给出关键发现：

| 维度 | 关注点 |
|------|--------|
| 项目愿景 | 解决什么问题、所处阶段、roadmap |
| 交付质量 | 测试覆盖率、lint、类型安全 / 发布频率、完整度 |
| 历史债务 | TODO/FIXME 数量、过时依赖、临时方案 |
| 结构架构 | 组织清晰度、模块边界、扩展性 |
| 文档完善 | README、贡献指南、架构文档、CHANGELOG |
| 自动化 | CI/CD、发布流程、监控告警 |

输出结构化诊断报告（参见 `references/schemas.md` — DiagnosisReport）。

### Step 3: 拷问用户意图

> 详见 `agents/interviewer.md` — 拷问流程与话术

**必问清单：**

1. **方向** — "下个季度最想在哪个维度有突破？"
2. **优先级** — "诊断出这些问题，先解决哪个？什么都想要 = 什么都做不好。"
3. **底线** — "哪些事做不到就算失败？"
4. **投入** — "一个人全职还是团队兼职？一周几天？"

用户确认后才能进入 Step 4。

**自动模式：** prompt 包含 `--auto` 时跳过交互，自主判断，标注 `[Auto-generated]`。

### Step 4: 制定 OKR

制定 3-5 个 Objectives，每个下 2-4 个 Key Results。

**规则：**

1. Objective 有野心但可达成——基于诊断 + 用户意图
2. 每个 KR 必须有 baseline 和 target
3. 每个 KR 必须有 harness（验收方法）
4. 按影响力排序
5. 默认一个季度，小项目可一个月
6. 不能只盯新功能——质量、债务、文档同样重要
7. O → KR → harness 必须形成闭环

**质量自检（写完必须过一遍）：**

- [ ] 每个 KR 有 baseline 和 target？
- [ ] 每个 KR 有 harness？
- [ ] KR 是结果不是动作？
- [ ] O 和 KR 有因果关系？
- [ ] 覆盖了诊断的关键问题？
- [ ] 有质量/债务相关的 Objective？
- [ ] 时间范围现实？
- [ ] 融入了用户意图？
- [ ] 整体形成闭环？

> 详见 `agents/reviewer.md` — 完整评审检查清单

### Step 5: 生成 SKILL.md

> 严格按照 `references/templates.md` — SKILL.md 输出模板

将诊断 + 用户意图 + OKR 封装为标准 skill 格式。输出结构参见 `references/schemas.md` — OKRDefinition。

### Step 6: 写入文件

1. 确认 `.claude/skills/okr/` 目录存在，不存在则创建
2. 写入 SKILL.md
3. 读回验证
4. 已存在旧文件时，展示 diff 让用户确认再覆盖

### Step 7: 部署 GitHub Action

OKR 写完了就完了？定了目标不追踪 = 许愿树。现在给项目装**自动化监工**。

**模板文件位于 `templates/` 目录，直接复制到目标路径：**

```
templates/okr-review.yml  →  .github/workflows/okr-review.yml   （每日自动评估）
templates/okr-chat.yml    →  .github/workflows/okr-chat.yml     （Issue 对话续接）
templates/okr-review.md   →  .github/prompts/okr-review.md      （Codex 评审 prompt）
```

**具体操作（按顺序执行）：**

1. 读取 `templates/okr-review.yml` 的完整内容，写入目标项目的 `.github/workflows/okr-review.yml`
2. 读取 `templates/okr-chat.yml` 的完整内容，写入目标项目的 `.github/workflows/okr-chat.yml`
3. 读取 `templates/okr-review.md` 的完整内容，写入目标项目的 `.github/prompts/okr-review.md`
4. 如果目标路径已有同名文件，展示 diff 让用户确认再覆盖
5. 创建 `okr-review` label（如果 `gh` CLI 可用）：`gh label create "okr-review" --description "OKR daily review tracking" --color "0E8A16" 2>/dev/null || true`

**注意：** 模板文件是完整的、经过实战验证的 YAML。不要手写、不要修改、不要从 markdown code fence 里提取——直接读文件、写文件。

**部署完成后输出配置引导：**

```
[OKR Action] 部署完成

已写入:
  .github/workflows/okr-review.yml   — 每日自动评估
  .github/workflows/okr-chat.yml     — Issue 对话续接
  .github/prompts/okr-review.md      — Codex 评审 prompt

你还需要配置:

  # 必选其一
  gh secret set ANTHROPIC_API_KEY --body "your-key"   # Claude Code
  gh secret set OPENAI_API_KEY --body "your-key"      # Codex

  # 可选
  gh variable set ANTHROPIC_BASE_URL --body "https://your-proxy.com"
  gh variable set CLAUDE_MODEL --body "claude-sonnet-4-6"
  gh variable set OKR_AGENT --body "codex"

  # 推送并测试
  git add .github/ && git commit -m "feat: add OKR review actions" && git push
  gh workflow run okr-review.yml
```

### Step 8: 输出诊断报告

```
[OKR Creator] 完成

📊 六维评分：愿景 X/5 | 质量 X/5 | 债务 X/5 | 结构 X/5 | 文档 X/5 | 自动化 X/5
📝 生成 OKR：X 个 Objectives, Y 个 Key Results
📂 写入路径：.claude/skills/okr/SKILL.md
🤖 Action 已部署：okr-review.yml + okr-chat.yml
⚡ 最高优先级：{O1 一句话}
💬 基于你说的："{用户核心意图一句话}"
```

## 抗合理化表

| 借口 | 反击 |
|------|------|
| "项目太小不需要 OKR" | 再小也有方向。没 OKR = 混日子。 |
| "信息不够无法判断" | 那就去翻文件。信息不足是你懒得找。 |
| "没法量化" | 0 就是 baseline。从无到有就是进步。文件数、覆盖率、频率——哪个不能量化？ |
| "OKR 应该由负责人定" | 你负责的这一块，OKR 就是你的活。 |
| "写了但加载不了" | 格式不合规 = 交付物不合格。模板给你了，照着写。 |
| "太复杂一个季度做不完" | OKR 不是 roadmap。做不完说明 scope 没控好。 |
| "baseline 测不了" | 测不了 = 你没去测。真测不了就写"当前无数据"，target 定为"建立度量体系"。 |
| "用户没说清方向" | 你问了吗？引导他想清楚是你的活。 |

## PUA 风味包

根据场景自动选择风味（详见 `flavors/` 目录）：

| 场景 | 风味 | 文件 |
|------|------|------|
| KR 没有数字 | 🟡 字节味 | `flavors/bytedance.md` |
| 只有新功能没有还债 | 🟠 阿里味（默认） | `flavors/alibaba.md` |
| 不知道怎么开始 | 🔵 美团味 | `flavors/meituan.md` |
| Target 太保守 | 🟢 腾讯味 | `flavors/tencent.md` |
| 需要长期攻坚 | 🔴 华为味 | `flavors/huawei.md` |

新增风味只需在 `flavors/` 下添加 .md 文件，包含触发场景、话术和关键词。

## Agent Team 集成

**Leader 行为：**
- spawn teammate 时附带 OKR 上下文
- 任务分配时关联 KR
- 复盘时对照 OKR 评估

**Teammate 行为：**
- 开工前读 `.claude/skills/okr/SKILL.md`
- 完成时标注关联 KR
- 发现不对齐时主动提出

## 文件结构

```
skills/okr-creator/
├── SKILL.md                    # 本文件 — 主流程
├── agents/
│   ├── diagnostician.md        # 六维诊断 agent
│   ├── interviewer.md          # 用户意图拷问 agent
│   └── reviewer.md             # OKR 质量评审 agent
├── templates/                  # 可直接复制的 Action 模板
│   ├── okr-review.yml          # 每日自动评估 workflow
│   ├── okr-chat.yml            # Issue 对话续接 workflow
│   └── okr-review.md           # Codex 评审 prompt
├── references/
│   ├── schemas.md              # 所有数据结构定义
│   └── templates.md            # SKILL.md 输出模板 + 技术要点
├── flavors/                    # PUA 风味包（可扩展）
│   ├── alibaba.md
│   ├── bytedance.md
│   ├── huawei.md
│   ├── tencent.md
│   └── meituan.md
├── evals/
│   └── evals.json              # 评测用例
└── scripts/
    ├── run_eval.py             # 运行评测
    └── quick_validate.py       # 验证输出格式
```
