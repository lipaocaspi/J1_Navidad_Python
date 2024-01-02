import os
import menu
import productos as producto

isActive = True
opMenu = 0
header = """
    **************************************************
    *     REGISTRO DE PRODUCTOS EN UN INVENTARIO     *
    **************************************************
    """

while (isActive):
    os.system("cls")
    try:
        print(header)
        opMenu = menu.menuShow()
    except ValueError:
        print(f"Error en el dato de ingreso")
    else:
        if (opMenu == 1):
            rta = "S"
            headerR = """
            ************************
            *  REGISTRAR PRODUCTO  *
            ************************
            """
            while (rta in ["S", "s"]):
                os.system("cls")
                print(headerR)
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
                rta = input(f"¿Desea registrar otro producto? S(Sí) o Enter(No) : ")
        elif (opMenu == 2):
            os.system("cls")
            producto.mostrarInventario()
        elif (opMenu == 3):
            rta = "S"
            headerA = """
            **********************
            *  ACTUALIZAR STOCK  *
            **********************
            """
            while (rta in ["S", "s"]):
                isIncorrect = True
                os.system("cls")
                print(headerA)
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
                rta = input(f"¿Desea registrar otra actualización de stock? S(Sí) o Enter(No) : ")
        elif (opMenu == 4):
            os.system("cls")
            producto.imprimirInforme()
        elif (opMenu == 5):
            os.system("cls")
            producto.calGanaciaP()
        elif (opMenu == 6):
            print(f"")
            print(f"GRACIAS POR USAR NUESTRO SERVICIO")
            isActive = False
        else:
            print(f"La opción ingresada es inválida")
        print(f"")
        os.system("pause")