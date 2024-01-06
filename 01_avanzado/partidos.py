import math
import menus as menu
import jugadores as jugador

partidosNovatos = {}
partidosIntermedios = {}
partidosAvanzados = {}
isIncorrect = True
    
def verificarTipo(valorDato, nombreDato, tipoDato):
    global isIncorrect
    isIncorrect = True
    valorDato = 0
    while (isIncorrect):
        try:
            valorDato = tipoDato(input(f"{nombreDato}"))
        except ValueError:
            print(f"Ingrese un dato correcto")
        else:
            isIncorrect = False
            return valorDato
        
def verificarPartido(id1 : str, id2 : str, partidos : dict) -> int:
    for item in partidos:
        if (((id1 == partidos[item]["cont1"]) or (id1 == partidos[item]["cont2"])) and ((id2 == partidos[item]["cont1"]) or (id2 == partidos[item]["cont2"]))):
            print(f"Este partido ya está registrado")
            return 0

def regPartidos(categoria: int) -> dict:
    id1 = None
    id2 = None
    contador = 0
    if (categoria == 1):
        contador = contador + len(partidosNovatos)
        while (type(id1) != str):
            idJ1 = input(f"Ingrese el código del jugador 1 : ")
            id1 = jugador.buscarJugador(idJ1, menu.jugadoresNovatos)
        while (type(id2) != str or id2 == id1):
            idJ2 = input(f"Ingrese el código del jugador 2 : ")
            id2 = jugador.buscarJugador(idJ2, menu.jugadoresNovatos)
        verificacion = verificarPartido(id1, id2, partidosNovatos)
    elif (categoria == 2):
        contador = contador + len(partidosIntermedios)
        while (type(id1) != str):
            idJ1 = input(f"Ingrese el código del jugador 1 : ")
            id1 = jugador.buscarJugador(idJ1, menu.jugadoresIntermedios)
        while (type(id2) != str or id2 == id1):
            idJ2 = input(f"Ingrese el código del jugador 2 : ")
            id2 = jugador.buscarJugador(idJ2, menu.jugadoresIntermedios)
        verificacion = verificarPartido(id1, id2, partidosIntermedios)
    elif (categoria == 3):
        contador = contador + len(partidosAvanzados)
        while (type(id1) != str):
            idJ1 = input(f"Ingrese el código del jugador 1 : ")
            id1 = jugador.buscarJugador(idJ1, menu.jugadoresAvanzados)
        while (type(id2) != str or id2 == id1):
            idJ2 = input(f"Ingrese el código del jugador 2 : ")
            id2 = jugador.buscarJugador(idJ2, menu.jugadoresAvanzados)
        verificacion = verificarPartido(id1, id2, partidosAvanzados)
    
    if (verificacion == 0):
        return
    else:
        valor = 0
        print(f"INGRESE LOS RESULTADOS DE CADA SET")
        print(F"SET 1")
        set1J1 = verificarTipo(valor, "Puntos jugador 1 : ", int)
        set1J2 = verificarTipo(valor, "Puntos jugador 2 : ", int)
        print(F"SET 2")
        set2J1 = verificarTipo(valor, "Puntos jugador 1 : ", int)
        set2J2 = verificarTipo(valor, "Puntos jugador 2 : ", int)
        print(F"SET 3")
        set3J1 = verificarTipo(valor, "Puntos jugador 1 : ", int)
        set3J2 = verificarTipo(valor, "Puntos jugador 2 : ", int)

        puntosJ1S1 = set1J1 - set1J2
        puntosJ2S1 = set1J2 - set1J1
        puntosJ1S2 = set2J1 - set2J2
        puntosJ2S2 = set2J2 - set2J1
        puntosJ1S3 = set3J1 - set3J2
        puntosJ2S3 = set3J2 - set3J1

        if ((puntosJ1S1 > 0 and puntosJ1S2 > 0 and puntosJ1S3 > 0) or (puntosJ1S1 > 0 and puntosJ1S2 > 0) or (puntosJ1S1 > 0 and puntosJ1S3 > 0) or (puntosJ1S2 > 0 and puntosJ1S3 > 0)):
            ganador = id1
            PA1 = puntosJ1S1 + puntosJ1S2 + puntosJ1S3
            PA2 = 0
            PG1 = 1
            PP1 = 0
            TP1 = 2
            PG2 = 0
            PP2 = 1
            TP2 = 0
            if (categoria == 1):
                jugador.actualizarJugador(ganador, menu.jugadoresNovatos, PA1, PG1, PP1, TP1)
                jugador.actualizarJugador(id2, menu.jugadoresNovatos, PA2, PG2, PP2, TP2)
            elif (categoria == 2):
                jugador.actualizarJugador(ganador, menu.jugadoresIntermedios, PA1, PG1, PP1, TP1)
                jugador.actualizarJugador(id2, menu.jugadoresIntermedios, PA2, PG2, PP2, TP2)
            elif (categoria == 3):
                jugador.actualizarJugador(ganador, menu.jugadoresAvanzados, PA1, PG1, PP1, TP1)
                jugador.actualizarJugador(id2, menu.jugadoresAvanzados, PA2, PG2, PP2, TP2)
        else:
            ganador = id2
            PA1 = 0
            PA2 = puntosJ2S1 + puntosJ2S2 + puntosJ2S3
            PG2 = 1
            PP2 = 0
            TP2 = 2
            PG1 = 0
            PP1 = 1
            TP1 = 0
            if (categoria == 1):
                jugador.actualizarJugador(ganador, menu.jugadoresNovatos, PA2, PG2, PP2, TP2)
                jugador.actualizarJugador(id1, menu.jugadoresNovatos, PA1, PG1, PP1, TP1)
            elif (categoria == 2):
                jugador.actualizarJugador(ganador, menu.jugadoresIntermedios, PA2, PG2, PP2, TP2)
                jugador.actualizarJugador(id1, menu.jugadoresIntermedios, PA1, PG1, PP1, TP1)
            elif (categoria == 3):
                jugador.actualizarJugador(ganador, menu.jugadoresAvanzados, PA2, PG2, PP2, TP2)
                jugador.actualizarJugador(id1, menu.jugadoresAvanzados, PA1, PG1, PP1, TP1)

        partido = {
            "id": str(contador),
            "cont1": id1,
            "cont2": id2,
            "sets": {
                "1": [set1J1, set1J2],
                "2": [set2J1, set2J2],
                "3": [set3J1, set3J2]
            },
            "ganador": ganador
        }

        return {contador : partido}

def calNumPartidos(numJugadores : int) -> float:
    jugadoresPorPartido = 2
    numerador = math.factorial(numJugadores)
    denominador = (math.factorial(jugadoresPorPartido)) * (math.factorial(numJugadores - jugadoresPorPartido))
    numPartidos = numerador / denominador
    return numPartidos