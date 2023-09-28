from ..schemas.base_schema import PyModel
from ..repositories.sqlalchemy_repository import ModelType, SqlAlchemyRepository


class BaseService:
    """Базовый класс для сервисов

    """
    repository: SqlAlchemyRepository
    def __init__(self, repository: SqlAlchemyRepository) -> None:
        self.repository: SqlAlchemyRepository = repository

    async def create(self, data: PyModel, *args, **kwargs) -> ModelType:
        return await self.repository.create(data=data.model_dump())

    async def update(self, pk: int, data: PyModel) -> ModelType:
        return await self.repository.update(data=data.model_dump(), id=pk)

    async def delete(self, pk: int) -> None:
        await self.repository.delete(id=pk)

    async def get_single(self, pk: int) -> ModelType:
        return await self.repository.get_single(id=pk)

    async def get_multi(self):
        return await self.repository.get_multi()
