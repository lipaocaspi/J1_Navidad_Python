# SUMATORIA DE 3 NÚMEROS POSITIVOS

nums = []
isNegative = True
suma = 0

while (isNegative):
    num = int(input("Ingrese el número : "))
    if (num >= 0):
        nums.append(num)
    else:
        print("Ingrese un número entero positivo")
    if (len(nums) == 3):
        isNegative = False
        suma = sum(nums)

print("La sumatoria de los números es", suma)