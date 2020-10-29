import pytest


@pytest.fixture(scope="session")
def datadir():
    return "datasets"
