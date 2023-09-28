from fastapi import APIRouter

from src.support.routes import equipment_router


def get_apps_router():
    router = APIRouter()
    router.include_router(equipment_router)
    return router
