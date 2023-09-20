from fastapi import APIRouter

from ..schemas.user import PermissionCreate, PermissionResponse
from ..services.user import permission_service

router = APIRouter(prefix="/permission", tags=["user"])


@router.post("/")
async def create_permission(
        data: PermissionCreate,
) -> PermissionResponse:
    return await permission_service.create(model=data)
