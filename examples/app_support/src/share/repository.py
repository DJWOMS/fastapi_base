from abc import ABC, abstractmethod
from typing import NewType

from sqlalchemy import delete, insert, update
from sqlalchemy.exc import MultipleResultsFound, NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import load_only

from ..share.errors import (
    DBError,
    MultipleRowsFoundError,
    NoRowsFoundError,
)

from ..share.models import Base


SqlModel = NewType("SqlModel", Base)


class AbstractRepository(ABC):
    model = None

    @abstractmethod
    async def create(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def update(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def delete(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def get(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def filter(self, **filters):
        raise NotImplementedError

    @abstractmethod
    async def all(self, **filters):
        raise NotImplementedError

    @abstractmethod
    async def exists(self, **filters):
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):
    model = None

    def __init__(self, db_session: AsyncSession):
        self._session_factory = db_session

    async def create(self, data: dict) -> SqlModel:
        async with self._session_factory() as session:
            instance = self.model(**data)
            session.add(instance)
            await session.commit()
            return instance

    async def update(self, data: dict, **filters):
        async with self._session_factory() as session:
            if not data:
                raise DBError(
                    f"Passed empty dictionary for update method in model {self.model.__name__}"
                )
            stmt = update(self.model).values(**data).filter_by(**filters).returning(self.model)
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one()

    async def delete(self, **filters):
        async with self._session_factory() as session:
            result = await session.execute(delete(self.model).filter_by(**filters))
            if result.rowcount == 0:
                raise NoRowsFoundError(
                    f"For model {self.model.__name__} with next filters: {filters}"
                )
            await session.commit()

    async def get(self, **filters):
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

    async def filter(
        self,
        fields: list[str] | None = None,
        order: list[str] | None = None,
        limit: int | None = None,
        offset: int | None = None,
    ) -> list[SqlModel] | None:
        async with self._session_factory() as session:
            stmt = select(self.model)
            if fields:
                model_fields = [getattr(self.model, field) for field in fields]
                stmt = stmt.options(load_only(*model_fields))
            if order:
                stmt = stmt.order_by(*order)
            if limit is not None:
                stmt = stmt.limit(limit)
            if offset is not None:
                stmt = stmt.offset(offset)

            row = await session.execute(stmt)
            return row.scalars().all()

    async def all(self):
        return await self.filter()

    async def exists(self, **filters) -> bool:
        stmt = select(self.model).filter_by(**filters)
        async with self._session_factory() as session:
            result = await session.execute(stmt)
            return result.scalar() is not None

