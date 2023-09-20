from typing import Annotated

from fastapi import Depends, HTTPException, Query
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT

from ..dependencies.permission import is_admin
from ..models import User
from ..schemas.support import (
    SupportCreate,
    SupportResponse,
    CategoryCreate,
    CategoryResponse,
    CategoryListResponse
)
from ..services.support import category_service, support_service


@router.get("/admin/category/exists")
async def exists_category_for_name(name: str, user: User = Depends(is_admin)) -> bool:
    try:
        return await category_service.exists(name)
    except Exception as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))


@router.post("/admin/category")
async def create_category(
        data: CategoryCreate,
        user: User = Depends(is_admin)
) -> CategoryResponse:
    try:
        return await category_service.create(model=data)
    except Exception as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))


@router.put("/admin/category/{pk}")
async def update_category(pk: int, data: CategoryCreate) -> CategoryResponse:
    try:
        return await category_service.update(pk=pk, model=data)
    except Exception as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))


@router.delete("/admin/category/{pk}", status_code=HTTP_204_NO_CONTENT)
async def delete_category(pk: int):
    try:
        return await category_service.delete(pk=pk)
    except Exception as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))


@router.get("/admin/category/{pk}")
async def get_single_category(pk: int) -> CategoryResponse:
    try:
        return await category_service.get(pk=pk)
    except Exception as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))


@router.get("/admin/category")
async def filter_category(
        fields: Annotated[list, Query()] = [],
        order: Annotated[list, Query()] = [],
        limit: int | None = None,
        offset: int | None = None
) -> list[CategoryListResponse] | None:
    try:
        return await category_service.filter(
            fields=fields,
            order=order,
            limit=limit,
            offset=offset
        )
    except Exception as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))
