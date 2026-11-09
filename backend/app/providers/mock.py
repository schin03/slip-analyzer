""" content is mock data. this data will never change, it is purely fictional and for testing """

from collections.abc import Callable
from datetime import UTC, datetime, timedelta

from backend.app.providers.base import (
    Game,
    GameList,
    GameNotFoundError,
    GameOdds,
    MarketType,
    OddsProvider,
    OutcomeOdds,
    Side,
    SourceMeta
)

BOOKMAKER = "MockBook"

_LINES: list[tuple[str, MarketType, str | None, float | None, float, float]] = [
    ("mock-game-1", MarketType.PLAYER_POINTS, "Alex Rivera", 24.5, 1.91, 1.91),
    ("mock-game-1", MarketType.PLAYER_REBOUNDS, "Jordan Blake", 9.5, 1.87, 1.95),
    ("mock-game-1", MarketType.PLAYER_ASSISTS, "Sam Okafor", 7.5, 2.00, 1.83),
    ("mock-game-1", MarketType.PLAYER_THREES, "Alex Rivera", 3.5, 2.10, 1.74),
    ("mock-game-1", MarketType.PLAYER_PRA, "Jordan Blake", 38.5, 1.91, 1.91),
    ("mock-game-1", MarketType.GAME_TOTAL, None, 224.5, 1.91, 1.91),
    ("mock-game-1", MarketType.GAME_ML, "UBC", None, 1.91, 1.91),
    ("mock-game-2", MarketType.PLAYER_POINTS, "Casey Lindqvist", 28.5, 1.95, 1.87),
    ("mock-game-2", MarketType.PLAYER_REBOUNDS, "Taylor Nguyen", 11.5, 1.83, 2.00),
    ("mock-game-2", MarketType.PLAYER_ASSISTS, "Casey Lindqvist", 5.5, 1.87, 1.95),
    ("mock-game-2", MarketType.GAME_TOTAL, None, 231.5, 1.91, 1.91),
    ("mock-game-1", MarketType.GAME_ML, "BCIT", None, 1.91, 1.91),
]


def _utc_now() -> datetime:
    return datetime.now(UTC)


class MockOddsProvider(OddsProvider):
    name = "mock"

    def __init__(self, clock: Callable[[], datetime] = _utc_now) -> None:
        self._clock = clock

    def _meta(self) -> SourceMeta:
        return SourceMeta(source=self.name, fetched_at=self._clock())

    def _games(self) -> list[Game]:
        now = self._clock()
        return [
            Game(
                id="mock-game-1",
                home_team="UBC",
                away_team="SFU",
                start_time=now + timedelta(hours=3)
            ),
            Game(
                id="mock-game-2",
                home_team="Langara",
                away_team="BCIT",
                start_time=now + timedelta(hours=4)
            ),
        ]

    async def list_games(self) -> GameList:
        return GameList(meta=self._meta(), games=self._games())

    async def get_game_odds(self, game_id: str) -> GameOdds:
        if game_id not in {e.id for e in self._games()}:
            raise GameNotFoundError(game_id)
        odds: list[OutcomeOdds] = []
        for game, market, player, line, over, under in _LINES:
            if game != game_id:
                continue
            for side, price in ((Side.OVER, over), (Side.UNDER, under)):
                odds.append(
                    OutcomeOdds(
                        game_id=game,
                        market=market,
                        player_name=player,
                        line=line,
                        side=side,
                        decimal_odds=price,
                        bookmaker=BOOKMAKER,
                    )
                )
        return GameOdds(meta=self._meta(), game_id=game_id, odds=odds)
