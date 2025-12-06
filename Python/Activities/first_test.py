import pytest
import math

#@pytest.mark.activity
def test_sqrt():
    num = 25
    assert math.sqrt(num)==5
def test_square():
    num= 7
    assert num*num == 40

@pytest.mark.compare
@pytest.mark.equal
def test_equality():
    assert 10==11

