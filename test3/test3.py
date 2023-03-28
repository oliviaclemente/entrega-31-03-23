import menu3

def test_ordena_naves():
    naves_ordenadas = menu.ordena_naves(menu.naves)
    assert naves_ordenadas[0]["nombre"] == "A-wing"
    assert naves_ordenadas[-1]["nombre"] == "Estrella de la Muerte"
    assert naves_ordenadas[0]["largo"] == 9.6
    assert naves_ordenadas[-1]["largo"] == 160.0

def test_info_naves():
    halcon_milenario = menu.info_nave("Halcón Milenario")
    estrella_muerte = menu.info_nave("Estrella de la Muerte")
    assert halcon_milenario["tripulacion"] == 4
    assert estrella_muerte["pasajeros"] == 843342

def test_naves_mas_pasajeros():
    naves_mas_pasajeros = menu.naves_mas_pasajeros(menu.naves, 5)
    assert len(naves_mas_pasajeros) == 5
    assert naves_mas_pasajeros[0]["nombre"] == "Estrella de la Muerte"

def test_nave_max_tripulacion():
    nave_max_tripulacion = menu.nave_max_tripulacion(menu.naves)
    assert nave_max_tripulacion["nombre"] == "Estrella de la Muerte"

def test_naves_AT():
    naves_AT = menu.naves_AT(menu.naves)
    assert len(naves_AT) == 2
    assert naves_AT[0]["nombre"] == "AT-AT"

def test_info_naves_extremas():
    nave_mas_pequena = menu.info_nave_extrema(menu.naves, "pequena")
    nave_mas_grande = menu.info_nave_extrema(menu.naves, "grande")
    assert nave_mas_pequena["nombre"] == "TIE Fighter"
    assert nave_mas_grande["nombre"] == "Estrella de la Muerte"

if __name__ == "__main__":
    test_ordena_naves()
    test_info_naves()
    test_naves_mas_pasajeros()
    test_nave_max_tripulacion()
    test_naves_AT()
    test_info_naves_extremas()
    print("Todos los tests pasaron.")
