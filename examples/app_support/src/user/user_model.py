from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from ..lib.models.base_model import Base


class UserProfileModel(Base):
    __tablename__ = "user_profiles"

    name: Mapped[str] = mapped_column(String(25))
    # Остальные поля
