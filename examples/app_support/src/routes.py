from fastapi import APIRouter

from .support.routes import support_router
from .user.routes import user_router


def get_apps_router():
    router = APIRouter()
    router.include_router(support_router)
    router.include_router(user_router)
    return router
