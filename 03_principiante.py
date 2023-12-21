# CÁLCULO IMC DE ESTUDIANTES CON REPORTE

header = """
*******
REPORTE
*******
"""

contadorIdeal = 0
contadorObesidadI = 0
contadorObesidadII = 0
contadorObesidadIII = 0
contadorSobrepeso = 0

for i in range(1, 21):
    nombre = input("Ingrese el nombre del estudiante : ")
    edad = int(input("Ingrese la edad del estudiante : "))
    peso = int(input("Ingrese el peso del estudiante : "))
    altura = float(input("Ingrese la altura del estudiante : "))
    imc = peso/pow(altura, 2)
    categoria = ""
    estudiante = [nombre, edad, peso, altura, imc, categoria]

    if (imc >= 18.5 and imc <= 24.9):
        estudiante[5] = "Normal"
        contadorIdeal = contadorIdeal + 1
    elif (imc >= 25 and imc <= 29.9):
        estudiante[5] = "Sobrepeso"
        contadorSobrepeso = contadorSobrepeso + 1
    elif (imc >= 30 and imc <= 34.9):
        estudiante[5] = "Obesidad I"
        contadorObesidadI = contadorObesidadI + 1
    elif (imc >= 35 and imc <= 39.9):
        estudiante[5] = "Obesidad II"
        contadorObesidadII = contadorObesidadII + 1
    elif (imc > 40):
        estudiante[5] = "Obesidad III"
        contadorObesidadIII = contadorObesidadIII + 1

print(header)
print("# ESTUDIANTES CON PESO IDEAL: ", contadorIdeal)
print("# ESTUDIANTES CON OBESIDAD I: ", contadorObesidadI)
print("# ESTUDIANTES CON OBESIDAD II: ", contadorObesidadII)
print("# ESTUDIANTES CON OBESIDAD III: ", contadorObesidadIII)
print("# ESTUDIANTES CON SOBREPESO: ", contadorSobrepeso)