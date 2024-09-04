import typing
import pydantic
import sqlalchemy

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.pool import Pool
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine

from src.config.manager import settings

url = f"{settings.DB_POSTGRES_SCHEMA}://{settings.DB_POSTGRES_USERNAME}:{settings.DB_POSTGRES_PASSWORD}@{settings.DB_POSTGRES_HOST}:{settings.DB_POSTGRES_PORT}/{settings.DB_POSTGRES_NAME}"


class AsyncDatabase:
    def __init__(self):
        self.postgres_uri: pydantic.PostgresDsn = pydantic.PostgresDsn(url=url)
        self.async_engine: AsyncEngine = create_async_engine(
            url=self.set_async_db_uri,
            echo=settings.IS_DB_ECHO_LOG,
            pool_size=settings.DB_POOL_SIZE,
            max_overflow=settings.DB_POOL_OVERFLOW,
        )
        self.async_session: AsyncSession = AsyncSession(bind=self.async_engine)
        self.pool: Pool = self.async_engine.pool

    @property
    def set_async_db_uri(self) -> str | pydantic.PostgresDsn:
        """
        Set the synchronous database driver into asynchronous version by utilizing AsyncPG:

            `postgresql://` => `postgresql+asyncpg://`
        """
        return (
            str(self.postgres_uri).replace("postgresql://", "postgresql+asyncpg://")
            if self.postgres_uri
            else self.postgres_uri
        )


class DBTable(DeclarativeBase):
    metadata: sqlalchemy.MetaData = sqlalchemy.MetaData()


async_db: AsyncDatabase = AsyncDatabase()
Base: typing.Type[DeclarativeBase] = DBTable
