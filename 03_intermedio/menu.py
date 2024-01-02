menuP = "1. Registrar Productos\n2. Visualizar Productos\n3. Actualizar Stock\n4. Informe de Productos Críticos\n5. Ganancia Potencial\n6. Salir"

def menuShow() -> int:
    global hasError
    hasError = True
    print(menuP)
    while (hasError):
        try:
            print(f"")
            return int(input(f"Ingrese una opción : "))
        except ValueError:
            hasError = True