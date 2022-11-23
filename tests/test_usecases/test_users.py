# pylint: disable=redefined-outer-name
from unittest.mock import Mock, MagicMock
import pytest
from pytest import fixture
from models.user import User
from usecases.users import CreateUser, UserCreationData


@fixture
def repo():
    mock = Mock()
    mock.save = MagicMock(side_effect=lambda item: item)
    mock.find_by_email = MagicMock(
        side_effect=lambda email:
            object() if email == "existing@mail.com" else None)
    return mock


def test_usecase_should_save_on_user_creation(repo):
    data = UserCreationData(email="example@mail.com", password="pass")
    CreateUser(repo).run(data)
    repo.save.assert_called_with(User(email="example@mail.com"))


def test_usecase_should_check_if_user_already_exists(repo):
    data = UserCreationData(email="example@mail.com", password="pass")
    CreateUser(repo).run(data)
    repo.find_by_email.assert_called_with("example@mail.com")
    repo.save.assert_called_with(User(email="example@mail.com"))


def test_usecase_should_raise_exception_on_email_conflict(repo):
    data = UserCreationData(email="existing@mail.com", password="pass")
    with pytest.raises(ValueError):
        CreateUser(repo).run(data)
