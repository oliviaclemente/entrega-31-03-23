#import numpy as np
from ej2 import determinante_sarrus

def mostrar_menu():
    print("1. Sumar dos matrices")
    print("2. Restar dos matrices")
    print("3. Multiplicar una matriz por un escalar")
    print("4. Calcular el determinante de una matriz")
    print("5. Salir")

def pedir_matriz():
    print("Introduzca los elementos de la matriz separados por comas:")
    fila1 = input().split(",")
    fila2 = input().split(",")
    fila3 = input().split(",")
    matriz = np.array([fila1, fila2, fila3], dtype=int)
    return matriz

def sumar_matrices():
    print("Introduzca la primera matriz:")
    matriz1 = pedir_matriz()
    print("Introduzca la segunda matriz:")
    matriz2 = pedir_matriz()
    resultado = matriz1 + matriz2
    print("El resultado de la suma es:")
    print(resultado)

def restar_matrices():
    print("Introduzca la primera matriz:")
    matriz1 = pedir_matriz()
    print("Introduzca la segunda matriz:")
    matriz2 = pedir_matriz()
    resultado = matriz1 - matriz2
    print("El resultado de la resta es:")
    print(resultado)

def multiplicar_escalar():
    print("Introduzca la matriz:")
    matriz = pedir_matriz()
    print("Introduzca el escalar:")
    escalar = int(input())
    resultado = matriz * escalar
    print("El resultado de la multiplicación por escalar es:")
    print(resultado)

def calcular_determinante():
    print("Introduzca la matriz:")
    matriz = pedir_matriz()
    determinante = determinante_sarrus(matriz)
    print("El determinante de la matriz es:", determinante)

def main():
    while True:
        mostrar_menu()
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            sumar_matrices()
        elif opcion == 2:
            restar_matrices()
        elif opcion == 3:
            multiplicar_escalar()
        elif opcion == 4:
            calcular_determinante()
        elif opcion == 5:
            break
        else:
            print("Opción no válida. Introduzca una opción del 1 al 5.")

if __name__ == '__main__':
    main()
