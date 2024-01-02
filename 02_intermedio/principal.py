import os
import menus as menu
import dependencias as dependencia

isActive = True
opMenu = 0
headerD = """
************************
* REGISTRO DEPENDENCIA *
************************
"""

while (isActive):
    os.system("cls")
    try:
        opMenu = menu.menuPrincipal()
    except ValueError:
        print(f"Error en el dato de ingreso")
    else:
        if (opMenu == 1):
            rta = "S"
            while(rta in ["S", "s"]):
                os.system("cls")
                print(headerD)
                valor = 0
                codigo = dependencia.regDependencia(valor, "código (3 cifras)", int)
                nombre = dependencia.regDependencia(valor, "nombre", str)
                co2Producido = 0
                dependencia.registroDependencia = [codigo, nombre, [], [], co2Producido]
                dependencia.dependencias.append(dependencia.registroDependencia)
                rta = input(f"¿Desea registrar otra dependencia? S(Sí) o Enter(No) : ")
            print(f"")
        elif (opMenu == 2):
            os.system("cls")
            menu.menuDependencia()
            print(f"")
        elif (opMenu == 3):
            os.system("cls")
            dependencia.calcularEmisiones()
            print(f"")
        elif (opMenu == 4):
            os.system("cls")
            max = 0
            nomMax = ""
            for i in range(len(dependencia.dependencias)):
                if (float(dependencia.dependencias[i][4]) > max):
                    max = float(dependencia.dependencias[i][4])
                    nomMax = dependencia.dependencias[i][1]
            print(f"DEPENDENCIA QUE PRODUCE MAYOR C02 : {nomMax}")
            print(f"")
        elif (opMenu == 5):
            print(f"")
            print(f"GRACIAS POR USAR NUESTRO SERVICIO")
            print(f"")
            isActive = False
        else:
            print(f"Ingrese una opción válida")
        os.system("pause")