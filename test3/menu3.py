# Definir una lista de diccionarios para almacenar la información de las naves
naves = [
    {"nombre": "Halcón Milenario", "largo": 34.37, "tripulacion": 4, "pasajeros": 6},
    {"nombre": "Estrella de la Muerte", "largo": 160.0, "tripulacion": 342, "pasajeros": 843342},
    {"nombre": "X-wing", "largo": 12.5, "tripulacion": 1, "pasajeros": 0},
    {"nombre": "AT-AT", "largo": 20.0, "tripulacion": 5, "pasajeros": 40},
    {"nombre": "AT-ST", "largo": 8.6, "tripulacion": 2, "pasajeros": 0},
    {"nombre": "TIE Fighter", "largo": 6.4, "tripulacion": 1, "pasajeros": 0},
    {"nombre": "Slave I", "largo": 21.5, "tripulacion": 1, "pasajeros": 6},
    {"nombre": "Millennium Falcon", "largo": 26.7, "tripulacion": 4, "pasajeros": 75},
    {"nombre": "A-wing", "largo": 9.6, "tripulacion": 1, "pasajeros": 0},
    {"nombre": "Imperial Shuttle", "largo": 20.0, "tripulacion": 6, "pasajeros": 20},
    {"nombre": "B-wing", "largo": 16.9, "tripulacion": 1, "pasajeros": 0}
]

# Ordenar la lista de naves por nombre de manera ascendente y por largo de manera descendente
naves_ordenadas = sorted(naves, key=lambda x: (x["nombre"], -x["largo"]))

# Mostrar toda la información del “Halcón Milenario” y la “Estrella de la Muerte”
halcon_milenario = next((nave for nave in naves if nave["nombre"] == "Halcón Milenario"), None)
estrella_muerte = next((nave for nave in naves if nave["nombre"] == "Estrella de la Muerte"), None)
print(halcon_milenario)
print(estrella_muerte)

# Determinar cuáles son las cinco naves con mayor cantidad de pasajeros
naves_mas_pasajeros = sorted(naves, key=lambda x: -x["pasajeros"])[:5]
for nave in naves_mas_pasajeros:
    print(nave)

# Indicar cuál es la nave que requiere mayor cantidad de tripulación
nave_max_tripulacion = max(naves, key=lambda x: x["tripulacion"])
print(nave_max_tripulacion)

# Mostrar todas las naves que comienzan con AT
naves_AT = [nave for nave in naves if nave["nombre"].startswith("AT")]
for nave in naves_AT:
    print(nave)

