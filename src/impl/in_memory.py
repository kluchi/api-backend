from typing import Dict, Optional
from uuid import UUID, uuid4

from pydantic import EmailStr
from models.user import User, UserWithId
from repositories.user_repository import UserRepository


class InMemoryUserRepo(UserRepository):
    def __init__(self) -> None:
        super().__init__()
        self._storage: Dict[UUID, UserWithId] = {}

    def get(self, user_id: UUID) -> Optional[UserWithId]:
        return self._storage.get(user_id)

    def find_by_email(self, email: EmailStr) -> Optional[UserWithId]:
        for user in self._storage.values():
            if user.email == email:
                return user
        return None

    def save(self, user: User) -> UserWithId:
        if isinstance(user, UserWithId):
            self._storage[user.id] = user
            return user

        new_id = uuid4()
        new_user = UserWithId(id=new_id, **user.dict())
        self._storage[new_id] = new_user
        return new_user
