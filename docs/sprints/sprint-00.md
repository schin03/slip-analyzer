# Sprint 0: Deployable skeleton

**Goal:** An empty-but-real app running locally with a professional GitHub workflow in place.
**Milestone:** v0.1 Skeleton

## Backlog
1. Repo workflow: labels, milestones, issue and PR templates
2. Docs: README, architecture, ADRs 0001-0004
3. Backend skeleton: FastAPI `/health`, pytest, ruff
4. `OddsProvider` interface + mock provider
5. PostgreSQL via Docker Compose + Alembic baseline
6. Frontend skeleton: dark shell, freshness chip, calls `/health`
7. CI: backend lint+tests, frontend lint+build
8. Research R-1: Odds API bookmaker/market coverage and terms
9. Research R-2: player stats / game-log source options
10. Deploy skeleton (hosting decision)

## Acceptance
`docker compose up` works from a fresh clone; CI is green; deployed page loads.

## Demo / checkpoint
Show the running dashboard shell, the `/health` response, a green CI run, and the board.

## Retrospective
_Filled in at sprint end._
