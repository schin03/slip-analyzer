import asyncio
from datetime import UTC, datetime

import pytest
from pydantic import ValidationError

from backend.app.providers.base import GameNotFoundError, MarketType, OutcomeOdds, Side
from backend.app.providers.mock import MockOddsProvider

FIXED_NOW = datetime(2026, 11, 7, 12, 0, tzinfo=UTC)

def make_provider() -> MockOddsProvider:
    return MockOddsProvider(clock = lambda: FIXED_NOW)

def test_list_games_include_source_and_freshness():
    result = asyncio.run(make_provider().list_games())
    assert result.meta.source == "mock"
    assert result.meta.fetched_at == FIXED_NOW
    assert len(result.games) == 2

def test_game_odds_have_over_under_for_all_lines():
    result = asyncio.run(make_provider().get_game_odds("mock-game-1"))
    assert result.odds, "expected some odds"
    pairs: dict[tuple, set[Side]] = {}
    for o in result.odds:
        assert o.decimal_odds > 1.0
        pairs.setdefault((o.market, o.player_name, o.line), set()).add(o.side)
    assert all(sides == {Side.OVER, Side.UNDER} for sides in pairs.values())

def test_game_odds_cover_requested_prop_types():
    result = asyncio.run(make_provider().get_game_odds("mock-game-1"))
    markets = {o.market for o in result.odds}
    assert {MarketType.PLAYER_POINTS, MarketType.PLAYER_PRA, MarketType.GAME_TOTAL} <= markets

def test_unknown_game_raises():
    with pytest.raises(GameNotFoundError):
        asyncio.run(make_provider().get_game_odds("nope"))


def test_decimal_odds_must_be_greater_than_one():
    with pytest.raises(ValidationError):
        OutcomeOdds(
            game_id="x",
            market=MarketType.GAME_TOTAL,
            line=200.5,
            side=Side.OVER,
            decimal_odds=1.0,
            bookmaker="b",
        )