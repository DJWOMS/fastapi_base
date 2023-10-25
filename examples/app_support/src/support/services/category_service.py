from fastapi import Depends

from src.lib.services.base_service import BaseService

from ..repositories.category_repository import ICetegoryRepository, CategoryRepository
from ..models.category_model import CategoryModel


class CategoryService(BaseService):

    def __init__(self, repository: ICetegoryRepository = Depends()):
        self.repository = repository

    async def create(self, DTO):
        if await self.repository.exists(name=DTO.name):
            raise Exception("Category already exists")
        self.repository.create(model=DTO)

    async def filter(
            self,
            fields: list[str] | None = None,
            order: list[str] | None = None,
            limit: int | None = None,
            offset: int | None = None
    ) -> list[CategoryModel] | None:
        return await self.repository.filter(
            fields=fields,
            order=order,
            limit=limit,
            offset=offset
        )

    async def exists(self, name: str) -> bool:
        return await self.repository.exists(name=name)


# category_service = CategoryService(repository=category_repository)
