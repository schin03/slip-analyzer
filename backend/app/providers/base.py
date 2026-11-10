from abc import ABC, abstractmethod
from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel, Field


class MarketType(StrEnum):
    PLAYER_POINTS = "player_points"
    PLAYER_REBOUNDS = "player_rebounds"
    PLAYER_ASSISTS = "player_assists"
    PLAYER_THREES = "player_threes"
    PLAYER_PRA = "player_pra"
    GAME_TOTAL = "total"
    GAME_ML = "game_moneyline"


class Side(StrEnum):
    OVER = "over"
    UNDER = "under"


class SourceMeta(BaseModel):
    source: str = Field(description="Data provider name, i.e. 'mock' or 'the-odds-api'")
    fetched_at: datetime = Field(description="When data was last obtained (timezone-aware, UTC)")


class Game(BaseModel):
    id: str
    home_team: str
    away_team: str
    start_time: datetime


class OutcomeOdds(BaseModel):
    game_id: str
    market: MarketType
    player_name: str | None = None
    line: float | None = None
    side: Side
    decimal_odds: float = Field(gt=1.0)
    bookmaker: str


class GameList(BaseModel):
    meta: SourceMeta
    games: list[Game]


class GameOdds(BaseModel):
    meta: SourceMeta
    game_id: str
    odds: list[OutcomeOdds]


class GameNotFoundError(Exception):
    pass


class OddsProvider(ABC):
    name: str

    @abstractmethod
    async def list_games(self) -> GameList:
        """Upcoming Games"""

    @abstractmethod
    async def get_game_odds(self, game_id: str) -> GameOdds:
        """All available odds for one game. Will raise GameNotFoundError if unknown"""
