import pytest
import math

@pytest.mark.greater
def test_greater():
    x = 2
    y = 5
    assert y > x
@pytest.mark.xfail
@pytest.mark.compare
@pytest.mark.equal
def test_greater_equal():
    x = 6
    y = 6
    assert y >= x

@pytest.mark.less
def test_lesser():
    x = 2
    y = 5
    assert x < y

@pytest.mark.xfail
def test_greater1():
    x = 2
    y = 5
    assert y > x    