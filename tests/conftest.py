import pytest


@pytest.fixture(scope="session")
def tmpdir(tmpdir_factory):
    fn = tmpdir_factory.mktemp("datasets")
    return fn
