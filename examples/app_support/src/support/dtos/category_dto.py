from dataclasses import dataclass
from fastapi import Query
from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str


class CategoryCreateDto(CategoryBase):
    pass


class CategoryUpdateDto(CategoryBase):
    pass


class CategoryDto(CategoryBase):
    id: int


class CategoryListDto(BaseModel):
    id: int | None = None
    name: str | None = None


class CategoryParams:
    """Параметры для фильтрации и сортировки категорий"""
    def __init__(
            self,
            order: str = Query(
                default='id',
                description="Название столбца для сортировки, если указать "
                            "минус, то сортировка от меньшего к большему."
            ),
            limit: int = 50,
            offset: int = Query(default=0, description="Смещение на"),
    ):
        self.order = order
        self.limit = limit
        self.offset = offset
