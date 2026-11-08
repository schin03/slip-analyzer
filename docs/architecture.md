# Architecture (living document)

See README for the high-level diagram. Sections to fill in as we build:

- Provider abstraction (`OddsProvider`) and data freshness model
- Data model: events, markets, odds snapshots, recommendation snapshots
- Analytics pipeline: implied probability -> de-vig -> shrinkage -> adjustments -> edge
- API surface and OpenAPI-generated client
- Future: auth, saved slips, sharing, mobile client
