from mock.auth_api import auth_api_mock
from .user import UserServiceDep


class AuthService:

    async def check_token(self, token) -> bool:
        if user := await auth_api_mock(token=token):
            return await UserServiceDep.get(user.get("id"))
        return False

    async def __call__(self):
        return await self.check_token("12345")
