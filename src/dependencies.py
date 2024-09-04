from typing import AsyncGenerator, Type, Callable

from fastapi import Depends
from sqlalchemy.ext.asyncio import async_sessionmaker

from src.crud.base import BaseCRUDRepository
from src.config.db import async_db


async def get_async_session() -> AsyncGenerator[async_sessionmaker, None]:
    try:
        yield async_db.async_session
    except Exception as e:
        await async_db.async_session.rollback()
        raise e
    finally:
        await async_db.async_session.close()


def get_repo(
    repo_type: Type[BaseCRUDRepository],
) -> Callable[[async_sessionmaker], BaseCRUDRepository]:
    def _get_repo(
        async_session: async_sessionmaker = Depends(get_async_session),
    ) -> BaseCRUDRepository:
        return repo_type(async_session=async_session)

    return _get_repo
