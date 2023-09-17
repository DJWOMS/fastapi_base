from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from share.models import Base


class Permission(Base):
    __tablename__ = "permissions"

    name: Mapped[str]
    code: Mapped[int]


class User(Base):
    __tablename__ = "users"

    username: Mapped[str]
    email: Mapped[str]
    password: Mapped[str]
    permission_id: Mapped[int] = mapped_column(ForeignKey("permissions.id"))
    # permissions: Mapped[list[Permission]]

