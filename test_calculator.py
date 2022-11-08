from calculator import MiniCalculator

mc = MiniCalculator(10, 5)

def test_add():
    assert mc.add() == 15

def test_subtract():
    assert mc.subtract() == 5

def test_substract_reverse():
    assert mc.subtract(reverse=True) == -5
