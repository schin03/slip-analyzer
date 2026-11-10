from app.providers.base import OddsProvider
from app.providers.mock import MockOddsProvider
from backend.app.config import Settings


def get_provider(settings: Settings) -> OddsProvider:
    if settings.odds.prover == "mock":
        return MockOddsProvider()
    raise ValueError(f"Unknown or not-yet implemented odds provider: {settings.odds_provider!r}")
