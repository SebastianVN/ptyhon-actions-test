from calculadora import multiplicar


def test_multiplicar():
    assert multiplicar(2, 3) == 6
    assert multiplicar(0, 0) == 0
    assert multiplicar(-2, 4) == -8
