from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    name: str


class CreateUserProfileSchema(BaseModel):
    name: str
    # Остальные поля схемы


class UpdateUserProfileSchema(BaseModel):
    name: str
    # Остальные поля схемы
