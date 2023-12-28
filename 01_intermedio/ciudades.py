sismos = []
indice = -1
promedio = 0
riesgo = ""
isIncorrect = True

def regCiudad() -> list:
    global isIncorrect
    isIncorrect = True
    while (isIncorrect):
        try:
            ciudad = input(f"Ingrese el nombre de la ciudad : ")
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
            print(f"REGISTRO ACTUAL DE SISMOS")
            print(f"Ciudad: {sismos[indice][0]}")
            print(f"Sismos: {sismos[indice][1]}")
    if (indice == -1):
        print(f"No se encontró la ciudad")
    return indice