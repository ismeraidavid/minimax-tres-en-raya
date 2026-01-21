from juego.constantes import VACIO, EMPATE

COMBINACIONES_GANADORAS = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
]


def comprobar_ganador(tablero):
    for a, b, c in COMBINACIONES_GANADORAS:
        if tablero[a] == tablero[b] == tablero[c] != VACIO:
            return tablero[a]

    if VACIO not in tablero:
        return EMPATE

    return None
