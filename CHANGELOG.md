# Changelog

All notable changes are documented here. Format based on [Keep a Changelog](https://keepachangelog.com/).

## [Unreleased]

### Added
- Project workflow: issue templates, PR template, labels/milestones script.
- Architecture decision records ADR-0001 to ADR-0004.
- README with disclaimers and planned stack.
- Backend skeleton: FastAPI app, `/health`, settings, pytest and ruff config.
- `OddsProvider` interface and deterministic mock provider.
- PostgreSQL via Docker Compose (configurable host port), SQLAlchemy engine, and Alembic baseline migration.
- Frontend skeleton: Vite, React, TypeScript, Tailwind v4, dark theme, header, footer disclaimers, and data-freshness chip.
- Backend status chip that calls `GET /health` using the `VITE_API_URL` setting.
