from ej4 import Polinomio

# prueba la función restar
def test_restar():
    p1 = Polinomio([2, 0, 1, 3])
    p2 = Polinomio([1, 2, 0, 4, 5])
    p3 = p1.restar(p2)
    assert str(p3) == '3x^4 - 2x^3 - 1x^2 - 1x^1 - 2x^0'

# prueba la función dividir
def test_dividir():
    p1 = Polinomio([2, 0, 1, 3])
    p2 = Polinomio([1, 2, 0, 4, 5])
    p3 = p1.dividir(p2)
    assert str(p3) == '0.5x^2 - 1.5x^1 + 1.0x^0'

# prueba la función eliminar_termino
def test_eliminar_termino():
    p1 = Polinomio([2, 0, 1, 3])
    p2 = p1.eliminar_termino(2)
    assert str(p2) == '3x^3 + 1x^1 + 2x^0'

# prueba la función existe_termino
def test_existe_termino():
    p1 = Polinomio([2, 0, 1, 3])
    assert p1.existe_termino(2) == True
    assert p1.existe_termino(4) == False

if __name__ == '__main__':
    test_restar()
    test_dividir()
    test_eliminar_termino()
    test_existe_termino()
    print('Todos los tests han pasado.')
