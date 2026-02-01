# GLM-4.7 Free OpenCode Zen — Benchmark Results

**Date**: 2026-02-01 22:30

## Summary

| Metric | Value |
|--------|-------|
| Classification | **Below Average** |
| Average TPS | 22.3 |
| Peak TPS | 38.7 (Medium Class) |
| Total Tokens | 7,088 |
| Total Characters | 28,362 |
| Total Lines of Code | 859 |
| Total Duration | 270.10s |
| Tests Completed | 6/6 |

## Detailed Results

| Test | Duration | Chars | Lines | Tokens | TPS |
|------|----------|-------|-------|--------|-----|
| Micro (Baseline) | 8.70s | 47 | 1 | 11 | 1.3 |
| Small Function | 20.14s | 213 | 9 | 53 | 2.6 |
| Medium Class | 11.11s | 1,722 | 48 | 430 | 38.7 |
| Large System | 30.41s | 4,438 | 157 | 1,109 | 36.5 |
| Very Large System | 81.49s | 8,512 | 255 | 2,128 | 26.1 |
| Massive System | 118.25s | 13,430 | 389 | 3,357 | 28.4 |
| **Total** | **270.10s** | **28,362** | **859** | **7,088** | **22.3** |

## Performance Analysis

- **Micro (Baseline)**: 1.3 TPS — Below Average
- **Small Function**: 2.6 TPS — Below Average
- **Medium Class**: 38.7 TPS — Standard
- **Large System**: 36.5 TPS — Standard
- **Very Large System**: 26.1 TPS — Below Average
- **Massive System**: 28.4 TPS — Below Average

**Overall: Below Average** (22.3 TPS average, peak 38.7 TPS)
