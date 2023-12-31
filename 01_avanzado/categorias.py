def defCategoria(edadJugador : int) -> str:
    categoria = ""
    if (edadJugador >= 15 and edadJugador <= 16):
        categoria = "Novato"
    elif (edadJugador >= 17 and edadJugador <= 20):
        categoria = "Intermedio"
    elif (edadJugador > 20):
        categoria = "Avanzado"
    return categoria