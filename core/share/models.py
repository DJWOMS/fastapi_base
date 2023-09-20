import datetime
import os
import re
import sys

from sqlalchemy import TIMESTAMP
from sqlalchemy.orm import DeclarativeBase, Mapped, declared_attr, mapped_column


class Base(DeclarativeBase):
    __abstarct__ = True

    id: Mapped[int] = mapped_column(primary_key=True)

    type_annotation_map = {
        datetime.datetime: TIMESTAMP(timezone=True),
    }

    @declared_attr.directive
    def __tablename__(cls) -> str:
        class_file_path = os.path.abspath(sys.modules[cls.__module__].__file__)

        path_elements = class_file_path.split(os.path.sep)
        src_index = path_elements.index("src")
        app_name = path_elements[src_index + 1]
        snake_string = re.sub(r"(?<!^)(?=[A-Z])", "_", cls.__name__).lower()

        return f"{app_name}_{snake_string}s"
