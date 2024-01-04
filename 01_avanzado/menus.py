import os
import jugadores as jugador
import partidos as partido

jugadoresNovatos = {}
jugadoresIntermedios = {}
jugadoresAvanzados = {}
menuP = "1. Registrar Jugador\n2. Registrar Partido\n3. Tabla de puntajes\n4. Ganador de cada categoría\n5. Salir"
menuRegJ = "1. Novato (15-16 años)\n2. Intermedio (17-20 años)\n3. Avanzado (Mayor de 20 años)\n4. Volver"
headerP = """
***********************************************
BIENVENIDO AL TORNEO DE TENIS DE MESA DE CAMPUS
***********************************************
"""
headerRJ = """
***********************************************
REGISTRO DE JUGADORES
***********************************************
"""
headerRP = """
***********************************************
REGISTRO DE PARTIDOS
***********************************************
"""
headerTablas = """
***********************************************
TABLA DE PUNTAJES
***********************************************
"""
headerGanadores = """
***********************************************
GANADORES POR CATEGORÍA
***********************************************
"""
hasError = True

def menuPrincipal() -> int:
    global hasError
    hasError = True
    print(headerP)
    print(menuP)
    while (hasError):
        try:
            print(f"")
            return int(input(f"Ingrese una opción : "))
        except ValueError:
            print(f"Ingrese un dato válido")
            hasError = True

def menuRegistroJ():
    os.system("pause")
    os.system("cls")
    isActive = True
    while (isActive):
        os.system("cls")
        try:
            print(headerRJ)
            print(menuRegJ)
            print(f"")
            opMenu = int(input(f"Ingrese una opción : "))
            print(f"")
        except ValueError:
            print(f"Ingrese una opción válida")
        else:
            if (opMenu == 1):
                if (len(partido.partidosNovatos) > 0):
                    print(f"El torneo ya comenzó, no se pueden registrar más participantes")
                else:
                    edad = jugador.verificarEdad()
                    if (edad >= 15 and edad <= 16):
                        jugadoresNovatos.update(jugador.regJugador(opMenu, edad, jugadoresNovatos))
                    else:
                        print(f"La edad no corresponde a la categoría seleccionada")
            elif (opMenu == 2):
                if (len(partido.partidosIntermedios) > 0):
                    print(f"El torneo ya comenzó, no se pueden registrar más participantes")
                else:
                    edad = jugador.verificarEdad()
                    if (edad >= 17 and edad <= 20):
                        jugadoresIntermedios.update(jugador.regJugador(opMenu, edad, jugadoresIntermedios))
                    else:
                        print(f"La edad no corresponde a la categoría seleccionada")
            elif (opMenu == 3):
                if (len(partido.partidosAvanzados) > 0):
                    print(f"El torneo ya comenzó, no se pueden registrar más participantes")
                else:
                    edad = jugador.verificarEdad()
                    if (edad > 20):
                        jugadoresAvanzados.update(jugador.regJugador(opMenu, edad, jugadoresAvanzados))
                    else:
                        print(f"La edad no corresponde a la categoría seleccionada")
            elif (opMenu == 4):
                isActive = False
            else:
                print(f"La opción ingresada es inválida")
            os.system("pause")
            
def menuRegistroP():
    os.system("pause")
    os.system("cls")
    isActive = True
    while (isActive):
        os.system("cls")
        try:
            print(headerRP)
            print(menuRegJ)
            print(f"")
            opMenu = int(input(f"Ingrese una opción : "))
            print(f"")
        except ValueError:
            print(f"Ingrese una opción válida")
        else:
            if (opMenu == 1):
                if (len(jugadoresNovatos) < 5):
                    print(f"Deben haber mínimo 5 jugadores inscritos para iniciar los juegos")
                else:
                    partidoR = partido.regPartidos(opMenu)
                    if (type(partidoR) != dict):
                        print(f"No se puede registrar un mismo partido 2 veces")
                    else:
                        partido.partidosNovatos.update(partidoR)
            elif (opMenu == 2):
                if (len(jugadoresIntermedios) < 5):
                    print(f"Deben haber mínimo 5 jugadores inscritos para iniciar los juegos")
                else:
                    partidoR = partido.regPartidos(opMenu)
                    if (type(partidoR) != dict):
                        print(f"No se puede registrar un mismo partido 2 veces")
                    else:
                        partido.partidosIntermedios.update(partidoR)
            elif (opMenu == 3):
                if (len(jugadoresAvanzados) < 5):
                    print(f"Deben haber mínimo 5 jugadores inscritos para iniciar los juegos")
                else:
                    partidoR = partido.regPartidos(opMenu)
                    if (type(partidoR) != dict):
                        print(f"No se puede registrar un mismo partido 2 veces")
                    else:
                        partido.partidosAvanzados.update(partidoR)
            elif (opMenu == 4):
                isActive = False
            else:
                print(f"La opción ingresada es inválida")
            os.system("pause")

def menuTablas():
    os.system("pause")
    os.system("cls")
    isActive = True
    while (isActive):
        os.system("cls")
        try:
            print(headerTablas)
            print(menuRegJ)
            print(f"")
            opMenu = int(input(f"Ingrese una opción : "))
            print(f"")
        except ValueError:
            print(f"Ingrese una opción válida")
        else:
            if (opMenu == 1):
                jugador.mostrarTabla(jugadoresNovatos)
            elif (opMenu == 2):
                jugador.mostrarTabla(jugadoresIntermedios)
            elif (opMenu == 3):
                jugador.mostrarTabla(jugadoresAvanzados)
            elif (opMenu == 4):
                isActive = False
            else:
                print(f"La opción ingresada es inválida")
            os.system("pause")

def menuGanadores():
    os.system("pause")
    os.system("cls")
    isActive = True
    while (isActive):
        os.system("cls")
        try:
            print(headerGanadores)
            print(menuRegJ)
            print(f"")
            opMenu = int(input(f"Ingrese una opción : "))
            print(f"")
        except ValueError:
            print(f"Ingrese una opción válida")
        else:
            if (opMenu == 1):
                if (len(jugadoresNovatos) < 5):
                    print(f"No se han registrado el mínimo de jugadores en esta categoría")
                else:
                    partidosRealizados = partido.calNumPartidos(len(jugadoresNovatos))
                    if (partidosRealizados == len(partido.partidosNovatos)):
                        print(f"GANADOR/A NOVATO/A")
                        jugador.mostrarGanador(jugadoresNovatos)
                    else:
                        print(f"El torneo no ha terminado")
            elif (opMenu == 2):
                if (len(jugadoresIntermedios) < 5):
                    print(f"No se han registrado el mínimo de jugadores en esta categoría")
                else:
                    partidosRealizados = partido.calNumPartidos(len(jugadoresIntermedios))
                    if (partidosRealizados == len(partido.partidosIntermedios)):
                        print(f"GANADOR/A INTERMDEDIO/A")
                        jugador.mostrarGanador(jugadoresIntermedios)
                    else:
                        print(f"El torneo no ha terminado")
            elif (opMenu == 3):
                if (len(jugadoresAvanzados) < 5):
                    print(f"No se han registrado el mínimo de jugadores en esta categoría")
                else:
                    partidosRealizados = partido.calNumPartidos(len(jugadoresAvanzados))
                    if (partidosRealizados == len(partido.partidosAvanzados)):
                        print(f"GANADOR/A AVANZADO/A")
                        jugador.mostrarGanador(jugadoresAvanzados)
                    else:
                        print(f"El torneo no ha terminado")
            elif (opMenu == 4):
                isActive = False
            else:
                print(f"La opción ingresada es inválida")
            os.system("pause")