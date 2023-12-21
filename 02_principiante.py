# CÁLCULO IMC DE ESTUDIANTES

header = """
***********
CÁLCULO IMC
***********
"""

nombre = input("Ingrese el nombre del estudiante ")
edad = int(input("Ingrese la edad del estudiante "))
peso = int(input("Ingrese el peso del estudiante "))
altura = float(input("Ingrese la altura del estudiante "))
imc = peso/pow(altura, 2)
categoria = ""
estudiante = [nombre, edad, peso, altura, imc, categoria]

if (imc >= 18.5 and imc <= 24.9):
    estudiante[5] = "Normal"
elif (imc >= 25 and imc <= 29.9):
    estudiante[5] = "Sobrepeso"
elif (imc >= 30 and imc <= 34.9):
    estudiante[5] = "Obesidad I"
elif (imc >= 35 and imc <= 39.9):
    estudiante[5] = "Obesidad II"
elif (imc > 40):
    estudiante[5] = "Obesidad III"

print(header)
print("Nombre: ", estudiante[0])
print("Edad: ", estudiante[1])
print("IMC: ", estudiante[4])
print("Categoría: ", estudiante[5])