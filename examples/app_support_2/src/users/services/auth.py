from mock.auth_api import auth_api_mock

from core.share.interfaces.permissions import UserModel
from .user import user_service


class AuthService:

    async def check_token(self, token) -> UserModel | bool:
        if user := await auth_api_mock(token=token):
            return await user_service.get(user.get("id"))
        return False

    async def __call__(self) -> UserModel | bool:
        return await self.check_token("12345")
