def torre_hanoi(numero_discos, torre_origen, torre_destino, torre_auxiliar):
    if numero_discos == 1:
        print(f"Mover disco 1 de la torre {torre_origen} a la torre {torre_destino}")
        return
    torre_hanoi(numero_discos - 1, torre_origen, torre_auxiliar, torre_destino)
    print(f"Mover disco {numero_discos} de la torre {torre_origen} a la torre {torre_destino}")
    torre_hanoi(numero_discos - 1, torre_auxiliar, torre_destino, torre_origen)

# Ejemplo de uso:
torre_hanoi(3, "A", "C", "B")



from io import StringIO
import sys

def test_torre_hanoi():
    captured_output = StringIO()  # Para capturar la salida estándar
    sys.stdout = captured_output  # Redirigir la salida estándar

    # Caso de prueba 1
    torre_hanoi(1, "A", "C", "B")
    output = captured_output.getvalue().strip()
    assert output == "Mover disco 1 de la torre A a la torre C"

    captured_output.truncate(0)  # Limpiar la salida capturada
    sys.stdout = sys.__stdout__  # Restaurar la salida estándar

    captured_output = StringIO()
    sys.stdout = captured_output

    # Caso de prueba 2
    torre_hanoi(2, "A", "C", "B")
    output = captured_output.getvalue().strip()
    assert output == "Mover disco 1 de la torre A a la torre B\nMover disco 2 de la torre A a la torre C\nMover disco 1 de la torre B a la torre C"

    captured_output.truncate(0)
    sys.stdout = sys.__stdout__

    captured_output = StringIO()
    sys.stdout = captured_output

    # Caso de prueba 3
    torre_hanoi(3, "A", "C", "B")
    output = captured_output.getvalue().strip()
    assert output == "Mover disco 1 de la torre A a la torre C\nMover disco 2 de la torre A a la torre B\nMover disco 1 de la torre C a la torre B\nMover disco 3 de la torre A a la torre C\nMover disco 1 de la torre B a la torre A\nMover disco 2 de la torre B a la torre C\nMover disco 1 de la torre A a la torre C"

    captured_output.truncate(0)
    sys.stdout = sys.__stdout__

    print("Todos los casos de prueba han pasado exitosamente.")

if __name__ == "__main__":
    test_torre_hanoi()
