from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from ...lib.models.base_model import Base


class CategoryModel(Base):
    """Категории для поддержки

    :param name: Название категории
    """
    __tablename__ = "categories"

    name: Mapped[str] = mapped_column(String(50), unique=True)
