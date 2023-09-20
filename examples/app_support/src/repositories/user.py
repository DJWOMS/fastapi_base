from ..share.repository import SqlAlchemyRepository, SqlModel
from core.database.db_helper import db_helper
from ..models.user import User, Permission


class PermissionRepository(SqlAlchemyRepository):
    model = Permission


class UserRepository(SqlAlchemyRepository):
    model = User

    async def create_superuser(self, data: dict) -> SqlModel:
        async with self._session_factory() as session:
            instance = self.model(**data)
            session.add(instance)
            await session.commit()
            await session.refresh(instance)
            return instance


permission_repository = PermissionRepository(db_session=db_helper.get_db_session)
user_repository = UserRepository(db_session=db_helper.get_db_session)
