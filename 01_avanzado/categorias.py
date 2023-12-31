def defCategoria(categoriaJ : int) -> str:
    categoria = ""
    if (categoriaJ == 1):
        categoria = "Novato"
    elif (categoriaJ == 2):
        categoria = "Intermedio"
    elif (categoriaJ == 3):
        categoria = "Avanzado"
    return categoria