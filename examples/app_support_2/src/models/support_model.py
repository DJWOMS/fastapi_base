from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .base_model import Base


class SupportModel(Base):
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    username: Mapped[str]
    text: Mapped[str]
