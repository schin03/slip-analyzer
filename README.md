# NBA Slip Analyzer

An open-source, **analysis and education** tool for exploring NBA player props and game lines. It surfaces statistical "leans" with transparent, human-readable reasoning, and shows how pairing two picks changes payout, probability, and risk.

> **Status:** Sprint 0 (project skeleton): backend skeleton and mock odds provider in progress. No product features yet. See [`docs/sprints/`](docs/sprints/) and the [GitHub Project board](../../projects).

## Disclaimer (please read)

- This project is for **informational and educational purposes only**. It is **not gambling advice**.
- It **does not place bets, process money, or link to wagering**.
- Odds change quickly and may be stale. Every number in the UI shows its source and freshness.
- **No outcome is guaranteed.** Estimated probabilities are model outputs, not certainties, and sportsbook markets are hard to beat.
- You must be of legal gambling age in your jurisdiction to bet. If gambling is causing harm, please contact a local support service.

## Planned stack

| Layer | Choice | Why |
|---|---|---|
| Frontend | Vite + React + TypeScript + Tailwind | Simple, fast; skills transfer to React Native later |
| Backend | Python 3.12 + FastAPI | Typed, auto-generated OpenAPI docs |
| Database | PostgreSQL (Docker locally) | Good for time-series odds snapshots; auth-ready later |
| Odds data | The Odds API (free tier) behind a provider interface | Swappable; Bet365 availability still being verified |
| Analytics | Transparent rules-based scoring | ML deferred until the rules version is measurable |

Decisions are recorded in [`docs/adr/`](docs/adr/).

## Architecture (planned)

```
React dashboard  -->  FastAPI  -->  analytics (rules engine)
                          |              |
                          v              v
                    PostgreSQL  <--  OddsProvider interface --> Mock | The Odds API | (future)
```

The backend never exposes a raw provider feed; it serves derived analysis only. Provider credentials live only in backend environment variables.

## Local setup

Prerequisites: Git, [uv](https://docs.astral.sh/uv/), Python 3.12 (uv can install it), Node.js LTS, Docker Desktop (needed from Increment 2b).

Backend (see [`backend/README.md`](backend/README.md)):

```powershell
docker compose up -d
cd backend
uv sync
uv run alembic upgrade head
uv run pytest
uv run uvicorn app.main:app --reload   # http://127.0.0.1:8000/docs
```

Frontend and Docker Compose arrive in later Sprint 0 increments.

## Contributing workflow

Work is tracked in GitHub Issues, grouped by milestone, with short sprints. Changes go through pull requests using [conventional commits](https://www.conventionalcommits.org/) (`feat:`, `fix:`, `docs:`, `chore:`, `test:`, `refactor:`).

## License

Code is released under the [MIT License](LICENSE). Odds and statistics data remain subject to their providers' terms and are **not** covered by this license.
