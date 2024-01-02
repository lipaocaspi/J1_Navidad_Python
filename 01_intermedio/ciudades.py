sismos = []
indice = -1
promedio = 0
riesgo = ""
isIncorrect = True
headerC = """
***********************************************
REGISTRO DE CIUDADES
***********************************************
"""

def regCiudad() -> list:
    global isIncorrect
    isIncorrect = True
    print(headerC)
    while (isIncorrect):
        try:
            ciudad = input(f"Ingrese el nombre de la ciudad : ").upper()
        except ValueError:
            print(f"Ingrese un dato correcto")
        else:
            registroCiudad = [ciudad, [], promedio, riesgo]
            sismos.append(registroCiudad)
            isIncorrect = False
    return sismos

def buscarCiudad(nombreCiudad : str) -> int:
    global indice
    for item in sismos:
        if nombreCiudad in item:
            indice = sismos.index(item)
            print(f"")
            print(f"REGISTRO ACTUAL DE SISMOS")
            print(f"")
            print(f"Ciudad: {sismos[indice][0]}")
            print(f"Sismos: {sismos[indice][1]}")
            print(f"")
    if (indice == -1):
        print(f"No se encontró la ciudad")
    return indice