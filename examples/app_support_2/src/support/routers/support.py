from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_400_BAD_REQUEST

from ..schemas.support import (
    SupportCreate,
    SupportResponse,
    CategoryCreate,
    CategoryResponse,
    CategoryListResponse
)
from ..services.support import category_service, support_service

router = APIRouter(prefix='/support', tags=["support"])


@router.post("/", response_model=SupportResponse)
async def create_support(data: SupportCreate) -> SupportResponse:
    try:
        return await support_service.create(data)
    except Exception as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))
