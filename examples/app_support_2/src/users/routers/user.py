from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_400_BAD_REQUEST

from ..schemas.request.user import CreateSuperUser
from ..schemas.response.user import UserResponse
from ..services.user import user_service

router = APIRouter(prefix="/user", tags=["user"])


@router.post("/superuser")
async def create_super_user(data: CreateSuperUser) -> UserResponse:
    try:
        return await user_service.create_admin(model=data)
    except Exception as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))
