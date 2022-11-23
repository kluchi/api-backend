from uuid import UUID
from pydantic import BaseModel, EmailStr


class User(BaseModel, frozen=True, orm_mode=True):
    email: EmailStr


class UserWithId(User):
    id: UUID
