from sqlalchemy.orm import Mapped

from core.share.models import Base


class Permission(Base):
    name: Mapped[str]
    code: Mapped[int]


class User(Base):
    username: Mapped[str]
    email: Mapped[str]
    password: Mapped[str]
    permissions: Mapped[list[Permission]]

