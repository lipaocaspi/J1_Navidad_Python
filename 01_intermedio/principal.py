import os
import menu
import sismos as sismo
import ciudades as ciudad

isActive = True
opMenu = 0
headerS = """
***********************************************
REGISTRO DE SISMOS POR CIUDAD
***********************************************
"""
headerB = """
***********************************************
BÚSQUEDA DE SISMOS POR CIUDAD
***********************************************
"""

while (isActive):
    os.system("cls")
    try:
        opMenu = menu.menuShow()
        print(f"")
    except ValueError:
        print(f"Error en el dato de ingreso")
    else:
        if (opMenu == 1):
            rta = "S"
            while (rta in ["S", "s"]):
                os.system("cls")
                if (len(ciudad.sismos) < 5):
                    ciudad.regCiudad()
                    rta = input(f"¿Desea registrar otra ciudad? S(Sí) o Enter(No) ")
                else:
                    rta = "N"
                    print(f"No es posible registrar más ciudades")
                print(f"")
        elif (opMenu == 2):
            os.system("cls")
            print(headerS)
            nombre = input(f"Ingrese el nombre de la ciudad correspondiente al sismo que desea registrar : ").upper()
            ciudad.buscarCiudad(nombre)
            if (ciudad.indice >= 0):
                rta = "S"
                while (rta in ["S", "s"]):
                    sismo.regSismo(ciudad.indice)
                    rta = input(f"¿Desea registrar otro sismo? S(Sí) o Enter(No) ")
        elif (opMenu == 3):
            os.system("cls")
            print(headerB)
            nombre = input(f"Ingrese el nombre de la ciudad que desea buscar : ").upper()
            ciudad.buscarCiudad(nombre)
        elif (opMenu == 4):
            os.system("cls")
            sismo.reporte()
        elif (opMenu == 5):
            isActive = False
            print(f"GRACIAS POR USAR NUESTRO SERVICIO")
            print(f"")
        else:
            print(f"La opción ingresada es inválida")
            print(f"")
        os.system("pause")