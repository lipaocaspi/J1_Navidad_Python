import os
import categorias as categoria

def regJugador() -> dict:
    id = input(f"Ingrese el código del jugador")
    nombre = input(f"Ingrese el nombre del jugador")
    edad = int(input(f"Ingrese la edad del jugador"))
    categoriaJ = categoria.defCategoria(edad)
    jugador = {
        "Id" : id,
        "Nombre" : nombre,
        "Edad" : edad,
        "Categoria" : categoriaJ,
        "PJ" : 0,
        "PG" : 0,
        "PP" : 0,
        "PA" : 0,
        "TP" : 0
    }
    return {id : jugador}