from src.lib.services.base_service import BaseService

from .user_repository import user_repository


class UserService(BaseService):
    pass


user_service = UserService(repository=user_repository)
