import pytest


@pytest.fixture(scope="session")
def datadir(tmpdir_factory):
    return tmpdir_factory.mktemp("datasets")
