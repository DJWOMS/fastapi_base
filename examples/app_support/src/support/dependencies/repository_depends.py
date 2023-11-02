from typing import Annotated

from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession
from src.config.database.db_helper import db_helper

IAsyncSession = Annotated[AsyncSession, Depends(db_helper.get_session)]
