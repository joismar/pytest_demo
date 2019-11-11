from app import *

def test_sum():
    assert sum(2,3) == 5

def test_sum_output_type():
    assert type(sum(1, 2)) is int
