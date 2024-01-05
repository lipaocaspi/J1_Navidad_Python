sismos = []
indice = -1
promedio = 0
riesgo = ""
isFound = True
headerC = """
***********************************************
*           REGISTRO DE CIUDADES              *
***********************************************
"""

def regCiudad() -> list:
    global isIncorrect, isFound
    isIncorrect = True
    isFound = True
    print(headerC)
    while (isFound):
        codigo = input(f"Ingrese el código de la ciudad : ")
        if (buscarId(codigo) != -1):
            print(f"El código ya se encuentra registrado")
        else:
            ciudad = input(f"Ingrese el nombre de la ciudad : ")
            registroCiudad = [codigo, ciudad, [], promedio, riesgo]
            sismos.append(registroCiudad)
            isFound = False
    return sismos

def buscarId(codigoCiudad : str) -> int:
    global indice
    indice = -1
    for i in range(len(sismos)):
        if (codigoCiudad == sismos[i][0]):
            indice = i
    return indice

def buscarCiudad(codigoCiudad : str) -> int:
    global indice
    indice = -1
    for i in range(len(sismos)):
        if (codigoCiudad == sismos[i][0]):
            indice = i
            print(f"")
            print(f"REGISTRO ACTUAL DE SISMOS")
            print(f"")
            print(f"Ciudad: {sismos[indice][1]}")
            print(f"Sismos: {sismos[indice][2]}")
            print(f"")
    if (indice == -1):
        print(f"No se encontró la ciudad")
    return indice