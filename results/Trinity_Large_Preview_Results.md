# Trinity Large Preview — Benchmark Results

**Date**: 2026-02-02 00:04

## Summary

| Metric | Value |
|--------|-------|
| Classification | **Below Average** |
| Average TPS | 15.5 |
| Peak TPS | 32.2 (Massive System) |
| Total Tokens | 9,891 |
| Total Characters | 39,574 |
| Total Lines of Code | 1,265 |
| Total Duration | 430.49s |
| Tests Completed | 6/6 |

## Detailed Results

| Test | Duration | Chars | Lines | Tokens | TPS |
|------|----------|-------|-------|--------|-----|
| Micro (Baseline) | 6.55s | 37 | 0 | 9 | 1.4 |
| Small Function | 10.72s | 284 | 12 | 71 | 6.6 |
| Medium Class | 50.32s | 2,706 | 77 | 676 | 13.4 |
| Large System | 97.26s | 6,249 | 216 | 1,562 | 16.1 |
| Very Large System | 111.14s | 10,387 | 332 | 2,596 | 23.4 |
| Massive System | 154.50s | 19,911 | 628 | 4,977 | 32.2 |
| **Total** | **430.49s** | **39,574** | **1,265** | **9,891** | **15.5** |

## Performance Analysis

- **Micro (Baseline)**: 1.4 TPS — Below Average
- **Small Function**: 6.6 TPS — Below Average
- **Medium Class**: 13.4 TPS — Below Average
- **Large System**: 16.1 TPS — Below Average
- **Very Large System**: 23.4 TPS — Below Average
- **Massive System**: 32.2 TPS — Standard

**Overall: Below Average** (15.5 TPS average, peak 32.2 TPS)
