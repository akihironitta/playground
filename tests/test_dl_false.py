from src import print_os


def test_print_os(datadir, tmpdir):
    assert isinstance(print_os(), str)
