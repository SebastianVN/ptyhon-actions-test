from calculadora import restar


def test_restar():
    assert restar(9, 3) == 6
    assert restar(0, 0) == 0
    assert restar(-2, 4) == -6
