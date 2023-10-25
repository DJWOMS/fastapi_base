from fastapi import HTTPException, Depends
from fastapi.security import APIKeyHeader
from sqlalchemy.orm import Session
from starlette.status import HTTP_401_UNAUTHORIZED

from ...config.database.db_helper import db_helper

from ...dto.user_schema import UserSchema

from ..user_repository import get_users_by_role


oauth2_scheme = APIKeyHeader(name="role")


class AuthService:
    def __init__(self, role: str):
        self.role = role

    def __call__(
            self,
            role: str = Depends(oauth2_scheme),
            db_session: Session = Depends(db_helper.get_session)
    ):
        if self.role == role:
            user = get_users_by_role(db_session, role=role)
            return UserSchema.model_validate(user, from_attributes=True)
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED)


is_admin = AuthService("admin")
is_client = AuthService("client")
is_manager = AuthService("manager")
