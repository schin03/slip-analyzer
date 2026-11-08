# ADR-0002: Odds data provider and abstraction

- **Status:** Accepted (with open verification items)
- **Date:** 2026-11-07

## Context
We want NBA props odds, ideally Bet365, without scraping or violating terms.

## Options considered
- **Odds-API.io:** lists Bet365 incl. player props; no free tier currently (cheapest plan ~GBP 49/mo); terms restrict redistribution of raw data.
- **The Odds API (chosen for V1):** free plan includes current odds; NBA player props via the per-event endpoint; cost is markets x regions credits per call; historical data paid-only (not needed). Bet365 NBA prop coverage **unverified**; props reportedly cover mainly US bookmakers.
- **Mock/recorded data:** free, deterministic; used for early development and tests.
- **Manual CSV import:** compliant fallback.

## Decision
All providers sit behind an `OddsProvider` interface returning bookmaker-labeled data. Start with mock data, then The Odds API free tier with aggressive caching and stored snapshots. Show source and freshness in the UI. The backend never serves a raw provider feed. We do not use provider deep links to sportsbooks.

## Open items
- R-1: verify bookmaker/market coverage and read the terms after obtaining a key.
- Confirm the free-tier credit allowance.
- Bet365 is added only if available and compliant; otherwise show another book, labeled.
