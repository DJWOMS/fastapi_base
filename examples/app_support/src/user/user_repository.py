from src.lib.repositories.sqlalchemy_repository import SqlAlchemyRepository
from src.config.database.db_helper import db_helper

from .user_model import UserProfileModel


class UserRepository(SqlAlchemyRepository):
    model = UserProfileModel


user_repository = UserRepository(db_session=db_helper.get_db_session)
