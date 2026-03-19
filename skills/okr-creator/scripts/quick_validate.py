#!/usr/bin/env python3
"""Quick validation for OKR Creator SKILL.md output.

Validates:
1. YAML frontmatter (name, description, license)
2. Required sections exist
3. KR table structure
4. Harness presence
"""

import io
import re
import sys
from pathlib import Path

# Ensure UTF-8 output on Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")


def validate_frontmatter(content: str) -> list[str]:
    """Check YAML frontmatter has required fields."""
    errors = []
    fm_match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not fm_match:
        return ["Missing YAML frontmatter (--- delimiters)"]

    fm = fm_match.group(1)
    for field in ("name:", "description:", "license:"):
        if field not in fm:
            errors.append(f"Frontmatter missing '{field.rstrip(':')}'")

    if "name:" in fm:
        name_match = re.search(r"^name:\s*(.+)$", fm, re.MULTILINE)
        if name_match:
            name = name_match.group(1).strip().strip('"').strip("'")
            if name != "okr":
                errors.append(f"name should be 'okr', got '{name}'")

    return errors


def validate_sections(content: str) -> list[str]:
    """Check required sections exist."""
    errors = []
    required = [
        ("项目概况", "## 项目概况"),
        ("六维诊断", "六维诊断"),
        ("OKR", "## OKR"),
        ("O1", "### O1:"),
        ("工作指引", "## 工作指引"),
    ]
    for name, marker in required:
        if marker not in content:
            errors.append(f"Missing section: {name} (expected '{marker}')")
    return errors


def validate_kr_tables(content: str) -> list[str]:
    """Check KR tables have baseline, target, harness."""
    errors = []
    objectives = re.findall(r"### O\d+:.*?(?=### O\d+:|## |\Z)", content, re.DOTALL)

    if not objectives:
        errors.append("No Objectives found (### O1: ...)")
        return errors

    for obj in objectives:
        obj_id = re.search(r"### (O\d+):", obj)
        oid = obj_id.group(1) if obj_id else "O?"

        if "Baseline" not in obj and "baseline" not in obj.lower():
            errors.append(f"{oid}: KR table missing 'Baseline' column")
        if "Target" not in obj and "target" not in obj.lower():
            errors.append(f"{oid}: KR table missing 'Target' column")
        if "Harness" not in obj and "harness" not in obj.lower():
            errors.append(f"{oid}: KR table missing 'Harness' column")

        # Match any line starting with | (table rows may not end with | if cells contain pipes)
        kr_rows = re.findall(r"^\|.+", obj, re.MULTILINE)
        # Exclude header row (contains "KR" as column label) and separator rows (----)
        data_rows = [
            r for r in kr_rows
            if not re.match(r"^\|\s*[-:]+", r)
            and not re.match(r"^\|\s*KR\s*\|", r)
        ]
        if not data_rows:
            errors.append(f"{oid}: No KR data rows found in table")

    return errors


def validate_file(path: str) -> tuple[bool, list[str]]:
    """Validate a generated OKR SKILL.md file."""
    p = Path(path)
    if not p.exists():
        return False, [f"File not found: {path}"]

    content = p.read_text(encoding="utf-8")
    errors = []
    errors.extend(validate_frontmatter(content))
    errors.extend(validate_sections(content))
    errors.extend(validate_kr_tables(content))

    return len(errors) == 0, errors


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else ".claude/skills/okr/SKILL.md"
    ok, errors = validate_file(path)

    if ok:
        print(f"✅ PASS — {path}")
        sys.exit(0)
    else:
        print(f"❌ FAIL — {path}")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
