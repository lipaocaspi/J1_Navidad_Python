import os
import menu
import sismos as sismo
import ciudades as ciudad

isActive = True
opMenu = 0

while (isActive):
    os.system("cls")
    try:
        opMenu = menu.menuShow()
    except ValueError:
        print(f"Error en el dato de ingreso")
    else:
        if (opMenu == 1):
            rta = "S"
            while (rta in ["S", "s"]):
                os.system("cls")
                if (len(ciudad.sismos) < 5):
                    ciudad.regCiudad()
                    rta = input(f"¿Desea registrar otra ciudad? ")
                else:
                    rta = "N"
                    print(f"No es posible registrar más ciudades")
        elif (opMenu == 2):
            os.system("cls")
            nombre = input(f"Ingrese el nombre de la ciudad correspondiente al sismo que desea registrar : ")
            ciudad.buscarCiudad(nombre)
            if (ciudad.indice >= 0):
                rta = "S"
                while (rta in ["S", "s"]):
                    sismo.regSismo(ciudad.indice)
                    rta = input(f"¿Desea registrar otro sismo? ")
        elif (opMenu == 3):
            os.system("cls")
            nombre = input(f"Ingrese el nombre de la ciudad que desea buscar : ")
            ciudad.buscarCiudad(nombre)
        elif (opMenu == 4):
            os.system("cls")
            sismo.reporte()
        elif (opMenu == 5):
            isActive = False
            print(f"GRACIAS POR USAR NUESTRO SERVICIO")
        else:
            print(f"La opción ingresada es inválida")
        os.system("pause")