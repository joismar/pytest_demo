from app import *
import pytest

cases = [(3,5,8),(4,15,19),(3,-5,-2), (0,5,5)]

@pytest.mark.parametrize('num1, num2, expected', cases)
def test_sum(num1, num2, expected):
        assert sum(num1, num2) == expected
