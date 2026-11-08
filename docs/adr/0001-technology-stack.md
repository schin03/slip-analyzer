# ADR-0001: Technology stack

- **Status:** Accepted
- **Date:** 2026-11-07

## Context
We want a polished interactive dashboard, a Python/FastAPI backend (a learning goal), low cost, and a path to a future mobile app.

## Options considered
**Frontend:** Vite+React+TS (chosen), Next.js, SvelteKit. Next.js adds a second server runtime beside FastAPI; SvelteKit has a weaker mobile story.
**Database:** PostgreSQL (chosen) vs SQLite. SQLite is simpler but awkward on ephemeral free hosts and harder to migrate from.
**Backend tooling:** FastAPI, SQLAlchemy 2, Alembic, Pydantic, pytest, ruff.

## Decision
Vite + React + TypeScript + Tailwind; FastAPI on Python 3.12; PostgreSQL (Docker locally, managed free tier when deployed). Hosting is decided separately in Sprint 0 after verifying current free tiers.

## Consequences
React skills transfer to React Native/Expo. A generated OpenAPI client keeps a future mobile app on the same API. Free backend tiers may sleep when idle, which is acceptable for V1.
