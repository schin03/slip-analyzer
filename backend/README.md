# Backend

FastAPI service. Run all commands from this `backend/` folder.

```powershell
uv sync                                   # create .venv with Python 3.12 and install deps
uv run pytest                             # run tests
uv run ruff check .                       # lint
uv run ruff format .                      # auto-format
uv run uvicorn app.main:app --reload      # run the server
```

Then open http://127.0.0.1:8000/health and http://127.0.0.1:8000/docs.

## Layout
- `app/main.py`: builds the FastAPI app
- `app/config.py`: settings from environment variables / `.env`
- `app/api/`: HTTP routes
- `app/providers/`: odds data behind the `OddsProvider` interface (mock for now)
- `tests/`: pytest tests
