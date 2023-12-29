productos = []
registroProducto = []
indice = -1
isIncorrect = True

def regProducto(valorDato, nombreDato, tipoDato):
    global isIncorrect
    isIncorrect = True
    valorDato = 0
    while (isIncorrect):
        try:
            valorDato = tipoDato(input(f"Ingrese {nombreDato} del producto: "))
        except ValueError:
            print(f"Ingrese un dato correcto")
        else:
            registroProducto.append(valorDato)
            isIncorrect = False
    return registroProducto

def mostrarInventario():
    print(f"INVENTARIO")
    print(f"------------------------------------------------------------------------------------------------------------------------")
    print("{:<10} {:<10} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format("CÓDIGO", "NOMBRE", "VALOR COMPRA", "VALOR VENTA", "STOCK MÍNIMO", "STOCK MÁXIMO", "STOCK ACTUAL", "NOMBRE PROVEEDOR"))
    for i in productos:
        codigo, nombre, valorCompra, valorVenta, stockMin, stockMax, stockActual, nombreProveedor = i
        print("{:<10} {:<10} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(codigo, nombre, valorCompra, valorVenta, stockMin, stockMax, stockActual, nombreProveedor))
    print(f"")

def buscarProducto(codigoProducto : int) -> int: #REVISIÓN
    global indice
    for item in productos:
        if codigoProducto in item:
            indice = productos.index(item)
    if (indice == -1):
        print(f"No se encontró el producto")
    return indice

def imprimirInforme():
    print(f"INFORME DE PRODUCTOS CRÍTICOS")
    print(f"------------------------------------------------------------------------------------------------------------------------")
    print("{:<10} {:<10} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format("CÓDIGO", "NOMBRE", "VALOR COMPRA", "VALOR VENTA", "STOCK MÍNIMO", "STOCK MÁXIMO", "STOCK ACTUAL", "NOMBRE PROVEEDOR"))
    for i in range(len(productos)):
        if (productos[i][6] < productos[i][4]):
            print("{:<10} {:<10} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(productos[i][0], productos[i][1], productos[i][2], productos[i][3], productos[i][4], productos[i][5], productos[i][6], productos[i][7]))
    print(f"")