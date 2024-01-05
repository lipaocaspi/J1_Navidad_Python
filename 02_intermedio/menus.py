import os
import dependencias

menu = "1. Registrar Dependencia\n2. Registrar Consumo por Dependencia\n3. Ver CO2 Producido\n4. Dependencia que produce mayor CO2\n5. Salir"
subMenuDependencias = "1. Dispositivos\n2. Transporte\n3. Regresar al menu principal"

def menuPrincipal() -> int:
    global hasError
    hasError = True
    headerP = """
    **************************************************
    *           CÁLCULO DE CO2 PRODUCIDO             *
    **************************************************
    """
    print(headerP)
    print(menu)
    while (hasError):
        try:
            print(f"")
            return int(input(f"Ingrese una opción : "))
        except ValueError:
            hasError = True

def menuDependencia():
    os.system("cls")
    headerD = """
    *************************************************
    *   MENU REGISTRO DE CONSUMO POR DEPENDENCIA    *
    *************************************************
    """
    headerCD = """
    ********************************
    * REGISTRO CONSUMO DISPOSITIVO *
    ********************************
    """
    headerCT = """
    *******************************
    * REGISTRO CONSUMO TRANSPORTE *
    *******************************
    """
    isActiveMenu = True
    isIncorrect = True
    while (isActiveMenu):
        os.system("cls")
        print(headerD)
        try:
            print(subMenuDependencias)
            print(f"")
            opMenu = int(input(f"Ingrese una opción : "))
        except ValueError:
            print(f"Opción inválida")
        else:
            if(opMenu == 1):
                isIncorrect = True
                os.system("cls")
                print(headerCD)
                while (isIncorrect):
                    codigo = input(f"Ingrese el código de la dependencia cuyos datos va a registrar : ")
                    dependencias.buscarDependencia(codigo)
                    if (dependencias.indice == -1):
                        print(f"No se encontró dependencia")
                        print(f"")
                        os.system("pause")
                    else:
                        rta = "S"
                        while (rta in ["S", "s"]):
                            dependencias.regConsumoDispositivos(dependencias.indice)
                            rta = input(f"¿Desea registrar otro dispositivo? S(Sí) o Enter(No) : ")
                        print(f"")
                        isIncorrect = False
                    os.system("pause")
                print(f"")
            elif(opMenu == 2):
                isIncorrect = True
                os.system("cls")
                print(headerCT)
                while (isIncorrect):
                    codigo = input(f"Ingrese el código de la dependencia cuyos datos va a registrar : ")
                    dependencias.buscarDependencia(codigo)
                    if (dependencias.indice == -1):
                        print(f"No se encontró dependencia")
                        print(f"")
                        os.system("pause")
                    else:
                        rta = "S"
                        while (rta in ["S", "s"]):
                            dependencias.regConsumoTransporte(dependencias.indice)
                            rta = input(f"¿Desea registrar otro transporte? S(Sí) o Enter(No) : ")
                        print(f"")  
                        isIncorrect = False  
                    os.system("pause")
            elif(opMenu == 3):
                isActiveMenu = False
            else:
                print(f"La opción ingresada es inválida")