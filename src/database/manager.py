from sqlalchemy.ext.asyncio import create_async_engine
from src.config import settings

DATABASE_URL = str(settings.DATABASE_URL)
engine = create_async_engine(DATABASE_URL)

