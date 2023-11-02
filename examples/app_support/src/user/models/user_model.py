from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from ...lib.models.base_model import Base


class UserModel(Base):
    """Модель пользователя

    :param name

    """
    __tablename__ = "users"

    name: Mapped[str] = mapped_column(String(25))
    role: Mapped[str] = mapped_column(String(25), unique=True)
