# Kimi K2.5 — Benchmark Results

**Date**: 2026-02-01 21:51

## Summary

| Metric | Value |
|--------|-------|
| Classification | **Standard** |
| Average TPS | 45.6 |
| Peak TPS | 83.2 (Massive System) |
| Total Tokens | 11,344 |
| Total Characters | 45,386 |
| Total Lines of Code | 1,470 |
| Total Duration | 165.90s |
| Tests Completed | 6/6 |

## Detailed Results

| Test | Duration | Chars | Lines | Tokens | TPS |
|------|----------|-------|-------|--------|-----|
| Micro (Baseline) | 5.36s | 38 | 1 | 9 | 1.7 |
| Small Function | 6.22s | 277 | 10 | 69 | 11.1 |
| Medium Class | 11.51s | 1,905 | 57 | 476 | 41.4 |
| Large System | 30.99s | 7,959 | 288 | 1,989 | 64.2 |
| Very Large System | 44.17s | 12,681 | 428 | 3,170 | 71.8 |
| Massive System | 67.65s | 22,526 | 686 | 5,631 | 83.2 |
| **Total** | **165.90s** | **45,386** | **1,470** | **11,344** | **45.6** |

## Performance Analysis

- **Micro (Baseline)**: 1.7 TPS — Below Average
- **Small Function**: 11.1 TPS — Below Average
- **Medium Class**: 41.4 TPS — Standard
- **Large System**: 64.2 TPS — Good
- **Very Large System**: 71.8 TPS — Very Good
- **Massive System**: 83.2 TPS — Very Good

**Overall: Standard** (45.6 TPS average, peak 83.2 TPS)
