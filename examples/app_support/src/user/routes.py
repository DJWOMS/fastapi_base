from fastapi import APIRouter

from .user_contoller import router


user_router = APIRouter()
user_router.include_router(router)
