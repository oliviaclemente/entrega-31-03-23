def torre_hanoi(numero_discos, torre_origen, torre_destino, torre_auxiliar):
    if numero_discos == 1:
        print(f"Mover disco 1 de la torre {torre_origen} a la torre {torre_destino}")
        return
    torre_hanoi(numero_discos - 1, torre_origen, torre_auxiliar, torre_destino)
    print(f"Mover disco {numero_discos} de la torre {torre_origen} a la torre {torre_destino}")
    torre_hanoi(numero_discos - 1, torre_auxiliar, torre_destino, torre_origen)

# Ejemplo de uso:
torre_hanoi(3, "A", "C", "B")
