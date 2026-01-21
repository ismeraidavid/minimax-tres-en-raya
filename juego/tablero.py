from juego.constantes import VACIO


def nuevo_tablero():
    return [VACIO] * 9


def movimientos_disponibles(tablero):
    return [i for i, celda in enumerate(tablero) if celda == VACIO]
