import warnings

from src import print_os


def test_print_os(datadir, tmpdir):
    warnings.warn("some message", DeprecationWarning)
    warnings.warn(f"datadir: {datadir}", FutureWarning)
    warnings.warn(f"tmpdir: {tmpdir}", UserWarning)
    assert print_os() is None
