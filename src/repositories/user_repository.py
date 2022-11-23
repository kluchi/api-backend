from abc import ABC, abstractmethod
from uuid import UUID
from pydantic import EmailStr

from models.user import User


class UserRepository(ABC):
    @abstractmethod
    def get(self, user_id: UUID):
        pass

    @abstractmethod
    def find_by_email(self, email: EmailStr):
        pass

    @abstractmethod
    def save(self, user: User) -> User:
        pass
