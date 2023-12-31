import os
import menus as menu
import jugadores as jugador

isActive = True
opMenu = 0

while (isActive):
    try:
        opMenu = menu.menuPrincipal()
    except ValueError:
        print(f"Ingrese un dato válido")
    else:
        if (opMenu == 1):
            menu.menuRegistroJ()
            # jugadores.update(jugador.regJugador())
        elif (opMenu == 2):
            pass
        elif (opMenu == 3):
            pass
        elif (opMenu == 4):
            pass
        elif (opMenu == 5):
            isActive = False

os.system("pause")