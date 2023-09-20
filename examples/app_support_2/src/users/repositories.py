from core.share.repository import SqlAlchemyRepository
from core.database.db_helper import db_helper

from .models import User, Permission


class PermissionRepository(SqlAlchemyRepository):
    model = Permission


class UserRepository(SqlAlchemyRepository):
    model = User


permission_repository = PermissionRepository(db_session=db_helper.get_db_session)
user_repository = UserRepository(db_session=db_helper.get_db_session)
