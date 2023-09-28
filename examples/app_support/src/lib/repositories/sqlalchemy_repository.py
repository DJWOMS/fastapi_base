from typing import Type, Optional

from fastapi import Depends
from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from ...config.database.db_helper import db_helper
from ..models.base_model import ModelType

from .base_repository import AbstractRepository


class SqlAlchemyRepository(AbstractRepository):
    """Репозиторий для работы с базой данных

    """
    model: Type[ModelType]

    def __init__(self, db_session: AsyncSession = Depends(db_helper.get_scope_session)):
        self._session_factory = db_session

    async def create(self, data: dict) -> ModelType:
        async with self._session_factory() as session:
            instance = self.model(**data)
            session.add(instance)
            await session.commit()
            await session.refresh(instance)
            return instance

    async def update(self, data: dict, **filters) -> ModelType:
        async with self._session_factory() as session:
            stmt = update(self.model).values(**data).filter_by(**filters).returning(self.model)
            res = await session.execute(stmt)
            await session.commit()
            return res.scalar_one()

    async def delete(self, **filters) -> None:
        async with self._session_factory() as session:
            await session.execute(delete(self.model).filter_by(**filters))
            await session.commit()

    async def get_single(self, **filters) -> Optional[ModelType] | None:
        async with self._session_factory() as session:
            row = await session.execute(select(self.model).filter_by(**filters))
            return row.scalar_one_or_none()

    async def get_multi(
            self,
            order: str = "id",
            limit: int = 100,
            offset: int = 0,
            **filters
    ) -> list[ModelType]:
        async with self._session_factory() as session:
            stmt = select(self.model).filter_by(**filters).order_by(order).limit(limit).offset(offset)
            row = await session.execute(stmt)
            return row.scalars().all()
