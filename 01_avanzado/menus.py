import os
import jugadores as jugador
import partidos as partido

jugadoresNovatos = {}
jugadoresIntermedios = {}
jugadoresAvanzados = {}
menuP = "1. Registrar Jugador\n2. Registrar Partido\n3. Tabla de puntajes\n4. Ganador de cada categoría\n5. Salir"
menuRegJ = "1. Novato (15-16 años)\n2. Intermedio (17-20 años)\n3. Avanzado (Mayor de 20 años)\n4. Volver"
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
        os.system("cls")
        try:
            print(menuRegJ)
            opMenu = int(input(f"Ingrese una opción : "))
        except ValueError:
            print(f"Ingrese una opción válida")
        else:
            if (opMenu == 1):
                edad = int(input(f"Ingrese la edad del jugador : "))
                if (edad >= 15 and edad <= 16):
                    jugadoresNovatos.update(jugador.regJugador(opMenu, edad))
                else:
                    print(f"La edad no corresponde a la categoría seleccionada")
            elif (opMenu == 2):
                edad = int(input(f"Ingrese la edad del jugador : "))
                if (edad >= 17 and edad <= 20):
                    jugadoresIntermedios.update(jugador.regJugador(opMenu, edad))
                else:
                    print(f"La edad no corresponde a la categoría seleccionada")
            elif (opMenu == 3):
                edad = int(input(f"Ingrese la edad del jugador : "))
                if (edad > 20):
                    jugadoresAvanzados.update(jugador.regJugador(opMenu, edad))
                else:
                    print(f"La edad no corresponde a la categoría seleccionada")
            elif (opMenu == 4):
                isActive = False
            os.system("pause")

def menuRegistroP():
    os.system("pause")
    os.system("cls")
    isActive = True
    while (isActive):
        os.system("cls")
        try:
            print(menuRegJ)
            opMenu = int(input(f"Ingrese una opción : "))
        except ValueError:
            print(f"Ingrese una opción válida")
        else:
            if (opMenu == 1):
                isIncorrect = True
                if (len(jugadoresNovatos) < 5):
                    print(f"Deben haber mínimo 5 jugadores inscritos para iniciar los juegos")
                else:
                    partido.regPartidos()
            elif (opMenu == 2):
                if (len(jugadoresIntermedios) < 5):
                    print(f"Deben haber mínimo 5 jugadores inscritos para iniciar los juegos")
                else:
                    partido.regPartidos()
            elif (opMenu == 3):
                if (len(jugadoresAvanzados) < 5):
                    print(f"Deben haber mínimo 5 jugadores inscritos para iniciar los juegos")
                else:
                    partido.regPartidos()
            elif (opMenu == 4):
                isActive = False
            os.system("pause")