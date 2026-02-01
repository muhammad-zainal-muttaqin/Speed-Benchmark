# Claude Opus 4.5 — Benchmark Results

**Date**: 2026-02-01 20:48

## Summary

| Metric | Value |
|--------|-------|
| Classification | **Good** |
| Average TPS | 61.1 |
| Peak TPS | 122.0 (Massive System) |
| Total Tokens | 15,415 |
| Total Characters | 61,672 |
| Total Lines of Code | 2,028 |
| Total Duration | 163.43s |
| Tests Completed | 6/6 |

## Detailed Results

| Test | Duration | Chars | Lines | Tokens | TPS |
|------|----------|-------|-------|--------|-----|
| Micro (Baseline) | 8.53s | 47 | 1 | 11 | 1.3 |
| Small Function | 4.63s | 222 | 9 | 55 | 11.9 |
| Medium Class | 8.30s | 1,749 | 50 | 437 | 52.6 |
| Large System | 35.68s | 9,546 | 351 | 2,386 | 66.9 |
| Very Large System | 42.98s | 19,209 | 614 | 4,802 | 111.7 |
| Massive System | 63.31s | 30,899 | 1003 | 7,724 | 122.0 |
| **Total** | **163.43s** | **61,672** | **2,028** | **15,415** | **61.1** |

## Performance Analysis

- **Micro (Baseline)**: 1.3 TPS — Below Average
- **Small Function**: 11.9 TPS — Below Average
- **Medium Class**: 52.6 TPS — Good
- **Large System**: 66.9 TPS — Good
- **Very Large System**: 111.7 TPS — Excellent
- **Massive System**: 122.0 TPS — Excellent

**Overall: Good** (61.1 TPS average, peak 122.0 TPS)
