import os
import categorias as categoria

def regJugador(categoriaJugador : int, edadJugador : int) -> dict:
    id = input(f"Ingrese el código del jugador : ")
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

def buscarJugador():
    return 0