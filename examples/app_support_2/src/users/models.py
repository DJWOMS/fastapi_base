from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.share.models import Base


class Permission(Base):
    __tablename__ = "permissions"

    name: Mapped[str]
    code: Mapped[int]
    users: Mapped["User"] = relationship("User", back_populates="permission")


class User(Base):
    __tablename__ = "users"

    username: Mapped[str]
    email: Mapped[str]
    password: Mapped[str]
    permission_id: Mapped[int] = mapped_column(ForeignKey("permissions.id"))
    permission: Mapped["Permission"] = relationship(
        "Permission",
        back_populates="users",
        lazy="joined"
    )
