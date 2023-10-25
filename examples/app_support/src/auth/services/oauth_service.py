from fastapi import HTTPException
from starlette.status import HTTP_401_UNAUTHORIZED

from ..user_schema import UserSchema


class OAuthService:
    def __init__(self, role: str):
        self.role = role

    async def auth(self):
        # Код обращения к удаленному сервису авторизации
        return UserSchema(id=1, username="John", role="admin")

    async def is_admin(self):
        user = await self.auth()
        if user.role == self.role:
            return user
        raise HTTPException(HTTP_401_UNAUTHORIZED, "Not admin")

    def __call__(self):
        # В зависимости должно быть получение токена
        return self.is_admin()


is_admin = AuthService("admin")
