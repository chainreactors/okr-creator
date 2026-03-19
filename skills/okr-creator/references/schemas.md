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

## 5. Eval 用例 (EvalCase)

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

## 6. Benchmark 结果 (BenchmarkResult)

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
