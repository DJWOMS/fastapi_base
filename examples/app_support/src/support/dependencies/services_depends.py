from typing import Annotated

from fastapi import Depends

from ..repositories.category_repository import CategoryRepository
from ..repositories.support_repository import SupportRepository


ICategoryRepository = Annotated[CategoryRepository, Depends(CategoryRepository)]
ISupportRepository = Annotated[SupportRepository, Depends(SupportRepository)]
