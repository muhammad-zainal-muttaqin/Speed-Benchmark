# MiniMax M2.1 Free OpenCode Zen — Benchmark Results

**Date**: 2026-02-01 21:05

## Summary

| Metric | Value |
|--------|-------|
| Classification | **Standard** |
| Average TPS | 34.1 |
| Peak TPS | 62.8 (Massive System) |
| Total Tokens | 8,444 |
| Total Characters | 33,787 |
| Total Lines of Code | 1,036 |
| Total Duration | 182.82s |
| Tests Completed | 6/6 |

## Detailed Results

| Test | Duration | Chars | Lines | Tokens | TPS |
|------|----------|-------|-------|--------|-----|
| Micro (Baseline) | 14.33s | 47 | 1 | 11 | 0.8 |
| Small Function | 11.61s | 342 | 15 | 85 | 7.3 |
| Medium Class | 22.57s | 2,513 | 75 | 628 | 27.8 |
| Large System | 28.61s | 5,722 | 203 | 1,430 | 50.0 |
| Very Large System | 49.00s | 10,912 | 330 | 2,728 | 55.7 |
| Massive System | 56.70s | 14,251 | 412 | 3,562 | 62.8 |
| **Total** | **182.82s** | **33,787** | **1,036** | **8,444** | **34.1** |

## Performance Analysis

- **Micro (Baseline)**: 0.8 TPS — Below Average
- **Small Function**: 7.3 TPS — Below Average
- **Medium Class**: 27.8 TPS — Below Average
- **Large System**: 50.0 TPS — Standard
- **Very Large System**: 55.7 TPS — Good
- **Massive System**: 62.8 TPS — Good

**Overall: Standard** (34.1 TPS average, peak 62.8 TPS)
