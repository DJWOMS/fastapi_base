from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from share.models import Base


class Category(Base):
    __tablename__ = "categories"

    name: Mapped[str] = mapped_column(String(50), unique=True)


class Support(Base):
    __tablename__ = "supports"

    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    username: Mapped[str]
    text: Mapped[str]
