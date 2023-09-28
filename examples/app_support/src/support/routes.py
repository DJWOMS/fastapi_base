from fastapi import APIRouter

from .controllers import admin_controller, support_controller


support_router = APIRouter()
support_router.include_router(admin_controller.router)
support_router.include_router(support_controller.router)

