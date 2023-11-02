from sqlalchemy import exc
from fastapi import Depends, HTTPException, APIRouter
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND

from ...dependencies import IsAdmin

from ..dtos.category_dto import (
    CategoryListDto,
    CategoryCreateDto,
    CategoryUpdateDto,
    CategoryParams,
    CategoryDto
)
from ..services.category_service import CategoryService


router = APIRouter(prefix="/admin", tags=["admin"], dependencies=[IsAdmin])


@router.post("/category")
async def create_category(
        dto: CategoryCreateDto,
        service: CategoryService = Depends(),
) -> CategoryDto:
    """Создание категории"""
    return await service.create(dto=dto)


@router.put("/category/{pk}")
async def update_category(
        pk: int,
        dto: CategoryUpdateDto,
        service: CategoryService = Depends()
) -> CategoryDto:
    """Обновление категории"""
    try:
        return await service.update(pk=pk, dto=dto)
    except exc.NoResultFound:
        raise HTTPException(HTTP_404_NOT_FOUND, "Категория не найдена.")


@router.delete("/category/{pk}", status_code=HTTP_204_NO_CONTENT)
async def delete_category(pk: int, service: CategoryService = Depends()):
    """Удаление категории"""
    return await service.delete(pk=pk)


@router.get("/category")
async def get_list_category(
        params: CategoryParams = Depends(),
        service: CategoryService = Depends()
) -> list[CategoryListDto]:
    """Фильтрация категорий"""
    return await service.get_multi(params=params)
