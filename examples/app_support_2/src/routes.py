from fastapi import APIRouter

from .support.controllers import support_controller, admin_controller


def get_apps_router():
    router = APIRouter()
    router.include_router(admin_controller.router)
    router.include_router(support_controller.router)
    return router
