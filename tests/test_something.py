import pytest
import sys


def test_ok():
    assert True


def test_fail():
    assert False


@pytest.mark.xfail    
def test_xfail():
    assert False

    
@pytest.mark.skipif(True, reason="always gets skipped")
def test_skip():
    assert False

    
@pytest.mark.skipif(sys.version_info < (3, 10), reason="requires python 3.10 or higher")
def test_skip_if_python_le_3_10():
    assert True

    
@pytest.mark.skipif(sys.version_info < (3, 9), reason="requires python 3.9 or higher")
def test_skip_if_python_le_3_9():
    assert True

    
@pytest.mark.skipif(sys.version_info < (3, 8), reason="requires python 3.8 or higher")
def test_skip_if_python_le_3_8():
    assert True

