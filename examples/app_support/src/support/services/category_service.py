from ..dependencies.services_depends import ICategoryRepository
from ..dtos.category_dto import (
    CategoryListDto,
    CategoryCreateDto,
    CategoryParams,
    CategoryDto, CategoryUpdateDto
)


class CategoryService:
    """Сервис для работы с категориями"""
    def __init__(self, repository: ICategoryRepository) -> None:
        self.repository = repository

    async def create(self, dto: CategoryCreateDto) -> CategoryDto:
        return await self.repository.create(dto=dto)

    async def update(self, pk: int, dto: CategoryUpdateDto) -> CategoryDto:
        return await self.repository.update(pk=pk, dto=dto)

    async def delete(self, pk: int) -> None:
        await self.repository.delete(pk=pk)

    async def get_multi(self, params: CategoryParams) -> list[CategoryListDto]:
        return await self.repository.get_multi(**params.__dict__)
