import datetime

from sqlalchemy import TIMESTAMP, func
from sqlalchemy.orm import DeclarativeBase, Mapped, declared_attr, mapped_column


class Base(DeclarativeBase):
    __abstarct__ = True

    id: Mapped[int] = mapped_column(primary_key=True)
    # created_at: Mapped[datetime.datetime] = mapped_column(
    #     TIMESTAMP(timezone=True)
    # )
    # updated_at: Mapped[datetime.datetime] = mapped_column(
    #     TIMESTAMP(timezone=True),
    #     onupdate=datetime.datetime.now
    # )
    created_at: Mapped[datetime] = mapped_column(default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        default=func.now(),
        onupdate=func.now()
    )
    # type_annotation_map = {
    #     datetime.datetime: TIMESTAMP(timezone=True),
    # }

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"
