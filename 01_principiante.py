# SUMATORIA DE 3 NÚMEROS ENTEROS POSITIVOS

import os

nums = []
isNegative = True
suma = 0

header = """
********************************************
* SUMATORIA DE 3 NÚMEROS ENTEROS POSITIVOS *
********************************************
"""
os.system("cls")
print(header)

while (isNegative):
    try:
        num = int(input(f"Ingrese el número : "))
    except ValueError:
        print(f"Ingrese un dato válido")
    else:
        if (num >= 0):
            nums.append(num)
        else:
            print(f"Ingrese un número entero positivo")
    if (len(nums) == 3):
        isNegative = False
        suma = sum(nums)

print(f"")
print(f"La sumatoria de los números es : {suma}")

os.system("pause")