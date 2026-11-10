import pytest
from sqlalchemy import text

from app.config import get_settings
from app.db import get_engine

pytestmark = pytest.mark.skipif(
    get_settings().database_url is None, reason="DATABASE_URL is not set"
)


def test_database_connection():
    with get_engine().connect() as connection:
        assert connection.execute(text("select 1")).scalar() == 1
