from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_400_BAD_REQUEST

from .user_schema import CreateUserProfileSchema
from .user_service import user_service

router = APIRouter(prefix='/user', tags=["user"])


@router.post("/", response_model=CreateUserProfileSchema)
async def create_profile_user(data: CreateUserProfileSchema) -> CreateUserProfileSchema:
    try:
        return await user_service.create(data)
    except Exception as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))
