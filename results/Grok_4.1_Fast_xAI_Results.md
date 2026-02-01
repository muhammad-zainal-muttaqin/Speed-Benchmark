# Grok 4.1 Fast xAI — Benchmark Results

**Date**: 2026-02-01 21:11

## Summary

| Metric | Value |
|--------|-------|
| Classification | **Standard** |
| Average TPS | 41.0 |
| Peak TPS | 87.5 (Massive System) |
| Total Tokens | 5,556 |
| Total Characters | 22,232 |
| Total Lines of Code | 732 |
| Total Duration | 110.88s |
| Tests Completed | 6/6 |

## Detailed Results

| Test | Duration | Chars | Lines | Tokens | TPS |
|------|----------|-------|-------|--------|-----|
| Micro (Baseline) | 9.88s | 37 | 0 | 9 | 0.9 |
| Small Function | 15.68s | 155 | 8 | 38 | 2.4 |
| Medium Class | 13.25s | 1,769 | 50 | 442 | 33.4 |
| Large System | 23.34s | 5,648 | 165 | 1,412 | 60.5 |
| Very Large System | 23.05s | 5,630 | 191 | 1,407 | 61.0 |
| Massive System | 25.68s | 8,993 | 318 | 2,248 | 87.5 |
| **Total** | **110.88s** | **22,232** | **732** | **5,556** | **41.0** |

## Performance Analysis

- **Micro (Baseline)**: 0.9 TPS — Below Average
- **Small Function**: 2.4 TPS — Below Average
- **Medium Class**: 33.4 TPS — Standard
- **Large System**: 60.5 TPS — Good
- **Very Large System**: 61.0 TPS — Good
- **Massive System**: 87.5 TPS — Very Good

**Overall: Standard** (41.0 TPS average, peak 87.5 TPS)
