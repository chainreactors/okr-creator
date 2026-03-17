# okr

## AI-powered OKR Creator — Give Your Project Direction, Hold It Accountable

> A [PUA](https://github.com/tanweai/pua)-like project — built on the PUA skill's philosophy and rhetoric system, focused on project goal management. PUA keeps AI from slacking off, OKR tells AI where to push.

<p>
  <img src="https://img.shields.io/badge/Claude_Code-black?style=flat-square&logo=anthropic&logoColor=white" alt="Claude Code">
  <img src="https://img.shields.io/badge/OpenAI_Codex_CLI-412991?style=flat-square&logo=openai&logoColor=white" alt="OpenAI Codex CLI">
  <img src="https://img.shields.io/badge/CodeBuddy-00B2FF?style=flat-square&logo=tencent-qq&logoColor=white" alt="CodeBuddy">
  <img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="MIT License">
</p>

> Your project has no goals — what are you even building?

An AI Agent skill that analyzes any project and generates customized OKR (Objectives and Key Results) skills, with GitHub Action deployment for daily automated tracking. Not limited to code — works for writing, research, ops, product, design, and any project type. Supports **Claude Code**, **OpenAI Codex CLI**, and **CodeBuddy**.

## The Problem: Projects Without Direction

| Pattern | Symptom |
|---------|---------|
| No goals | Work on whatever comes to mind, no idea if it's valuable |
| Vague goals | "Improve quality", "optimize performance" — no numbers, no acceptance criteria |
| Set and forget | OKR written and filed away, remembered next quarter |
| Misaligned team | Team members pulling in different directions, duplicating work |
| Directionless AI | AI works in the repo but has no idea what the priorities are |

## Installation

### Claude Code

```bash
# Option 1: Install via marketplace
claude plugin marketplace add chainreactors/okr-creator
claude plugin install okr-creator@okr-creator

# Option 2: Manual install
git clone https://github.com/chainreactors/okr-creator.git ~/.claude/plugins/okr
```

### OpenAI Codex CLI

```bash
mkdir -p ~/.codex/skills/okr-creator
curl -o ~/.codex/skills/okr-creator/SKILL.md \
  https://raw.githubusercontent.com/chainreactors/okr-creator/main/skills/okr-creator/SKILL.md

# /okr command
mkdir -p ~/.codex/prompts
curl -o ~/.codex/prompts/okr.md \
  https://raw.githubusercontent.com/chainreactors/okr-creator/main/commands/okr.md
```

### CodeBuddy (Tencent)

```bash
# Option 1: Install via marketplace
codebuddy plugin marketplace add chainreactors/okr-creator
codebuddy plugin install okr-creator@okr-creator

# Option 2: Manual install
mkdir -p ~/.codebuddy/skills/okr-creator
curl -o ~/.codebuddy/skills/okr-creator/SKILL.md \
  https://raw.githubusercontent.com/chainreactors/okr-creator/main/skills/okr-creator/SKILL.md
```

## Usage

Type `/okr-creator:okr` in any project. The skill runs the entire flow automatically:

| Step | Action | Description |
|------|--------|-------------|
| 1 | Read project identity | README, config, directory structure, git log, TODOs |
| 2 | Six-dimension diagnosis | Vision, quality, debt, architecture, docs, automation — scored individually |
| 3 | Challenge user intent | "What do you actually want this project to become? What's the priority? Where's the bottom line?" |
| 4 | Define OKRs | 3-5 Objectives, 2-4 KRs each, every KR has a Harness |
| 5-6 | Generate + verify | Write to `.claude/skills/okr/SKILL.md` and read back to confirm |
| 7 | Deploy Action | Write workflows + prompt + create label + output config guide |
| 8 | Output report | Six-dimension scores + OKR summary + top priority |

### Auto Mode (Non-interactive)

For CI/CD or batch scenarios, skip user interaction:

```
Use /okr-creator:okr with --auto flag, do not confirm with humans, execute directly
```

The AI will autonomously determine direction based on diagnostic data and generate OKRs, marked `[Auto-generated]`.

## How It Works

```
+---------------------------------------------------+
|               /okr-creator:okr triggered           |
+----------+----------------------------------------+
           |
+----------v--------+     +------------------+
|  Step 1-2          |     |  Step 3          |
|  Read -> Diagnose  |---->|  Challenge intent|
+-------------------+     +--------+---------+
                                    |
+-------------------+     +--------v---------+
|  Step 4            |     |  Step 5-6        |
|  Define OKRs       |---->|  Generate SKILL  |
|  (Harness-driven)  |     |  Write & verify  |
+-------------------+     +--------+---------+
                                    |
+-------------------------------------------+
|  Step 7: Deploy GitHub Action              |
|                                            |
|  okr-review.yml -> Daily review, Issue     |
|  okr-chat.yml   -> @claude/@codex chat     |
|  okr-review.md  -> Codex review prompt     |
|  okr-review label -> Auto-created          |
+-------------------------------------------+
           |
+-------------------------------------------+
|  Daily Loop                                |
|                                            |
|  UTC 02:00 -> Claude/Codex reviews KRs     |
|  -> Run Harness -> Append Issue comment    |
|  -> Maintainer @claude -> AI replies       |
+-------------------------------------------+
```

## Core Capabilities

1. **Full Diagnosis** — Six-dimension analysis of project status (vision, quality, debt, architecture, docs, automation)
2. **Co-created OKRs** — Guided rhetoric helps users clarify direction, combined with diagnostics to generate measurable OKRs
3. **Harness-driven** — Every KR must have a verifiable acceptance method; a KR without a harness is waste paper
4. **Delivered as Skill** — Output to `.claude/skills/okr/SKILL.md` so AI can reference it every time it works
5. **Auto-deploy Action** — One-click workflow + prompt + label deployment; users just configure their API key
6. **Daily Automated Review** — GitHub Action runs Harness daily, Issue tracks progress
7. **Chat Continuation** — Maintainers `@claude` / `@codex` in Issues to discuss OKRs directly with AI

## Three Core Principles

| Principle | Meaning |
|-----------|---------|
| **End-to-end delivery** | From diagnosis to definition to deployment to tracking — full-chain closed loop. "Did it" doesn't count; "did it and can prove it" does |
| **Proactive initiative** | Proactively find problems, guide user thinking, propose improvements |
| **Construct Harness** | Every KR has a verifiable acceptance framework — the concrete method for "how do I know this KR is done" |

## Dogfooding: OKR Creator Manages Itself

OKR Creator is using its own generated OKR to drive its own iteration — this is **bootstrapping**.

We ran `/okr-creator:okr` on okr-creator itself, completed a six-dimension diagnosis, generated 5 Objectives / 14 Key Results, and deployed the daily review Action. Now, every day at UTC 02:00, Claude automatically checks okr-creator's own OKR progress, runs Harness verification for each KR, and appends a review report to the Issue. Maintainers can `@claude` directly in the Issue to discuss progress and adjust direction.

**Bootstrap verification results:**

| Step | Result | Link |
|------|--------|------|
| Six-dim diagnosis + OKR generation (5O/14KR) | Pass | [`.claude/skills/okr/SKILL.md`](https://github.com/chainreactors/okr-creator/blob/main/.claude/skills/okr/SKILL.md) |
| Daily review Action deploy + run | Pass | [Workflow Runs](https://github.com/chainreactors/okr-creator/actions/workflows/okr-review.yml) |
| Quarterly Issue auto-created + review comments | Pass | [Issue #1: \[OKR Review\] 2026-Q1 Progress Tracking](https://github.com/chainreactors/okr-creator/issues/1) |
| `@claude` chat continuation | Pass | [Issue #1 Comments](https://github.com/chainreactors/okr-creator/issues/1) |

**Daily review output example** (from [Issue #1](https://github.com/chainreactors/okr-creator/issues/1)):

> **O1: Complete Bootstrap Loop — OKR Creator manages itself with its own OKR**
>
> | KR | Progress | Status |
> |----|----------|--------|
> | KR1.1 OKR skill exists and format-compliant | 100% | 🟢 |
> | KR1.2 Daily Review Action runs successfully | 100% | 🟢 |
> | KR1.3 OKR Review Issue exists with review comments | 100% | 🟢 |
>
> **Roast**: You built a tool that "helps others define OKRs," and you did write your own. And then what? E2E is at 0%, the template is still a 700-line monolith, and there's no CONTRIBUTING.md — are you trying to attract contributors or scare them away?

**Chat continuation example** (Maintainer `@claude` in Issue):

> Maintainer: *@claude KR1.2 and KR1.3 are actually done — this very review you're running is the proof.*
>
> Claude: *O1 overall: 100% — P0 bottom line #1 achieved. The previous review misjudged "requires gh run list authorization" as uncertainty. Self-proving evidence (the output you're reading IS the run result) is more reliable.*

This proves OKR Creator's complete closed loop: **diagnose -> define -> deploy -> daily track -> discuss -> adjust** — fully automated, fully visible in GitHub Issues.

## E2E Testing

### Case 1: External Project — aide-e2e-test

End-to-end closed-loop test on [M09Ic/aide-e2e-test](https://github.com/M09Ic/aide-e2e-test):

| Step | Result |
|------|--------|
| Install skill to target repo | Pass |
| Auto Mode generates OKR (3O/7KR) | Pass |
| Deploy GitHub Action | Pass |
| Claude Code CLI install + execute | Pass (npm install -g) |
| Issue auto-created ([#54](https://github.com/M09Ic/aide-e2e-test/issues/54)) | Pass |
| AI review content valid (per-KR evidence + roast) | Pass |
| Workflow duration | ~2 minutes |

**Review output example** (from real Issue #54):

> KR1: Define at least 5 E2E test scenarios — Progress 0% — `tests/` directory does not exist
>
> **Roast**: How much effort did you spend on "the tool that tracks OKRs"? You built a perfect OKR dashboard that live-broadcasts "nothing accomplished." Close this file and go write your first test scenario.

### Case 2: Bootstrap — okr-creator itself

OKR Creator ran `/okr` on itself, completing the full closed loop (see [Dogfooding](#dogfooding-okr-creator-manages-itself) section above):

| Step | Result |
|------|--------|
| Six-dim diagnosis + OKR generation (5O/14KR) | Pass |
| Daily review Action run | Pass (~2 minutes) |
| Quarterly Issue creation + review comments | Pass ([Issue #1](https://github.com/chainreactors/okr-creator/issues/1)) |
| `@claude` chat continuation + AI reply | Pass ([Issue #1 comments](https://github.com/chainreactors/okr-creator/issues/1)) |
| Claude self-proving re-evaluation | Pass (accepted the run itself as KR completion evidence) |

## GitHub Action

After `/okr-creator:okr` runs, the following files are auto-deployed to the target project:

```
.github/
├── workflows/
│   ├── okr-review.yml     # Daily UTC 02:00 automated review
│   └── okr-chat.yml       # Issue comment @claude/@codex chat
└── prompts/
    └── okr-review.md      # Codex review prompt
```

### Configuration (one step after deployment)

```bash
# Required (pick one) — power on the AI
gh secret set ANTHROPIC_API_KEY --body "your-key"   # Claude Code
gh secret set OPENAI_API_KEY --body "your-key"      # Codex

# Optional — custom API endpoint
gh variable set ANTHROPIC_BASE_URL --body "https://your-proxy.com"

# Optional — switch Agent (default: claude)
gh variable set OKR_AGENT --body "codex"

# Push and test
git add .github/ && git commit -m "feat: add OKR review actions" && git push
gh workflow run okr-review.yml
```

### Daily Review

- Runs daily at UTC 02:00 (can also be triggered manually)
- Claude/Codex reads OKR -> runs Harness for each KR -> generates Markdown review report
- Auto-creates quarterly Issue `[OKR Review] YYYY-QN Progress Tracking`
- Daily appended review comments with progress, evidence, suggestions, and roast

### Chat Continuation

Maintainers comment in the OKR Review Issue to chat with AI:

```
@claude The progress assessment for O2-KR1 is wrong, the first draft is actually done
@claude Give me a weekly action plan for O1's blockers
@codex Check if the sync script has been implemented
```

| Role | Daily Review | Chat Continuation |
|------|-------------|-------------------|
| Owner | Auto-receives Issue | `@claude` / `@codex` |
| Member / Collaborator | Can view | `@claude` / `@codex` |
| External users | Can view | **Not triggered** |

### Technical Details

- Uses `npm install -g @anthropic-ai/claude-code` to install CLI, **no GitHub App dependency**
- `claude -p` non-interactive mode + `--output-format text`
- Supports `ANTHROPIC_BASE_URL` custom API endpoint (proxy-compatible)
- Codex uses `codex exec --approval-mode full-auto`
- Auto-creates `okr-review` label

## Corporate Roast Flavor Pack

OKR Creator has built-in corporate roast flavors, auto-selected by context:

| Flavor | Scenario | Example |
|--------|----------|---------|
| Alibaba (default) | KRs not aligned with strategy | "What's the underlying logic of this OKR? Where are the leverage points?" |
| ByteDance | KRs not quantified | "Data talks. 'Do better' is not a KR. 'From X to Y' is." |
| Huawei | Poor execution | "OKRs are not a wish list. They're marching orders." |
| Tencent | Targets too conservative | "Are you sure the target is high enough? Or are you managing expectations?" |
| Meituan | Good on paper, bad in practice | "Next to each KR, write: What's step one? What's today's task?" |

## Pair with PUA

OKR Creator sets direction, PUA ensures execution. Recommended combo:

```bash
claude plugin marketplace add tanweai/pua
```

| Combo | Effect |
|-------|--------|
| `pua:pua` + `okr-creator` | Direction + no slacking |
| `pua:high-agency` + `okr-creator` | Direction + intrinsic drive |

## Project Structure

```
chainreactors/okr-creator/
├── skills/okr-creator/SKILL.md    # Core skill (with Action templates)
├── commands/okr.md                # /okr-creator:okr slash command
├── .claude/skills/okr/SKILL.md    # Bootstrap: this project's own OKR (dogfooding)
├── .claude-plugin/                # Claude Code marketplace config
├── .codebuddy-plugin/             # CodeBuddy marketplace config
├── .github/workflows/
│   ├── okr-review.yml             # Daily OKR automated review (bootstrap)
│   ├── okr-chat.yml               # Issue comment @claude/@codex chat
│   ├── release.yml                # Tag-triggered auto release
│   └── lint.yml                   # Markdown lint + frontmatter validation
├── .github/prompts/
│   └── okr-review.md              # Codex review prompt
├── .markdownlint.json             # Markdown lint rules
├── README.md
├── README-en.md
├── LICENSE
└── .gitignore
```

## License

MIT

## Credits

By [chainreactors](https://github.com/chainreactors) & [M09ic](https://github.com/M09ic)
