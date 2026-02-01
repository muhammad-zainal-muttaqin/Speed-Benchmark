# Kimi K2.5 Free — Benchmark Results

**Date**: 2026-02-01 20:57

## Summary

| Metric | Value |
|--------|-------|
| Classification | **Standard** |
| Average TPS | 48.9 |
| Peak TPS | 96.4 (Massive System) |
| Total Tokens | 11,698 |
| Total Characters | 46,803 |
| Total Lines of Code | 1,530 |
| Total Duration | 151.99s |
| Tests Completed | 6/6 |

## Detailed Results

| Test | Duration | Chars | Lines | Tokens | TPS |
|------|----------|-------|-------|--------|-----|
| Micro (Baseline) | 4.12s | 47 | 1 | 11 | 2.7 |
| Small Function | 6.76s | 222 | 9 | 55 | 8.1 |
| Medium Class | 11.43s | 1,536 | 43 | 384 | 33.6 |
| Large System | 15.96s | 4,666 | 190 | 1,166 | 73.1 |
| Very Large System | 51.45s | 16,319 | 536 | 4,079 | 79.3 |
| Massive System | 62.27s | 24,013 | 751 | 6,003 | 96.4 |
| **Total** | **151.99s** | **46,803** | **1,530** | **11,698** | **48.9** |

## Performance Analysis

- **Micro (Baseline)**: 2.7 TPS — Below Average
- **Small Function**: 8.1 TPS — Below Average
- **Medium Class**: 33.6 TPS — Standard
- **Large System**: 73.1 TPS — Very Good
- **Very Large System**: 79.3 TPS — Very Good
- **Massive System**: 96.4 TPS — Excellent

**Overall: Standard** (48.9 TPS average, peak 96.4 TPS)
