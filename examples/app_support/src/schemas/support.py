from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    pass


class CategoryResponse(CategoryBase):
    id: int


class CategoryListResponse(BaseModel):
    id: int | None = None
    name: str | None = None


class SupportBase(BaseModel):
    category_id: int
    username: str
    text: str


class SupportCreate(SupportBase):
    pass


class SupportResponse(SupportBase):
    id: int
