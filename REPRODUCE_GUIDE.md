# OpenCode LLM Benchmark - Reproduction Guide

## Overview

This benchmark measures **real token generation speed** (tokens per second) of AI coding assistants like Claude Code, OpenCode, or Cursor. It runs directly inside an AI coding session — no API key required.

## Prerequisites

- Python 3.8+
- An AI coding assistant session (Claude Code, OpenCode, Cursor, etc.)
- No external dependencies (standard library only)

## How It Works

The AI generates real code for each prompt. Wall-clock time between `start` and `submit` captures actual generation speed.

---

## Instructions for AI

> **IMPORTANT**: You must follow these steps exactly. Do NOT read or copy from any existing files in `benchmark_output/` or `results/`. You must generate ALL code yourself from scratch.

### Step 1: Reset previous data

```bash
python benchmark.py reset
```

### Step 2: Run each test (1 through 6)

For EACH test, do these 3 things in order:

**a)** Run `start` to record the start timestamp:
```bash
python benchmark.py start <TEST_NUMBER>
```

**b)** Read the prompt shown by the `start` command, then **generate the code yourself from scratch** and write it to `benchmark_output/test_<TEST_NUMBER>.py`. Do NOT copy from any existing file. Do NOT read any file before writing. Generate fresh code based solely on the prompt.

**c)** Run `submit` to record end timestamp and calculate metrics:
```bash
python benchmark.py submit <TEST_NUMBER>
```

Repeat a/b/c for tests 1, 2, 3, 4, 5, 6 in order.

### Step 3: Generate report

```bash
python benchmark.py report --model "<YOUR MODEL NAME>"
```

Replace `<YOUR MODEL NAME>` with your actual model name (e.g. "Kimi K2.5", "GPT-4o", "Claude Opus 4.5").

---

## Test Suite

| # | Test | Prompt |
|---|------|--------|
| 1 | Micro (Baseline) | Say exactly: 'Long-form benchmark test starting now' |
| 2 | Small Function | Fibonacci with memoization |
| 3 | Medium Class | Matrix class with add, multiply, transpose, determinant |
| 4 | Large System | Flask REST API with auth, rate limiting, CRUD |
| 5 | Very Large System | E-commerce system (Product, Cart, Order, User) |
| 6 | Massive System | Database ORM with Model, Query, Migration, Relationships |

## Output Files

Results are saved to `./results/`:

| File | Format |
|------|--------|
| `[MODEL]_report.json` | Machine-readable structured data |
| `[MODEL]_report.txt` | Human-readable formatted report |

## TPS Classification

| Range | Classification |
|-------|---------------|
| 90+ TPS | Excellent |
| 70-90 TPS | Very Good |
| 50-70 TPS | Good |
| 30-50 TPS | Standard |
| <30 TPS | Below Average |

Small tasks show lower TPS due to per-call overhead. Real throughput is best observed on medium-to-large tests (tests 4-6).

## Technical Details

- **Token estimation**: `character_count / 4`
- **Timing**: Wall-clock time between `start` and `submit` commands
- **Output directory**: `benchmark_output/test_N.py`
