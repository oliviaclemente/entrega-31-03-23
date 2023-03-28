class Config:
    num_discos = 74
    torre_origen = 'A'
    torre_destino = 'C'
    torre_auxiliar = 'B'

from torre_hanoi import resolver_torre_hanoi
from config import Config

def mostrar_menu():
    while True:
        print("== Problema de la Torre de Hanoi ==")
        print("1. Resolver con valores por defecto")
        print("2. Resolver con valores personalizados")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            resolver_torre_hanoi(Config.num_discos, Config.torre_origen, Config.torre_destino, Config.torre_auxiliar)
        elif opcion == '2':
            n = int(input("Ingrese el número de discos: "))
            origen = input("Ingrese la torre de origen (A, B o C): ")
            destino = input("Ingrese la torre de destino (A, B o C): ")
            auxiliar = input("Ingrese la torre auxiliar (A, B o C): ")
            resolver_torre_hanoi(n, origen, destino, auxiliar)
        elif opcion == '3':
            break
        else:
            print("Opción inválida")

if __name__ == '__main__':
    mostrar_menu()
