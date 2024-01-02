import os
import categorias as categoria

isIncorrect = True

def verificarEdad() -> int:
    global isIncorrect
    isIncorrect = True
    while(isIncorrect):
        try:
            edad = int(input(f"Ingrese la edad del jugador : "))
        except ValueError:
            print(f"Ingrese un dato válido")
        else:
            isIncorrect = False
    return edad

def regJugador(categoriaJugador : int, edadJugador : int) -> dict:
    id = ""
    nombre = ""
    while (id == ""):
        id = input(f"Ingrese el código del jugador : ")
    while (nombre == ""):
        nombre = input(f"Ingrese el nombre del jugador : ")
    categoriaJ = categoria.defCategoria(categoriaJugador)
    jugador = {
        "Id" : id,
        "Nombre" : nombre,
        "Edad" : edadJugador,
        "Categoria" : categoriaJ,
        "PJ" : 0,
        "PG" : 0,
        "PP" : 0,
        "PA" : 0,
        "TP" : 0
    }
    return {id : jugador}

def buscarJugador(codJugador : str, jugadores : dict) -> str:
    data = jugadores.get(codJugador, -1)
    if (type(data) == dict):
        codigo = data.get("Id")
        return codigo
    else:
        print(f"No se encontró el jugador con el código {codJugador}")
        os.system("pause")

def actualizarJugador(codJugador: str, jugadores : dict, puntosA : int, partidosG : int, partidosP : int, totalP : int):
    data = jugadores.get(codJugador, -1)
    PJ = data.get("PJ") + 1
    PG = data.get("PG") + partidosG
    PP = data.get("PP") + partidosP
    PA = data.get("PA") + puntosA
    TP = data.get("TP") + totalP
    data.update({"PJ" : PJ})
    data.update({"PG" : PG})
    data.update({"PP" : PP})
    data.update({"PA" : PA})
    data.update({"TP" : TP})
    # print(data)