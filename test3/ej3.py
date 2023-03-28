# Crear una lista de diccionarios con información de las naves
naves = [
    {"nombre": "Halcón Milenario", "largo": 34.75, "tripulación": 4, "pasajeros": 6},
    {"nombre": "Estrella de la Muerte", "largo": 120000, "tripulación": 342953, "pasajeros": 843342},
    {"nombre": "AT-AT", "largo": 20, "tripulación": 5, "pasajeros": 40},
    {"nombre": "AT-ST", "largo": 8.6, "tripulación": 2, "pasajeros": 0},
    {"nombre": "X-wing", "largo": 12.5, "tripulación": 1, "pasajeros": 0},
    {"nombre": "TIE fighter", "largo": 6.4, "tripulación": 1, "pasajeros": 0},
    {"nombre": "Nave Corelliana", "largo": 30, "tripulación": 3, "pasajeros": 8},
    {"nombre": "Transporte de Asalto Imperial", "largo": 20, "tripulación": 6, "pasajeros": 20},
]

# Listado ordenado por nombre ascendente y largo descendente
naves_ordenadas = sorted(naves, key=lambda n: (n["nombre"], -n["largo"]))

# Mostrar información del Halcón Milenario y la Estrella de la Muerte
halcon_milenario = next(n for n in naves if n["nombre"] == "Halcón Milenario")
estrella_muerte = next(n for n in naves if n["nombre"] == "Estrella de la Muerte")
print(halcon_milenario)
print(estrella_muerte)

# Las cinco naves con mayor cantidad de pasajeros
naves_pasajeros = sorted(naves, key=lambda n: -n["pasajeros"])[:5]
for n in naves_pasajeros:
    print(n)

# Nave que requiere mayor cantidad de tripulación
nave_max_tripulacion = max(naves, key=lambda n: n["tripulación"])
print(nave_max_tripulacion)

# Naves que comienzan con AT
naves_AT = [n for n in naves if n["nombre"].startswith("AT")]
for n in naves_AT:
    print(n)

# Naves que pueden llevar seis o más pasajeros
naves_pasajeros_minimo = [n for n in naves if n["pasajeros"] >= 6]
for n in naves_pasajeros_minimo:
    print(n)

# Información de la nave más pequeña y la más grande
nave_mas_pequeña = min(naves, key=lambda n: n["largo"])
nave_mas_grande = max(naves, key=lambda n: n["largo"])
print(nave_mas_pequeña)
print(nave_mas_grande)
