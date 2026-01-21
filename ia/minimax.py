from juego.constantes import IA, HUMANO, EMPATE, VACIO
from juego.tablero import movimientos_disponibles
from juego.reglas import comprobar_ganador


def minimax(tablero, es_maximizando):
    resultado = comprobar_ganador(tablero)

    if resultado == IA:
        return 1
    elif resultado == HUMANO:
        return -1
    elif resultado == EMPATE:
        return 0

    if es_maximizando:
        mejor_puntuacion = -float("inf")
        for movimiento in movimientos_disponibles(tablero):
            tablero[movimiento] = IA
            puntuacion = minimax(tablero, False)
            tablero[movimiento] = VACIO
            mejor_puntuacion = max(mejor_puntuacion, puntuacion)
        return mejor_puntuacion
    else:
        mejor_puntuacion = float("inf")
        for movimiento in movimientos_disponibles(tablero):
            tablero[movimiento] = HUMANO
            puntuacion = minimax(tablero, True)
            tablero[movimiento] = VACIO
            mejor_puntuacion = min(mejor_puntuacion, puntuacion)
        return mejor_puntuacion


def mejor_movimiento(tablero):
    mejor_puntuacion = -float("inf")
    movimiento = None

    for i in movimientos_disponibles(tablero):
        tablero[i] = IA
        puntuacion = minimax(tablero, False)
        tablero[i] = VACIO
        if puntuacion > mejor_puntuacion:
            mejor_puntuacion = puntuacion
            movimiento = i

    return movimiento
