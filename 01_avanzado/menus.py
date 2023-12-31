import os
import jugadores as jugador

jugadores = {}
menuP = "1. Registrar Jugador\n2. Registrar Partido\n3. Tabla de puntajes\n4. Ganador de cada categoría\n5. Salir"
menuRegJ = "1. Novato\n2. Intermedio\n3. Avanzado\n4. Volver"
hasError = True

def menuPrincipal() -> int:
    global hasError
    hasError = True
    print(menuP)
    while (hasError):
        try:
            return int(input(f"Ingrese una opción : "))
        except ValueError:
            hasError = True

def menuRegistroJ():
    os.system("pause")
    os.system("cls")
    isActive = True
    while (isActive):
        try:
            print(menuRegJ)
            opMenu = int(input(f"Ingrese una opción : "))
        except ValueError:
            print(f"Ingrese una opción válida")
        else:
            if (opMenu == 1):
                jugadores.update(jugador.regJugador())
            elif (opMenu == 2):
                pass
            elif (opMenu == 3):
                pass
            elif (opMenu == 4):
                isActive = False
    print(jugadores)