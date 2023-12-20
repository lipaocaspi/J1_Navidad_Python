isNegative = True
sum = 0
contador = 0

while (contador < 3):
    while (isNegative):
        num = int(input("Ingrese el número "))
        if (num >= 0):
            sum = sum + num
            contador = contador + 1
            if (contador == 3):
                isNegative = False
        else:
            isNegative = False

print("La sumatoria de los números es", sum)