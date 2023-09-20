from typing import Annotated

from fastapi import Depends
from core.database.db_helper import db_helper
from sqlalchemy.ext.asyncio import AsyncSession

from ..share.repository import AbstractRepository, SqlAlchemyRepository, SqlModel

from ..share.service import BaseService
from ..schemas.user import UserCreate
from ..repositories.user import user_repository, permission_repository, UserRepository, PermissionRepository


class PermissionService(BaseService):

    async def get_by_name(self, name: str) -> SqlModel:
        return await self.repository.get(name=name)


class UserService(BaseService):

    async def create_admin(self, model: UserCreate):
        new_data = model.model_dump()
        permission = await PermissionServiceDep.get_by_name("admin")
        new_data["permission_id"] = permission.id # PermissionService().get_by_name("admin")
        return await self.repository.create(data=new_data)


class ProviderService:
    def __init__(self, service: BaseService, repository: AbstractRepository):
        self._service = service
        self._repository = repository
        # db = providers.Singleton(Database, db_url=config.db.url)
        #
        # repository = providers.Factory(
        #     UserRepository,
        #     session_factory=db.provided.session,
        # )
        #
        # service = providers.Factory(
        #     UserService,
        #     user_repository=user_repository,
        # )
    @staticmethod
    def get_repository(session: AsyncSession = Depends(db_helper.get_db_session)):
        return PermissionRepository(session)

    def get_service(self, repository: AbstractRepository = Depends(get_repository)):
        return self._service(repository=repository)

    def __call__(self):
        return self.get_service()

# p = ProviderService(PermissionService, PermissionRepository)
# Annotated[PermissionService, Depends(p)]


PermissionServiceDep = PermissionService(repository=permission_repository)

UserServiceDep = UserService(repository=user_repository) # Annotated[UserService, Depends(ProviderService(UserService, user_repository))]
