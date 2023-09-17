from sqlalchemy.orm import Mapped

from core.share.models import Base


class Category(Base):
    name: Mapped[str]


class Support(Base):
    category: Mapped[Category]
    username: Mapped[str]
    text: Mapped[str]
