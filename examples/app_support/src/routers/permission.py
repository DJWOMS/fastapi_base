from fastapi import APIRouter

from ..schemas.user import PermissionCreate, PermissionResponse
from ..services.user import PermissionServiceDep

router = APIRouter(prefix="/permission", tags=["user"])


@router.post("/")
async def create_permission(
        data: PermissionCreate,
        # service: PermissionServiceDep
) -> PermissionResponse:
    return await PermissionServiceDep.create(model=data)
