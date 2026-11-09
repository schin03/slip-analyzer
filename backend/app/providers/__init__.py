from backend.app.config import Settings
from app.providers.base import OddsProvider
from app.providers.mock import MockOddsProvider

def get_provider(settings: Settings) -> OddsProvider:
    if settings.odds.prover == "mock":
        return MockOddsProvider()
    raise ValueError(f"Unknown or not-yet implemented odds provider: {setting.odds_provider!r}")