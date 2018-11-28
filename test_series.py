from .series import fibonacci
from .series import lucas
from .series import sum_series

def test_fibonacci1():
    assert(fibonacci(0) == 0)

def test_fibonacci2():
    assert(fibonacci(2) == 1)

def test_fibonacci3():
    assert(fibonacci(3) == 2)

def test_fibonacci4():
    assert(fibonacci(6) == 8)

def test_lucas1():
    assert(lucas(2) == 3)

def test_lucas2():
    assert(lucas(4) == 7)

def test_lucas3():
    assert(lucas(6) == 18)    


def test_sum_series1():
    assert(sum_series(2) == 1)

def test_sum_series2():
    assert(sum_series(6) == 8)

def test_sum_series3():
    assert(sum_series(2,2,1) == 3)

def test_sum_series4():
    assert(sum_series(6,2,1) == 18)