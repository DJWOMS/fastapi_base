from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base_model import Base


class CategoryModel(Base):
    __tablename__ = "categories"

    name: Mapped[str] = mapped_column(String(50), unique=True)
