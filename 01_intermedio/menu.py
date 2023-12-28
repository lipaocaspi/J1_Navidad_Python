menuP = "1. Registrar Ciudad\n2. Registrar Sismo\n3. Buscar sismos por ciudad\n4. Informe de riesgo\n5. Salir"

def menuShow() -> int:
    global hasError
    hasError = True
    print(menuP)
    while (hasError):
        try:
            return int(input(f"Ingrese una opción : "))
        except ValueError:
            hasError = True