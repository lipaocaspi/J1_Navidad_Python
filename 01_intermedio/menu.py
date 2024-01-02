menuP = "1. Registrar Ciudad\n2. Registrar Sismo\n3. Buscar sismos por ciudad\n4. Informe de riesgo\n5. Salir"
header = """
***********************************************
REGISTRO DE SISMOS
***********************************************
"""

def menuShow() -> int:
    global hasError
    hasError = True
    print(header)
    print(menuP)
    while (hasError):
        try:
            print(f"")
            return int(input(f"Ingrese una opción : "))
        except ValueError:
            hasError = True