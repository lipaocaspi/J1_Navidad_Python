import os
import menu
import productos as producto

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
                valor = 0
                codigo = producto.regProducto(valor, "código (3 cifras)", int)
                nombre = producto.regProducto(valor, "nombre", str)
                valorCompra = producto.regProducto(valor, "valor de compra", float)
                valorVenta = producto.regProducto(valor, "valor de venta", float)
                stockMin = producto.regProducto(valor, "stock mínimo", int)
                stockMax = producto.regProducto(valor, "stock máximo", int)
                stockActual = producto.regProducto(valor, "stock actual", int)
                nombreProveedor = producto.regProducto(valor, "nombre del proveedor", str)
                producto.productos.append(producto.registroProducto)
                producto.registroProducto = []
                rta = input(f"¿Desea registrar otro producto? : ")
        elif (opMenu == 2):
            os.system("cls")
            producto.mostrarInventario()
        elif (opMenu == 3):
            isIncorrect = True
            os.system("cls")
            while (isIncorrect):
                try:
                    codigo = int(input(f"Ingrese código del producto que desee actualizar stock : "))
                except ValueError:
                    print(f"Ingrese un dato válido")
                else:
                    if (len(str(codigo)) != 3):
                        print(f"Ingrese un código de 3 cifras")
                    else:
                        producto.buscarProducto(codigo)
                        isIncorrect = False
            producto.actStock()
        elif (opMenu == 4):
            os.system("cls")
            producto.imprimirInforme()
        elif (opMenu == 5):
            os.system("cls")
            producto.calGanaciaP()
        elif (opMenu == 6):
            isActive = False
            print(f"GRACIAS POR USAR NUESTRO SERVICIO")
        else:
            print(f"La opción ingresada es inválida")
        os.system("pause")