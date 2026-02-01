#!/usr/bin/env python3
"""
OpenCode LLM Benchmark - Long-Form Code Generation
Measures real token generation speed of AI coding assistants.

Usage (run inside an AI coding session like Claude Code, OpenCode, Cursor):

    python benchmark.py start 1          # Mark start of test 1
    # AI generates code and writes to benchmark_output/test_1.py
    python benchmark.py submit 1         # Mark end of test 1, measure timing

    ... repeat for tests 2-6 ...

    python benchmark.py report --model "Claude Opus 4.5"   # Generate report
    python benchmark.py prompts          # Show all test prompts
    python benchmark.py reset            # Clear all timing data
"""

import argparse
import json
import os
import sys
import time
from datetime import datetime

DATA_DIR = "benchmark_output"
TIMING_FILE = os.path.join(DATA_DIR, "_timings.json")

TESTS = [
    {
        "id": 1,
        "name": "Micro (Baseline)",
        "prompt": "Say exactly: 'Long-form benchmark test starting now'",
    },
    {
        "id": 2,
        "name": "Small Function",
        "prompt": "Write a Python function to calculate Fibonacci with memoization. Output only the code.",
    },
    {
        "id": 3,
        "name": "Medium Class",
        "prompt": "Create a complete Python Matrix class with add, multiply, transpose, and determinant methods. Output only the code.",
    },
    {
        "id": 4,
        "name": "Large System",
        "prompt": "Implement a complete HTTP REST API server using Flask with authentication, rate limiting, logging, and CRUD operations for a user/item management system. Output only the code.",
    },
    {
        "id": 5,
        "name": "Very Large System",
        "prompt": "Create a complete e-commerce system in Python with Product, Cart, Order, and User classes, including inventory management, discount system, and payment processing. Output only the code.",
    },
    {
        "id": 6,
        "name": "Massive System",
        "prompt": "Build a complete database ORM system in Python with Model base class, Query builder, Migration system, Field types (Integer, String, Float, Boolean, DateTime, ForeignKey), Relationship handling (one-to-many, many-to-many), and Transaction support. Output only the code.",
    },
]


def load_timings():
    if os.path.exists(TIMING_FILE):
        with open(TIMING_FILE) as f:
            return json.load(f)
    return {}


def save_timings(data):
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(TIMING_FILE, "w") as f:
        json.dump(data, f, indent=2)


def cmd_prompts(args):
    """Show all test prompts."""
    print("=" * 70)
    print("BENCHMARK TESTS")
    print("=" * 70)
    for t in TESTS:
        print(f"\nTest {t['id']}: {t['name']}")
        print(f"  Prompt: {t['prompt']}")
        print(f"  Output: benchmark_output/test_{t['id']}.py")
    print()


def cmd_start(args):
    """Record start time for a test."""
    test_id = str(args.test_id)
    timings = load_timings()
    timings[test_id] = {"start": time.time()}
    save_timings(timings)

    test = next((t for t in TESTS if t["id"] == int(test_id)), None)
    if test:
        print(f"[START] Test {test_id}: {test['name']}")
        print(f"Prompt: {test['prompt']}")
        print(f"Write output to: benchmark_output/test_{test_id}.py")
    else:
        print(f"[START] Test {test_id} (unknown)")


def cmd_submit(args):
    """Record end time and calculate metrics."""
    test_id = str(args.test_id)
    timings = load_timings()

    if test_id not in timings or "start" not in timings[test_id]:
        print(f"[ERROR] Test {test_id} was not started. Run: python benchmark.py start {test_id}")
        sys.exit(1)

    end_time = time.time()
    start_time = timings[test_id]["start"]
    duration = end_time - start_time

    # Read output file
    output_file = os.path.join(DATA_DIR, f"test_{test_id}.py")
    if not os.path.exists(output_file):
        print(f"[ERROR] Output file not found: {output_file}")
        sys.exit(1)

    with open(output_file) as f:
        content = f.read()

    char_count = len(content)
    line_count = content.count("\n")
    estimated_tokens = char_count // 4
    tps = estimated_tokens / duration if duration > 0 else 0

    timings[test_id].update({
        "end": end_time,
        "duration": round(duration, 2),
        "characters": char_count,
        "lines": line_count,
        "tokens": estimated_tokens,
        "tps": round(tps, 2),
    })
    save_timings(timings)

    test = next((t for t in TESTS if t["id"] == int(test_id)), None)
    name = test["name"] if test else f"Test {test_id}"

    print(f"\n[SUBMIT] {name}")
    print(f"  Duration:   {duration:.2f}s")
    print(f"  Characters: {char_count:,}")
    print(f"  Lines:      {line_count}")
    print(f"  Tokens:     {estimated_tokens:,} (estimated)")
    print(f"  TPS:        {tps:.1f}")


def cmd_report(args):
    """Generate final report from all submitted tests."""
    timings = load_timings()
    completed = []

    for t in TESTS:
        tid = str(t["id"])
        if tid in timings and "duration" in timings[tid]:
            completed.append({
                "test_id": t["id"],
                "test_name": t["name"],
                "duration_seconds": timings[tid]["duration"],
                "characters": timings[tid]["characters"],
                "lines": timings[tid]["lines"],
                "tokens": timings[tid]["tokens"],
                "tokens_per_second": timings[tid]["tps"],
            })

    if not completed:
        print("No completed tests found. Run start/submit for each test first.")
        sys.exit(1)

    avg_tps = sum(r["tokens_per_second"] for r in completed) / len(completed)
    total_tokens = sum(r["tokens"] for r in completed)
    total_duration = sum(r["duration_seconds"] for r in completed)

    # Console output
    print("=" * 70)
    print("BENCHMARK RESULTS")
    print(f"Model: {args.model}")
    print(f"Tests completed: {len(completed)}/{len(TESTS)}")
    print("=" * 70)

    print(f"\n{'Test':<25} {'Duration':<12} {'Tokens':<12} {'TPS':<12}")
    print("-" * 70)
    for r in completed:
        print(f"{r['test_name']:<25} {r['duration_seconds']:<12.2f} {r['tokens']:<12,} {r['tokens_per_second']:<12.1f}")
    print("-" * 70)
    print(f"{'TOTAL':<25} {total_duration:<12.2f} {total_tokens:<12,} {avg_tps:<12.1f}")

    # Classification
    if avg_tps >= 90:
        tier = "Excellent"
    elif avg_tps >= 70:
        tier = "Very Good"
    elif avg_tps >= 50:
        tier = "Good"
    elif avg_tps >= 30:
        tier = "Standard"
    else:
        tier = "Below Average"
    print(f"\nClassification: {tier} ({avg_tps:.1f} TPS average)")

    # Save reports
    os.makedirs("results", exist_ok=True)
    model_slug = args.model.replace(" ", "_").replace("/", "_")

    report = {
        "timestamp": datetime.now().isoformat(),
        "model": args.model,
        "classification": tier,
        "average_tps": round(avg_tps, 2),
        "total_tokens": total_tokens,
        "total_duration": round(total_duration, 2),
        "tests_completed": len(completed),
        "tests_total": len(TESTS),
        "results": completed,
    }

    json_file = f"results/{model_slug}_report.json"
    txt_file = f"results/{model_slug}_report.txt"
    md_file = f"results/{model_slug}_Results.md"

    with open(json_file, "w") as f:
        json.dump(report, f, indent=2)

    with open(txt_file, "w") as f:
        f.write(f"OpenCode LLM Benchmark Report\n")
        f.write("=" * 70 + "\n")
        f.write(f"Model: {report['model']}\n")
        f.write(f"Date: {report['timestamp']}\n")
        f.write(f"Classification: {report['classification']}\n\n")
        f.write("SUMMARY\n")
        f.write(f"  Average Speed: {report['average_tps']:.1f} tokens/second\n")
        f.write(f"  Total Tokens: {report['total_tokens']:,}\n")
        f.write(f"  Total Duration: {report['total_duration']:.2f}s\n\n")
        f.write(f"{'Test':<25} {'Duration':<12} {'Tokens':<12} {'TPS':<12}\n")
        f.write("-" * 70 + "\n")
        for r in completed:
            f.write(f"{r['test_name']:<25} {r['duration_seconds']:<12.2f} {r['tokens']:<12,} {r['tokens_per_second']:<12.1f}\n")

    # Markdown summary
    peak = max(completed, key=lambda r: r["tokens_per_second"])
    total_chars = sum(r["characters"] for r in completed)
    total_lines = sum(r["lines"] for r in completed)

    with open(md_file, "w") as f:
        f.write(f"# {args.model} — Benchmark Results\n\n")
        f.write(f"**Date**: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
        f.write(f"## Summary\n\n")
        f.write(f"| Metric | Value |\n")
        f.write(f"|--------|-------|\n")
        f.write(f"| Classification | **{tier}** |\n")
        f.write(f"| Average TPS | {avg_tps:.1f} |\n")
        f.write(f"| Peak TPS | {peak['tokens_per_second']:.1f} ({peak['test_name']}) |\n")
        f.write(f"| Total Tokens | {total_tokens:,} |\n")
        f.write(f"| Total Characters | {total_chars:,} |\n")
        f.write(f"| Total Lines of Code | {total_lines:,} |\n")
        f.write(f"| Total Duration | {total_duration:.2f}s |\n")
        f.write(f"| Tests Completed | {len(completed)}/{len(TESTS)} |\n\n")
        f.write(f"## Detailed Results\n\n")
        f.write(f"| Test | Duration | Chars | Lines | Tokens | TPS |\n")
        f.write(f"|------|----------|-------|-------|--------|-----|\n")
        for r in completed:
            f.write(f"| {r['test_name']} | {r['duration_seconds']:.2f}s | {r['characters']:,} | {r['lines']} | {r['tokens']:,} | {r['tokens_per_second']:.1f} |\n")
        f.write(f"| **Total** | **{total_duration:.2f}s** | **{total_chars:,}** | **{total_lines:,}** | **{total_tokens:,}** | **{avg_tps:.1f}** |\n\n")
        f.write(f"## Performance Analysis\n\n")
        # Group by performance tier
        for r in completed:
            tps_val = r["tokens_per_second"]
            if tps_val >= 90:
                label = "Excellent"
            elif tps_val >= 70:
                label = "Very Good"
            elif tps_val >= 50:
                label = "Good"
            elif tps_val >= 30:
                label = "Standard"
            else:
                label = "Below Average"
            f.write(f"- **{r['test_name']}**: {tps_val:.1f} TPS — {label}\n")
        f.write(f"\n**Overall: {tier}** ({avg_tps:.1f} TPS average, peak {peak['tokens_per_second']:.1f} TPS)\n")

    print(f"\n[OK] Reports saved:")
    print(f"  - {json_file}")
    print(f"  - {txt_file}")
    print(f"  - {md_file}")
    print("=" * 70)


def cmd_reset(args):
    """Clear all timing data and output files."""
    import shutil
    if os.path.exists(DATA_DIR):
        shutil.rmtree(DATA_DIR)
        print("[OK] Benchmark data cleared.")
    else:
        print("Nothing to clear.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="OpenCode LLM Benchmark")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("prompts", help="Show all test prompts")

    p_start = sub.add_parser("start", help="Mark start of a test")
    p_start.add_argument("test_id", type=int, help="Test number (1-6)")

    p_submit = sub.add_parser("submit", help="Mark end of a test and calculate metrics")
    p_submit.add_argument("test_id", type=int, help="Test number (1-6)")

    p_report = sub.add_parser("report", help="Generate final report")
    p_report.add_argument("--model", required=True, help="Model name for report")

    sub.add_parser("reset", help="Clear all timing data")

    args = parser.parse_args()

    if args.command == "prompts":
        cmd_prompts(args)
    elif args.command == "start":
        cmd_start(args)
    elif args.command == "submit":
        cmd_submit(args)
    elif args.command == "report":
        cmd_report(args)
    elif args.command == "reset":
        cmd_reset(args)
    else:
        parser.print_help()
