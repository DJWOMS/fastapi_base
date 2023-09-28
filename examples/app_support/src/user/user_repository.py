from src.lib.repositories.sqlalchemy_repository import SqlAlchemyRepository
from src.config.database.db_helper import db_helper

from .user_model import UserProfileModel
from .user_schema import CreateUserProfileSchema, UpdateUserProfileSchema


class UserRepository(
    SqlAlchemyRepository[UserProfileModel, CreateUserProfileSchema, UpdateUserProfileSchema]
):
    pass


user_repository = UserRepository(model=UserProfileModel, db_session=db_helper.get_db_session)
