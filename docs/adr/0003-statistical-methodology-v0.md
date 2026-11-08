# ADR-0003: Statistical methodology v0.1 (draft)

- **Status:** Proposed (to be refined with data)
- **Date:** 2026-11-07

## Summary
1. Odds are stored as decimal; the UI can display decimal or American.
2. Implied probability = 1 / decimal odds. Remove the bookmaker margin (vig) by normalizing the Over/Under pair to get a fair probability.
3. Estimated probability starts from the recent hit rate versus the line, **shrunk toward the fair probability** according to sample size, so small samples cannot create large fake edges.
4. Capped, explainable adjustments: home/away, rest, minutes trend, opponent defense vs. position, injuries where reliably sourced. Each appears in the rationale.
5. Edge = estimated probability - fair probability; also expected value per unit. Present a conservative / central / optimistic range.
6. Pairings: combined probability = p1 x p2 only when independent; same-game legs are flagged as correlated. Payout multiplier = odds1 x odds2.
7. Every recommendation is saved as an immutable, timestamped snapshot (line, odds, model version, rationale) before game time, then evaluated later using calibration and closing-line value.
8. Draft thresholds (to tune by backtest): >= 15 games, >= 20 mpg, edge >= 4 points, no unresolved injury flag.

## Honest expectation
Sportsbook lines are efficient. A simple rules model will probably not beat them consistently. The product is framed as transparent statistical analysis, not a promise of profit.

## Later
"High Upside" table (5-7 picks) and "Play of the Day" definitions to be proposed and approved in a later sprint. ML is deferred until this version is working and measurable.
