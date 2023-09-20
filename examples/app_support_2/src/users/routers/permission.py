from fastapi import APIRouter

from ..schemas.response.permission import PermissionResponse
from ..schemas.request.permission import PermissionCreate
from ..services.user import permission_service

router = APIRouter(prefix="/permission", tags=["user"])


@router.post("/")
async def create_permission(
        data: PermissionCreate,
) -> PermissionResponse:
    return await permission_service.create(model=data)
