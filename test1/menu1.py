def torre_hanoi(numero_discos, torre_origen, torre_destino, torre_auxiliar):
    if numero_discos == 1:
        print(f"Mover disco 1 de la torre {torre_origen} a la torre {torre_destino}")
        return
    torre_hanoi(numero_discos - 1, torre_origen, torre_auxiliar, torre_destino)
    print(f"Mover disco {numero_discos} de la torre {torre_origen} a la torre {torre_destino}")
    torre_hanoi(numero_discos - 1, torre_auxiliar, torre_destino, torre_origen)


from torre_hanoi import resolver_torre_hanoi

def mostrar_menu():
    while True:
        print("== Problema de la Torre de Hanoi ==")
        print("1. Resolver con valores por defecto")
        print("2. Resolver con valores personalizados")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            resolver_torre_hanoi()
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
