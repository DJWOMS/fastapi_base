from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from app_support.core.config import settings


class DatabaseHelper:
    def __init__(self, url: str, echo: bool = False):
        self.engine = create_async_engine(url=url, echo=echo)

        self.engine_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False
        )


db_helper = DatabaseHelper(settings.db_url, settings.db_echo)
