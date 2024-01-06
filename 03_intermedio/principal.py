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
                codigo = producto.regProducto(valor, "código", str)
                nombre = input(f"Ingrese nombre del producto : ")
                valorCompra = producto.regProducto(valor, "valor de compra", float)
                valorVenta = producto.regProducto(valor, "valor de venta", float)
                stockMin = producto.regProducto(valor, "stock mínimo", int)
                stockMax = producto.regProducto(valor, "stock máximo", int)
                stockActual = producto.regProducto(valor, "stock actual", int)
                nombreProveedor = input(f"Ingrese nombre del proveedor del producto : ")
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
                os.system("cls")
                print(headerA)
                codigo = input(f"Ingrese código del producto que desee actualizar stock : ")
                indice = producto.buscarProducto(codigo)
                if (indice == -1):
                    print(f"No se encontró el producto")
                else:
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