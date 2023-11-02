from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ...lib.models.base_model import Base

# if TYPE_CHECKING:
from ...user.models.user_model import UserModel


class RequestSupportModel(Base):
    """Модель поддержки

    :param category_id: id категории FK
    :param username: имя пользователя
    :param text: текст заявки
    """
    __tablename__ = "request_support"

    text: Mapped[str]
    username: Mapped[str] = mapped_column(nullable=True)
    email: Mapped[str] = mapped_column(nullable=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    is_active: Mapped[bool] = mapped_column(default=True)
    is_working: Mapped[bool] = mapped_column(default=False)

    category: Mapped["CategoryModel"] = relationship("CategoryModel", lazy="raise_on_sql")
    # user: Mapped["UserModel"] = relationship("UserModel", lazy="raise_on_sql")
