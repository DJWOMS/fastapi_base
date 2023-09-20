from fastapi import APIRouter

from .support.routers import support, admin
from .users.routers import permission, user


def get_apps_router():
    router = APIRouter()
    router.include_router(admin.router)
    router.include_router(support.router)
    router.include_router(permission.router)
    router.include_router(user.router)
    return router
