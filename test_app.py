import pytest
from app import add

def test_add():
    assert add(2, 2) == 4
    assert add(-5, 5) == 0
