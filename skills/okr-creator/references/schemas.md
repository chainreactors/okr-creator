# OKR Creator — 数据结构定义

本文件定义 OKR Creator 各阶段的输入输出数据结构。所有 agent 和脚本都应遵循这些 schema。

## 1. 诊断报告 (DiagnosisReport)

diagnostician agent 的输出。

```json
{
  "$schema": "diagnosis",
  "project": {
    "name": "string — 项目名称",
    "summary": "string — 一句话项目定位",
    "stage": "exploring | growing | stable | maintenance",
    "tech_stack": ["string — 技术栈/内容体系标签"],
    "repo_url": "string | null"
  },
  "dimensions": {
    "vision":       { "score": "1-5", "finding": "string" },
    "quality":      { "score": "1-5", "finding": "string" },
    "debt":         { "score": "1-5", "finding": "string" },
    "architecture": { "score": "1-5", "finding": "string" },
    "docs":         { "score": "1-5", "finding": "string" },
    "automation":   { "score": "1-5", "finding": "string" }
  },
  "top_issues": ["string — 最多 5 个关键问题"],
  "next_milestone": "string — 建议的下一个里程碑",
  "raw_data": {
    "todo_count": "number",
    "test_coverage": "number | null — 百分比",
    "recent_commits": "number — 近 30 天提交数",
    "open_issues": "number | null",
    "doc_files": "number"
  }
}
```

## 2. 用户意图 (UserIntent)

interviewer agent 的输出。

```json
{
  "$schema": "user_intent",
  "direction": "string — 用户明确的方向",
  "priority_focus": ["string — 优先关注的维度"],
  "bottom_line": ["string — P0 底线，做不到算失败"],
  "investment": "full_sprint | primary | part_time | low_priority",
  "auto_mode": "boolean",
  "raw_intent": "string — 用户原话"
}
```

## 3. OKR 定义 (OKRDefinition)

核心输出结构，用于生成 SKILL.md。

```json
{
  "$schema": "okr_definition",
  "time_range": {
    "quarter": "2026-Q2",
    "start": "2026-04-01",
    "end": "2026-06-30"
  },
  "objectives": [
    {
      "id": "O1",
      "title": "string — Objective 标题",
      "tagline": "string — PUA 风格的一句话点评",
      "key_results": [
        {
          "id": "KR1.1",
          "description": "string — KR 描述",
          "baseline": "string — 当前值",
          "target": "string — 目标值",
          "harness": "string — 验收方法（可执行的命令或可检查的条件）",
          "priority": "P0 | P1 | P2"
        }
      ]
    }
  ],
  "priority_baseline": {
    "P0": ["KR1.1", "KR1.2"],
    "P1": ["KR2.1"],
    "P2": ["KR3.3"]
  }
}
```

## 4. 评审结果 (ReviewResult)

reviewer agent 的输出。

```json
{
  "$schema": "review_result",
  "verdict": "pass | fail",
  "checks": [
    {
      "id": "number",
      "name": "string — 检查项名称",
      "pass": "boolean",
      "evidence": "string — 判定依据",
      "issues": ["string — 具体问题描述"]
    }
  ],
  "pass_count": "number",
  "fail_count": "number",
  "summary": "string",
  "suggestions": ["string"]
}
```

## 5. 每日评审报告 (DailyReviewReport)

每日评审 Action 的输出结构。

```json
{
  "$schema": "daily_review",
  "date": "ISO 8601 date",
  "review_sequence": "number — 本季度第 N 次评审",
  "objectives": [
    {
      "id": "O1",
      "title": "string",
      "health": "healthy | at_risk | critical",
      "key_results": [
        {
          "id": "KR1.1",
          "description": "string",
          "progress_pct": "number 0-100",
          "status": "completed | on_track | at_risk | blocked | not_started",
          "evidence": "string — 实际命令输出或文件内容",
          "root_cause": "string | null — 仅 at_risk/blocked",
          "root_cause_type": "resource | knowledge | dependency | priority | null",
          "unblock_action": "string | null — 最小解锁动作",
          "velocity": "accelerating | steady | decelerating | stalled | null",
          "prev_progress_pct": "number | null",
          "stalled_days": "number — 连续停滞天数"
        }
      ]
    }
  ],
  "six_dimensions": {
    "vision":       { "score": "1-5", "delta": "number", "note": "string" },
    "quality":      { "score": "1-5", "delta": "number", "note": "string" },
    "debt":         { "score": "1-5", "delta": "number", "note": "string" },
    "architecture": { "score": "1-5", "delta": "number", "note": "string" },
    "docs":         { "score": "1-5", "delta": "number", "note": "string" },
    "automation":   { "score": "1-5", "delta": "number", "note": "string" }
  },
  "cross_kr_insights": ["string — 依赖链、共同根因等"],
  "action_queue": [
    {
      "rank": "number",
      "action": "string — 具体任务描述",
      "advances_kr": "string — KR ID",
      "effort": "small | medium | large",
      "rationale": "string — 为什么现在做"
    }
  ],
  "previous_actions_status": [
    {
      "action": "string",
      "status": "done | pending | skipped",
      "note": "string | null"
    }
  ],
  "pua_commentary": "string"
}
```

## 6. 进展文件 (ProgressFile)

`.claude/skills/okr/PROGRESS.md` 的结构化表示，由每日评审自动维护。

```json
{
  "$schema": "progress_file",
  "last_updated": "ISO 8601 date",
  "kr_snapshot": [
    {
      "id": "KR1.1",
      "description": "string",
      "progress_pct": "number 0-100",
      "status": "completed | on_track | at_risk | blocked | not_started",
      "last_change_date": "ISO 8601 date | null",
      "stalled_days": "number"
    }
  ],
  "six_dimensions_trend": [
    {
      "dimension": "string",
      "initial": "number 1-5",
      "previous": "number 1-5",
      "current": "number 1-5",
      "trend": "up | flat | down"
    }
  ],
  "action_queue": [
    {
      "rank": "number",
      "action": "string",
      "advances_kr": "string",
      "status": "pending | done | skipped",
      "proposed_date": "ISO 8601 date",
      "completed_date": "ISO 8601 date | null"
    }
  ],
  "review_history": [
    {
      "date": "ISO 8601 date",
      "summary": "string — KR 进度一行摘要",
      "new_actions": ["string"],
      "pua_oneliner": "string"
    }
  ]
}
```

## 7. Eval 用例 (EvalCase)


用于测试 skill 质量的评测用例。

```json
{
  "$schema": "eval_case",
  "id": "string — 用例 ID",
  "name": "string — 用例名称",
  "prompt": "string — 触发 prompt",
  "should_trigger": "boolean — 是否应该触发此 skill",
  "context": {
    "project_type": "code | writing | research | ops | product | design",
    "has_readme": "boolean",
    "has_git": "boolean",
    "file_count": "number"
  },
  "assertions": [
    {
      "type": "file_exists | contains | format_valid | score_range",
      "target": "string — 检查目标",
      "expected": "string — 期望值"
    }
  ]
}
```

## 8. Benchmark 结果 (BenchmarkResult)

eval 运行的汇总统计。

```json
{
  "$schema": "benchmark",
  "timestamp": "ISO 8601",
  "skill_version": "string",
  "total_evals": "number",
  "pass_rate": "number — 0-1",
  "trigger_accuracy": "number — 0-1",
  "per_eval": [
    {
      "id": "string",
      "pass": "boolean",
      "duration_ms": "number",
      "assertions_pass": "number",
      "assertions_total": "number"
    }
  ],
  "mean_duration_ms": "number",
  "notes": "string"
}
```
