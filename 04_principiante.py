# REPORTE DE INGRESO DE NÚMEROS

ingresados = []
paresIngresados = []
imparesIngresados = []
promedioPares = 0
promedioImpares = 0
menoresDiez = []
veinteCincuenta = []
mayoresCien = []
isPositive = True

while (isPositive):
    num = int(input("Ingrese el número : "))
    if (num > 0):
        ingresados.append(num)
        if (num % 2 == 0):
            paresIngresados.append(num)
        else:
            imparesIngresados.append(num)
        if (num < 10):
            menoresDiez.append(num)
        elif (num >= 20 and num <= 50):
            veinteCincuenta.append(num)
        elif (num > 100):
            mayoresCien.append(num)
    else:
        isPositive = False

promedioPares = sum(paresIngresados)/len(paresIngresados)
promedioImpares = sum(imparesIngresados)/len(imparesIngresados)

print("REPORTE")
print("Total de números ingresados : ", len(ingresados))
print("Total de números pares ingresados : ", len(paresIngresados))
print("Promedio de los números pares : ", promedioPares)
print("Promedio de los números impares : ", promedioImpares)
print("Total de números menores que 10 : ", len(menoresDiez))
print("Total de números entre 20 y 50 : ", len(veinteCincuenta))
print("Total de números mayores que 100 : ", len(mayoresCien))