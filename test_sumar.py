from calculadora import sumar


def test_sumar():
    assert sumar(2, 3) == 5
    assert sumar(0, 0) == 0
    assert sumar(-9, 10) == 1
