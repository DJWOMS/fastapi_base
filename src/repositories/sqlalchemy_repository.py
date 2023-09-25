from typing import Type, TypeVar, Optional, Generic

from pydantic import BaseModel
from sqlalchemy import delete, select, update
from sqlalchemy.ext.asyncio import AsyncSession

from ..models.base_model import Base

from .base_repository import AbstractRepository


ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class SqlAlchemyRepository(AbstractRepository, Generic[ModelType, CreateSchemaType, UpdateSchemaType]):

    def __init__(self, model: Type[ModelType], db_session: AsyncSession):
        self._session_factory = db_session
        self.model = model

    async def create(self, data: CreateSchemaType) -> ModelType:
        async with self._session_factory() as session:
            instance = self.model(**data)
            session.add(instance)
            await session.commit()
            await session.refresh(instance)
            return instance

    async def update(self, data: UpdateSchemaType, **filters) -> ModelType:
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
            offset: int = 0
    ) -> list[ModelType]:
        async with self._session_factory() as session:
            stmt = select(self.model).order_by(*order).limit(limit).offset(offset)
            row = await session.execute(stmt)
            return row.scalars().all()
