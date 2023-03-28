from ej4 import Polinomio

def mostrar_menu():
    print('--- Menú ---')
    print('1. Crear un polinomio')
    print('2. Sumar dos polinomios')
    print('3. Restar dos polinomios')
    print('4. Multiplicar dos polinomios')
    print('5. Dividir un polinomio por otro')
    print('6. Eliminar un término de un polinomio')
    print('7. Determinar si un término existe en un polinomio')
    print('8. Mostrar un polinomio')
    print('0. Salir')

def crear_polinomio():
    coeficientes = []
    grado = int(input('Ingrese el grado del polinomio: '))
    for i in range(grado+1):
        coeficiente = int(input(f'Ingrese el coeficiente de x^{grado-i}: '))
        coeficientes.append(coeficiente)
    return Polinomio(coeficientes)

def sumar_polinomios():
    p1 = crear_polinomio()
    p2 = crear_polinomio()
    p3 = p1.sumar(p2)
    print(f'Resultado: {p3}')

def restar_polinomios():
    p1 = crear_polinomio()
    p2 = crear_polinomio()
    p3 = p1.restar(p2)
    print(f'Resultado: {p3}')

def multiplicar_polinomios():
    p1 = crear_polinomio()
    p2 = crear_polinomio()
    p3 = p1.multiplicar(p2)
    print(f'Resultado: {p3}')

def dividir_polinomios():
    p1 = crear_polinomio()
    p2 = crear_polinomio()
    p3 = p1.dividir(p2)
    print(f'Resultado: {p3}')

def eliminar_termino():
    p = crear_polinomio()
    termino = int(input('Ingrese el grado del término a eliminar: '))
    p = p.eliminar_termino(termino)
    print(f'Resultado: {p}')

def existe_termino():
    p = crear_polinomio()
    termino = int(input('Ingrese el grado del término a buscar: '))
    if p.existe_termino(termino):
        print('El término existe en el polinomio.')
    else:
        print('El término no existe en el polinomio.')

def mostrar_polinomio():
    p = crear_polinomio()
    print(f'{p}')

def main():
    while True:
        mostrar_menu()
        opcion = int(input('Ingrese la opción deseada: '))
        if opcion == 0:
            print('¡Hasta luego!')
            break
        elif opcion == 1:
            polinomio = crear_polinomio()
            print(f'Polinomio creado: {polinomio}')
        elif opcion == 2:
            sumar_polinomios()
        elif opcion == 3:
            restar_polinomios()
        elif opcion == 4:
            multiplicar_polinomios()
        elif opcion == 5:
            dividir_polinomios()
       
