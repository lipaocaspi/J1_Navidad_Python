import os
import categorias as categoria
import menus as menu

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

def buscarId(codJugador : str, jugadores : dict) -> str:
    data = jugadores.get(codJugador, -1)
    if (type(data) == dict):
        codigo = data.get("Id")
        return codigo

def regJugador(categoriaJugador : int, edadJugador : int, jugadores : dict) -> dict:
    id = ""
    nombre = ""
    while (id == ""):
        id = input(f"Ingrese el código del jugador : ")
        idEncontrado = buscarId(id, jugadores)
        if (type(idEncontrado) == str):
            print(f"Ya existe un jugador con ese código")
            id = ""
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
    print(data)

def mostrarTabla(jugadores : dict):
    print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format("ID", "JUGADOR", "PJ", "PG", "PP", "PA", "TP"))
    for item in jugadores:
        print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(jugadores[item]["Id"], jugadores[item]["Nombre"], jugadores[item]["PJ"], jugadores[item]["PG"], jugadores[item]["PP"], jugadores[item]["PA"], jugadores[item]["TP"]))
    print(f"")
    os.system("pause")