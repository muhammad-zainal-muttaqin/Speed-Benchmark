# Big Pickle OpenCode Zen — Benchmark Results

**Date**: 2026-02-01 23:52

## Summary

| Metric | Value |
|--------|-------|
| Classification | **Below Average** |
| Average TPS | 27.1 |
| Peak TPS | 65.2 (Medium Class) |
| Total Tokens | 27,075 |
| Total Characters | 108,309 |
| Total Lines of Code | 3,379 |
| Total Duration | 1927.44s |
| Tests Completed | 6/6 |

## Detailed Results

| Test | Duration | Chars | Lines | Tokens | TPS |
|------|----------|-------|-------|--------|-----|
| Micro (Baseline) | 11.34s | 47 | 1 | 11 | 1.0 |
| Small Function | 9.89s | 731 | 33 | 182 | 18.4 |
| Medium Class | 24.44s | 6,376 | 219 | 1,594 | 65.2 |
| Large System | 95.87s | 16,900 | 553 | 4,225 | 44.1 |
| Very Large System | 372.35s | 38,846 | 1175 | 9,711 | 26.1 |
| Massive System | 1413.55s | 45,409 | 1398 | 11,352 | 8.0 |
| **Total** | **1927.44s** | **108,309** | **3,379** | **27,075** | **27.1** |

## Performance Analysis

- **Micro (Baseline)**: 1.0 TPS — Below Average
- **Small Function**: 18.4 TPS — Below Average
- **Medium Class**: 65.2 TPS — Good
- **Large System**: 44.1 TPS — Standard
- **Very Large System**: 26.1 TPS — Below Average
- **Massive System**: 8.0 TPS — Below Average

**Overall: Below Average** (27.1 TPS average, peak 65.2 TPS)
