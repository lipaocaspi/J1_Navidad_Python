import os
import dependencias

menu = "1. Registrar Dependencia\n2. Registrar Consumo por Dependencia\n3. Ver CO2 Producido\n4. Dependencia que produce mayor CO2\n5. Salir"
subMenuDependencias = "1. Dispositivos\n2. Transporte\n3. Regresar al menu principal"

def menuPrincipal() -> int:
    global hasError
    hasError = True
    print(menu)
    while (hasError):
        try:
            return int(input("Ingrese una opción : "))
        except ValueError:
            hasError = True

def menuDependencia():
    os.system("cls")
    header = """
    *************************************************
    *   MENU REGISTRO DE CONSUMO POR DEPENDENCIA    *
    *************************************************
    """
    isActiveMenu = True
    isIncorrect = True
    while (isActiveMenu):
        os.system("cls")
        print(header)
        try:
            print(subMenuDependencias)
            opMenu = int(input("Ingrese una opción : "))
        except ValueError:
            print("Opción inválida")
        else:
            if(opMenu == 1):
                isIncorrect = True
                while (isIncorrect):
                    os.system("cls")
                    try:
                        codigo = int(input(f"Ingrese el código de la dependencia cuyos datos va a registrar : "))
                    except ValueError:
                        print(f"Error en el dato de ingreso")
                    else:
                        dependencias.buscarDependencia(codigo)
                        if (dependencias.indice == -1):
                            print(f"No se encontró dependencia")
                            os.system("pause")
                        else:
                            rta = "S"
                            while (rta in ["S", "s"]):
                                dependencias.regConsumoDispositivos(dependencias.indice)
                                rta = input(f"¿Desea registrar otro dispositivo? : ")
                            os.system("pause")
                        isIncorrect = False
            elif(opMenu == 2):
                isIncorrect = True
                while (isIncorrect):
                    os.system("cls")
                    try:
                        codigo = int(input(f"Ingrese el código de la dependencia cuyos datos va a registrar : "))
                    except ValueError:
                        print(f"Error en el dato de ingreso")
                    else:
                        dependencias.buscarDependencia(codigo)
                        if (dependencias.indice == -1):
                            print(f"No se encontró dependencia")
                            os.system("pause")
                        else:
                            rta = "S"
                            while (rta in ["S", "s"]):
                                dependencias.regConsumoTransporte(dependencias.indice)
                                rta = input(f"¿Desea registrar otro transporte? : ")
                            os.system("pause")
                        isIncorrect = False
            elif(opMenu == 3):
                isActiveMenu = False
            else:
                print("La opción ingresada es inválida")