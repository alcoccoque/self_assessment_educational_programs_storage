import pytest

from self_assessment_educational_programs_storage.users.models import User
from self_assessment_educational_programs_storage.users.tests.factories import (
    UserFactory,
)


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user(db) -> User:
    return UserFactory()
