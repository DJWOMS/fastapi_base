from typing import NewType

from sqlalchemy import delete, update
from sqlalchemy.exc import MultipleResultsFound, NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from .interfaces.repository import AbstractRepository
from .errors import (
    DBError,
    MultipleRowsFoundError,
    NoRowsFoundError,
)
from .models import Base


SqlModel = NewType("SqlModel", Base)


class SqlAlchemyRepository(AbstractRepository):
    model = None

    def __init__(self, db_session: AsyncSession):
        self._session_factory = db_session

    async def create(self, data: dict) -> SqlModel:
        async with self._session_factory() as session:
            instance = self.model(**data)
            session.add(instance)
            await session.commit()
            await session.refresh(instance)
            return instance

    async def update(self, data: dict, **filters) -> SqlModel:
        async with self._session_factory() as session:
            if not data:
                raise DBError(
                    f"Passed empty dictionary for update method in model {self.model.__name__}"
                )
            stmt = update(self.model).values(**data).filter_by(**filters).returning(self.model)
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one()

    async def delete(self, **filters) -> None:
        async with self._session_factory() as session:
            result = await session.execute(delete(self.model).filter_by(**filters))
            if result.rowcount == 0:
                raise NoRowsFoundError(
                    f"For model {self.model.__name__} with next filters: {filters}"
                )
            await session.commit()

    async def get(self, **filters) -> SqlModel:
        async with self._session_factory() as session:
            row = await session.execute(select(self.model).filter_by(**filters))
            try:
                result = row.scalar_one()
            except NoResultFound:
                raise NoRowsFoundError(
                    f"For model {self.model.__name__} with next filters: {filters}"
                )
            except MultipleResultsFound:
                raise MultipleRowsFoundError(
                    f"For model {self.model.__name__} with next filters: {filters}"
                )
        return result
