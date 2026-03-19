#!/usr/bin/env python3
"""Run evals for OKR Creator skill.

Tests skill triggering accuracy and output quality by running eval cases
through `claude -p` and checking assertions.

Usage:
    python scripts/run_eval.py                    # Run all evals
    python scripts/run_eval.py --filter trigger   # Run only trigger evals
    python scripts/run_eval.py --dry-run          # Show what would run
"""

import json
import subprocess
import sys
import time
from pathlib import Path


EVALS_PATH = Path(__file__).parent.parent / "evals" / "evals.json"
RESULTS_DIR = Path(__file__).parent.parent / "evals" / "results"


def load_evals(filter_str: str | None = None) -> list[dict]:
    """Load eval cases, optionally filtered by ID substring."""
    with open(EVALS_PATH, encoding="utf-8") as f:
        evals = json.load(f)
    if filter_str:
        evals = [e for e in evals if filter_str in e["id"]]
    return evals


def run_single_eval(eval_case: dict) -> dict:
    """Run a single eval case and return result."""
    eval_id = eval_case["id"]
    prompt = eval_case["prompt"]
    start = time.time()

    result = {
        "id": eval_id,
        "name": eval_case["name"],
        "prompt": prompt,
        "should_trigger": eval_case["should_trigger"],
        "pass": False,
        "duration_ms": 0,
        "output": "",
        "error": None,
        "assertions": [],
    }

    try:
        proc = subprocess.run(
            ["claude", "-p", prompt, "--output-format", "stream-json"],
            capture_output=True,
            text=True,
            timeout=120,
        )
        result["output"] = proc.stdout
        result["duration_ms"] = int((time.time() - start) * 1000)

        # Check if skill was triggered by looking for tool_use events
        triggered = "okr-creator" in proc.stdout or "okr:okr-creator" in proc.stdout

        if eval_case["should_trigger"]:
            result["pass"] = triggered
            if not triggered:
                result["error"] = "Skill was NOT triggered but should have been"
        else:
            result["pass"] = not triggered
            if triggered:
                result["error"] = "Skill WAS triggered but should NOT have been"

    except subprocess.TimeoutExpired:
        result["error"] = "Timeout (120s)"
        result["duration_ms"] = 120000
    except FileNotFoundError:
        result["error"] = "claude CLI not found — install with: npm i -g @anthropic-ai/claude-code"
        result["duration_ms"] = 0

    return result


def run_all(evals: list[dict], dry_run: bool = False) -> list[dict]:
    """Run all eval cases and return results."""
    results = []
    total = len(evals)

    for i, ev in enumerate(evals, 1):
        print(f"[{i}/{total}] {ev['id']}: {ev['name']}", end="")
        if dry_run:
            print(" (dry-run, skipped)")
            continue

        r = run_single_eval(ev)
        status = "✅" if r["pass"] else "❌"
        print(f" — {status} ({r['duration_ms']}ms)")
        if r["error"]:
            print(f"         ↳ {r['error']}")
        results.append(r)

    return results


def print_summary(results: list[dict]):
    """Print summary statistics."""
    if not results:
        return

    total = len(results)
    passed = sum(1 for r in results if r["pass"])
    failed = total - passed
    avg_ms = sum(r["duration_ms"] for r in results) // total

    print(f"\n{'='*50}")
    print(f"Results: {passed}/{total} passed ({passed/total*100:.0f}%)")
    print(f"Failed:  {failed}")
    print(f"Avg time: {avg_ms}ms")

    if failed > 0:
        print(f"\nFailed evals:")
        for r in results:
            if not r["pass"]:
                print(f"  ❌ {r['id']}: {r['error']}")


def main():
    filter_str = None
    dry_run = False

    for arg in sys.argv[1:]:
        if arg == "--dry-run":
            dry_run = True
        elif arg.startswith("--filter"):
            # --filter=xxx or --filter xxx
            if "=" in arg:
                filter_str = arg.split("=", 1)[1]
            else:
                idx = sys.argv.index(arg)
                if idx + 1 < len(sys.argv):
                    filter_str = sys.argv[idx + 1]

    evals = load_evals(filter_str)
    print(f"Loaded {len(evals)} eval(s) from {EVALS_PATH}")
    if filter_str:
        print(f"Filter: '{filter_str}'")
    print()

    results = run_all(evals, dry_run=dry_run)

    if not dry_run:
        print_summary(results)

        # Save results
        RESULTS_DIR.mkdir(parents=True, exist_ok=True)
        ts = time.strftime("%Y%m%d-%H%M%S")
        out_path = RESULTS_DIR / f"run-{ts}.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        print(f"\nResults saved to {out_path}")


if __name__ == "__main__":
    main()
