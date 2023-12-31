import os
import menus as menu

isActive = True
opMenu = 0

while (isActive):
    os.system("cls")
    try:
        opMenu = menu.menuPrincipal()
    except ValueError:
        print(f"Ingrese un dato válido")
    else:
        if (opMenu == 1):
            menu.menuRegistroJ()
        elif (opMenu == 2):
            menu.menuRegistroP()
        elif (opMenu == 3):
            pass
        elif (opMenu == 4):
            pass
        elif (opMenu == 5):
            isActive = False
            print(f"GRACIAS POR USAR NUESTRO SERVICIO")
            os.system("pause")