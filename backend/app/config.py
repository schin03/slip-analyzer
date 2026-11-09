"""Application settings, loaded from environment variables and an optional .env file."""

from functools import lru_cache

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=PROJECT_ROOT/".env", extra="ignore")

    environment: str = "development"
    odds_provider: str = "mock"
    # Provider credentials stay on the backend only. SecretStr hides the value in logs/reprs.
    odds_api_key: SecretStr | None = None
    cors_origins: list[str] = ["http://localhost:5173"]


@lru_cache
def get_settings() -> Settings:
    return Settings()
