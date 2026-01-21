from juego.tablero import nuevo_tablero, movimientos_disponibles
from ia.minimax import mejor_movimiento
from juego.constantes import IA, HUMANO
from juego.reglas import comprobar_ganador


def imprimir_bonito(tablero):
    print(f" {tablero[0]} | {tablero[1]} | {tablero[2]} ")
    print("---+---+---")
    print(f" {tablero[3]} | {tablero[4]} | {tablero[5]} ")
    print("---+---+---")
    print(f" {tablero[6]} | {tablero[7]} | {tablero[8]} ")
    print()


def main():
    tablero = nuevo_tablero()
    print("¡Bienvenido al tres en raya de Ismerai!  Tú eres 'O' y la IA es 'X'.")
    print("Introduce el número de la casilla (0-8) para jugar.")

    turno_humano = (
        True  # False y la IA empieza primera, True y el jugador empieza primero
    )

    while True:
        imprimir_bonito(tablero)

        resultado = comprobar_ganador(tablero)
        if resultado:
            print(f"Juego terminado. Resultado: {resultado}")
            break

        if turno_humano:
            try:
                entrada = input("Tu turno (0-8): ")
                mov = int(entrada)
                if mov in movimientos_disponibles(tablero):
                    tablero[mov] = HUMANO
                    turno_humano = False
                else:
                    print("Movimiento inválido o casilla ocupada.")
            except ValueError:
                print("Por favor, introduce un número válido.")
        else:
            print("La IA está pensando...")
            mov = mejor_movimiento(tablero)
            tablero[mov] = IA
            turno_humano = True


if __name__ == "__main__":
    main()
