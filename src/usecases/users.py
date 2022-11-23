from pydantic import BaseModel, EmailStr
from models.user import User

from repositories.user_repository import UserRepository


class UserCreationData(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str


class CreateUser:
    def __init__(self, users: UserRepository):
        self._users = users

    def run(self, data: UserCreationData):
        if self._users.find_by_email(data.email) is not None:
            raise ValueError("user already exists")
        self._users.save(User.from_orm(data))
