from src.repositories.sqlalchemy_repository import ModelType
from src.services.base_service import BaseService
from ..repositories.category_repository import category_repository


class CategoryService(BaseService):

    async def filter(
            self,
            fields: list[str] | None = None,
            order: list[str] | None = None,
            limit: int | None = None,
            offset: int | None = None
    ) -> list[ModelType] | None:
        return await self.repository.filter(
            fields=fields,
            order=order,
            limit=limit,
            offset=offset
        )

    async def exists(self, name: str) -> bool:
        return await self.repository.exists(name=name)


category_service = CategoryService(repository=category_repository)
