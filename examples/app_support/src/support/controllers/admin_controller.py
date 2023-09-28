from typing import Annotated

from fastapi import Depends, HTTPException, Query, APIRouter
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT

from ...auth.auth_service import is_admin
from ...user.user_schema import UserSchema

from ..schemas.category_schema import (
    CategoryCreate,
    CategoryResponse,
    CategoryListResponse
)
from ..services.category_service import category_service


router = APIRouter(prefix="/admin", tags=["admin"])


@router.get("/category/exists")
async def exists_category_for_name(name: str, user: UserSchema = Depends(is_admin)) -> bool:
    try:
        return await category_service.exists(name)
    except Exception as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))


@router.post("/category")
async def create_category(
        data: CategoryCreate,
        user: UserSchema = Depends(is_admin)
) -> CategoryResponse:
    try:
        return await category_service.create(model=data)
    except Exception as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))


@router.put("/category/{pk}")
async def update_category(
        pk: int,
        data: CategoryCreate,
        user: UserSchema = Depends(is_admin)
) -> CategoryResponse:
    try:
        return await category_service.update(pk=pk, model=data)
    except Exception as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))


@router.delete("/category/{pk}", status_code=HTTP_204_NO_CONTENT)
async def delete_category(pk: int, user: UserSchema = Depends(is_admin)):
    try:
        return await category_service.delete(pk=pk)
    except Exception as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))


@router.get("/category/{pk}")
async def get_single_category(pk: int, user: UserSchema = Depends(is_admin)) -> CategoryResponse:
    try:
        return await category_service.get(pk=pk)
    except Exception as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))


@router.get("/category")
async def filter_category(
        fields: Annotated[list, Query()] = [],
        order: Annotated[list, Query()] = [],
        limit: int | None = None,
        offset: int | None = None,
        user: UserSchema = Depends(is_admin)
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
