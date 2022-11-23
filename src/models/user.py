from uuid import UUID
from pydantic import BaseModel, EmailStr


class User(BaseModel, frozen=True, orm_mode=True):
    email: EmailStr
    first_name: str
    last_name: str
    bio: str = ""


class UserWithId(User):
    id: UUID
