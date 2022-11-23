from abc import ABC, abstractmethod
from typing import Optional
from uuid import UUID
from pydantic import EmailStr

from models.user import User, UserWithId


class UserRepository(ABC):
    @abstractmethod
    def get(self, user_id: UUID) -> Optional[UserWithId]:
        pass

    @abstractmethod
    def find_by_email(self, email: EmailStr) -> Optional[UserWithId]:
        pass

    @abstractmethod
    def save(self, user: User) -> UserWithId:
        pass
