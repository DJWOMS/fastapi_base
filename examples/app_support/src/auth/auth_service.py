from fastapi import HTTPException
from starlette.status import HTTP_401_UNAUTHORIZED

from .user_schema import UserSchema


class AuthService:

    async def auth(self):
        # Код обращения к удаленному сервису авторизации
        return UserSchema(id=1, role="admin")

    async def is_admin(self):
        user = await self.auth()
        if user.role == "admin":
            return user
        raise HTTPException(HTTP_401_UNAUTHORIZED, "Not admin")
