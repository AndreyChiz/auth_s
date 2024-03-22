from typing import Any

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import Select, Insert, Update, CursorResult
from src.config import settings
from .models import User

DATABASE_URL = str(settings.DATABASE_URL_asyncpg)
engine = create_async_engine(DATABASE_URL)


async def fetch_one(select_query: Select | Insert | Update) -> dict[str, Any] | None:
    async with engine.begin() as conn:
        cursor: CursorResult = await conn.execute(select_query)
        return cursor.first()._asdict() if cursor.rowcount > 0 else None
