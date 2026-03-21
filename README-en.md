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

OKR Creator doesn't just generate goals — it builds a complete **project improvement engine**: SKILL.md defines direction and execution protocol, PROGRESS.md persists progress memory, GitHub Actions perform daily deep reviews with actionable suggestions, and optional alignment checks keep every PR on target.

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
|  + Weekly breakdown |     |  + PROGRESS.md   |
|  + Pattern matching |     |  Write & verify  |
+-------------------+     +--------+---------+
                                    |
+-------------------------------------------+
|  Step 7: Deploy GitHub Action              |
|                                            |
|  okr-review.yml  -> Deep review + auto PR  |
|  okr-chat.yml    -> @claude/@codex chat    |
|  okr-review.md   -> Review prompt (shared) |
|  [opt] okr-align-check.yml -> PR check     |
+-------------------------------------------+
           |
+-------------------------------------------+
|  Improvement Engine (continuous)           |
|                                            |
|  Daily 02:00:                              |
|    Read SKILL.md + PROGRESS.md             |
|    -> 5-phase deep review                  |
|    -> Root cause + dependencies + actions  |
|    -> Issue comment + auto PR for progress |
|                                            |
|  Every PR (optional):                      |
|    -> OKR alignment check -> PR comment    |
|                                            |
|  Daily dev:                                |
|    -> Execution protocol guides each task  |
+-------------------------------------------+
```

## Core Capabilities

1. **Full Diagnosis** — Six-dimension analysis of project status (vision, quality, debt, architecture, docs, automation)
2. **Co-created OKRs** — Guided rhetoric helps users clarify direction, combined with diagnostics to generate measurable OKRs
3. **Harness-driven** — Every KR must have a verifiable acceptance method; a KR without a harness is waste paper
4. **Execution Protocol** — SKILL.md includes task alignment checks, priority recommendations, and weekly KR breakdowns to actively guide every AI task
5. **PROGRESS.md Memory** — Persistent progress file so AI reviews don't start from zero; supports trend analysis and suggestion tracking
6. **5-Phase Deep Review** — Beyond progress percentages: root cause analysis, cross-KR dependencies, six-dimension trends, prioritized action queue
7. **Auto PR Updates** — Daily review auto-creates PR to update PROGRESS.md; users review and merge
8. **PR Alignment Check (optional)** — Each PR gets a non-blocking comment assessing OKR alignment
9. **Chat Continuation** — Maintainers `@claude` / `@codex` in Issues to discuss OKRs directly with AI
10. **Improvement Pattern Library** — Auto-matched reusable strategies based on diagnosis (testing cold start, doc sprint, etc.)

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
| v2 deep review (root cause + action queue + trends) | Pass |
| PROGRESS.md auto-update PR ([#55](https://github.com/M09Ic/aide-e2e-test/pull/55)) | Pass |
| OKR alignment check Action deployed | Pass |
| Workflow duration | ~2 minutes |

**v2 review output example** (from real Issue #54):

> **Root Cause Analysis**
>
> **O1-KR1** — Type: priority. All commits over 4 days focused on OKR infrastructure, zero code advancing test scenarios. Smallest unblock: create 5 Markdown scenario files in `tests/`.
>
> **Action Queue**
>
> | # | Action | Advances KR | Effort | Why now |
> |---|--------|-------------|--------|---------|
> | 1 | Create tests/ + 5 scenario files | O1-KR1 | S | Critical path start |
> | 2 | New e2e-test.yml CI | O1-KR2 | S | Unblock test chain |
> | 3 | Expand README to 50+ lines | O2-KR1 | S | Independent P0, 30 min |

### Case 2: Bootstrap — okr-creator itself

OKR Creator ran `/okr` on itself, completing the full closed loop (see [Dogfooding](#dogfooding-okr-creator-manages-itself) section above):

| Step | Result |
|------|--------|
| Six-dim diagnosis + OKR generation (5O/14KR) | Pass |
| Daily review Action run | Pass (~2 minutes) |
| Quarterly Issue creation + review comments | Pass ([Issue #1](https://github.com/chainreactors/okr-creator/issues/1)) |
| `@claude` chat continuation + AI reply | Pass ([Issue #1 comments](https://github.com/chainreactors/okr-creator/issues/1)) |
| Claude self-proving re-evaluation | Pass (accepted the run itself as KR completion evidence) |

## GitHub Action & Skill Interaction

The core of OKR isn't just "setting goals" — it's the synergy between Skill and Action that creates a continuous improvement loop:

| Component | Location | Role |
|-----------|----------|------|
| **SKILL.md** | `.claude/skills/okr/SKILL.md` | OKR definition + execution protocol + improvement patterns + weekly KR breakdown |
| **PROGRESS.md** | `.claude/skills/okr/PROGRESS.md` | AI's "memory" — progress snapshot, action queue, review history |
| **okr-review.yml** | `.github/workflows/` | Daily deep review + auto PR for progress updates |
| **okr-chat.yml** | `.github/workflows/` | Issue @claude/@codex chat continuation |
| **okr-review.md** | `.github/prompts/` | 5-phase review prompt (shared by Claude/Codex) |
| **okr-align-check.yml** | `.github/workflows/` | [Optional] PR alignment check |

### Deployed File Structure

```
.claude/skills/okr/
├── SKILL.md              # OKR + execution protocol + patterns + weekly breakdown
└── PROGRESS.md           # Progress record (auto-maintained by Action)

.github/
├── workflows/
│   ├── okr-review.yml    # Daily deep review + auto PR
│   ├── okr-chat.yml      # @claude/@codex chat
│   └── okr-align-check.yml  # [Optional] PR alignment check
└── prompts/
    ├── okr-review.md     # Review prompt (Claude/Codex shared)
    └── okr-align-check.md   # [Optional] Alignment check prompt
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
git add .github/ .claude/ && git commit -m "feat: add OKR review actions" && git push
gh workflow run okr-review.yml
```

### 5-Phase Deep Review

Daily reviews go far beyond simple progress tracking:

| Phase | Content | Value |
|-------|---------|-------|
| Phase 1 | Load SKILL.md + PROGRESS.md | No cold start — has historical memory |
| Phase 2 | Per-KR Harness + **root cause analysis** | Not just "0%" — tells you **why it's stuck** and the **smallest unblock action** |
| Phase 3 | Cross-KR dependencies + Objective health | Find blocking chains, know which unlock releases the most value |
| Phase 4 | Trend analysis + suggestion tracking | Compare with last review, auto-escalate stalled KRs, check if previous suggestions were acted on |
| Phase 5 | Prioritized action queue + roast | Not "write more tests" but "add frontmatter check job to lint.yml, effort: S" |

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

## How to Use OKR to Improve Your Project

OKR Creator is designed not just to "set OKRs" — but to make OKRs actually drive project improvement:

### 1. Generate: Let AI understand your project

Run `/okr:create`. AI diagnoses, aligns with your intent, and generates OKR with execution protocol. Don't skip the intent challenge — your direction determines OKR quality.

### 2. Daily dev: Let OKR guide every task

The **execution protocol** in SKILL.md activates automatically when AI works in your project:

- Before starting a task, AI checks "Which KR does this relate to?"
- If P0 KRs are incomplete, AI suggests handling the bottom line first
- After completion, AI annotates `[O1-KR1.1]` to record the contribution

### 3. Daily review: Get actionable improvement advice

Daily reviews tell you not just "X% complete" but:

- **Why it's stuck** — root cause analysis pointing to specific files, configs, decisions
- **Smallest unblock action** — a concrete 1-2 hour task
- **What to do first** — prioritized action queue with effort estimates
- **Trend warnings** — continuously stalled KRs auto-escalate

### 4. Feedback loop: Suggest → Execute → Track

Review suggestions persist in PROGRESS.md's action queue. Next review checks: acted on? Effect? Ignored? Escalate.

### 5. PR alignment: Every commit has direction

Enable optional `okr-align-check` — every PR gets a non-blocking comment with KR association, priority check, and progress estimate.

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
├── skills/okr-creator/
│   ├── SKILL.md                   # Core skill — 8-step execution flow
│   ├── agents/                    # Specialized agent definitions
│   │   ├── diagnostician.md       # Six-dimension diagnosis
│   │   ├── interviewer.md         # User intent challenge
│   │   └── reviewer.md            # OKR quality review
│   ├── templates/                 # Deployable Action templates
│   │   ├── okr-review.yml         # Daily deep review + auto PR
│   │   ├── okr-chat.yml           # Issue chat continuation
│   │   ├── okr-review.md          # Review prompt (Claude/Codex shared)
│   │   ├── okr-align-check.yml    # [Optional] PR alignment check
│   │   └── okr-align-prompt.md    # [Optional] Alignment check prompt
│   ├── references/
│   │   ├── schemas.md             # Data structure definitions
│   │   ├── templates.md           # SKILL.md output template
│   │   └── patterns.md            # Improvement pattern library (8 patterns)
│   └── flavors/                   # Corporate roast flavor packs
├── commands/create.md             # /okr:create slash command
├── .claude/skills/okr/
│   ├── SKILL.md                   # Bootstrap: this project's own OKR
│   └── PROGRESS.md                # Bootstrap: progress record
├── .claude-plugin/                # Claude Code marketplace config
├── .codebuddy-plugin/             # CodeBuddy marketplace config
├── README.md
├── README-en.md
├── LICENSE
└── .gitignore
```

## License

MIT

## Credits

By [chainreactors](https://github.com/chainreactors) & [M09ic](https://github.com/M09ic)
