from core.share.service import BaseService

from ..models import Permission, User
from ..schemas.request.user import UserCreate
from ..repositories import user_repository, permission_repository


class PermissionService(BaseService):

    async def get_by_name(self, name: str) -> Permission:
        return await self.repository.get(name=name)


class UserService(BaseService):

    async def create_admin(self, model: UserCreate) -> User:
        new_data = model.model_dump()
        permission = await permission_service.get_by_name("admin")
        new_data["permission_id"] = permission.id
        return await self.repository.create(data=new_data)


permission_service = PermissionService(repository=permission_repository)
user_service = UserService(repository=user_repository)
