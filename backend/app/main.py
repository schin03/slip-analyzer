from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import __version__
from app.api.health import router as health_router
from app.config import get_settings

DESCRIPTION = (
    "Analysis and education tool for NBA props. Not gambling advice. "
    "It does not place bets. Odds change and no outcome is guaranteed."
)

def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(title = "Slip Analyzer API", version = __version__, description = DESCRIPTION)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_methods=["GET"],
        allow_headers=["*"],
    )
    app.include_router(health_router)
    return app

app = create_app()
