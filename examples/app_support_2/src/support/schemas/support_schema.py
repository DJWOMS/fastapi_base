from pydantic import BaseModel


class SupportBase(BaseModel):
    category_id: int
    username: str
    text: str


class SupportCreate(SupportBase):
    pass


class SupportUpdate(SupportBase):
    pass


class SupportResponse(SupportBase):
    id: int
