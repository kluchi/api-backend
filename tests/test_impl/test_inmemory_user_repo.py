from uuid import uuid4
import pytest

from impl.in_memory import InMemoryUserRepo
from models.user import User, UserWithId


@pytest.fixture
def repo():
    return InMemoryUserRepo()


def test_empty_repo_should_return_none_on_lookup(repo):
    assert repo.find_by_email("example@example.com") is None
    assert repo.get(uuid4()) is None


@pytest.fixture
def created_user(repo):
    return repo.save(User(email="example@mail.com",
                          first_name="name",
                          last_name="name"))


def test_repo_should_return_created_user_on_save(created_user):
    assert isinstance(created_user, UserWithId)


def test_repo_should_overwrite_user_on_save(repo, created_user):
    new_user_data = UserWithId(email="new_email@example.com",
                               first_name=created_user.first_name,
                               last_name=created_user.last_name,
                               id=created_user.id)
    repo.save(new_user_data)
    assert repo.get(created_user.id) == new_user_data


@pytest.fixture
def user2(repo):
    return repo.save(User(email="second@mail.com",
                          first_name="name",
                          last_name="name"))


def test_repo_should_find_user_by_email(repo, user2, created_user):
    assert repo.find_by_email("example@mail.com") \
        == \
        UserWithId(email="example@mail.com",
                   first_name=created_user.first_name,
                   last_name=created_user.last_name,
                   id=created_user.id)
