# REPORTE DE INGRESO DE NÚMEROS

import os

header = """
****************************************
\tREPORTE
****************************************
"""

ingresados = []
paresIngresados = []
imparesIngresados = []
promedioPares = 0
promedioImpares = 0
menoresDiez = []
veinteCincuenta = []
mayoresCien = []
isPositive = True

os.system("cls")

while (isPositive):
    try:
        num = int(input(f"Ingrese el número : "))
    except:
        print(f"Ingrese un dato válido")
    else:
        if (num >= 0):
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

os.system("cls")

print(header)
print(f"Total de números ingresados : {len(ingresados)}" )
print(f"Total de números pares ingresados : {len(paresIngresados)}")
print(f"Promedio de los números pares : {promedioPares}")
print(f"Promedio de los números impares : {promedioImpares}")
print(f"Total de números menores que 10 : {len(menoresDiez)}")
print(f"Total de números entre 20 y 50 : {len(veinteCincuenta)}")
print(f"Total de números mayores que 100 : {len(mayoresCien)}")
print(f"")

os.system("pause")