# ADR-0005: Database access and migrations

- **Status:** Accepted
- **Date:** 2026-11-09

## Context
Sprint 1 needs persistent storage for odds snapshots and recommendation records. We want
reproducible local setup and versioned schema changes.

## Decisions
- **Local Postgres runs in Docker Compose; the backend runs natively with uv** (option C).
  A backend Dockerfile is added when we deploy (issue #10). Options considered: Postgres-only
  in Docker, both in Docker now, or Postgres now and backend later.
- **Synchronous SQLAlchemy 2 with psycopg 3.** Simpler to learn and test; V1 traffic is small.
  Async (asyncpg) was rejected as extra complexity with no V1 benefit and can be revisited.
- **Alembic for migrations**, in `backend/migrations/`, using the same engine and `DATABASE_URL`
  as the app. The baseline migration is intentionally empty.
- **Host port is configurable** via `POSTGRES_PORT` (default 5432) because 5432 may be taken.

## Consequences
- Credentials live only in git-ignored `.env` files; the database is bound to 127.0.0.1.
- Real tables and the data model are designed in Sprint 1.
- `docker compose down -v` deletes all local data; hosted databases need their own backup plan.