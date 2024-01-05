# CÁLCULO IMC DE ESTUDIANTES CON REPORTE

import os

header = """
******************************************
*  CÁLCULO IMC ESTUDIANTES CAMPUSLANDS   *
******************************************
"""

def verify(valorDato, nombreDato, tipoDato):
    valorDato = 0
    isIncorrect = True
    while (isIncorrect):
        try:
            valorDato = tipoDato(input(f"Ingrese {nombreDato} del estudiante : "))
        except ValueError:
            print(f"Ingrese un dato válido")
        else:
            if (valorDato <= 0):
                print(f"Ingrese un número positivo")
            else:
                isIncorrect = False
    return valorDato

contadorIdeal = 0
contadorObesidadI = 0
contadorObesidadII = 0
contadorObesidadIII = 0
contadorSobrepeso = 0
estudiantes = []

for i in range(1, 21):
    os.system("cls")
    print(header)
    nombre = input(f"Ingrese el nombre del estudiante : ")
    valor = 0
    edad = verify(valor, "edad", int)
    peso = verify(valor, "peso (en kilos)", float)
    altura = verify(valor, "altura (en metros)", float)
    imc = peso/pow(altura, 2)
    categoria = ""
    estudiante = [nombre, edad, peso, altura, imc, categoria]
    estudiantes.append(estudiante)

    if (imc >= 18.5 and imc <= 24.9):
        estudiantes[i-1][5] = "Normal"
        contadorIdeal = contadorIdeal + 1
    elif (imc >= 25 and imc <= 29.9):
        estudiantes[i-1][5] = "Sobrepeso"
        contadorSobrepeso = contadorSobrepeso + 1
    elif (imc >= 30 and imc <= 34.9):
        estudiantes[i-1][5] = "Obesidad I"
        contadorObesidadI = contadorObesidadI + 1
    elif (imc >= 35 and imc <= 39.9):
        estudiantes[i-1][5] = "Obesidad II"
        contadorObesidadII = contadorObesidadII + 1
    elif (imc > 40):
        estudiantes[i-1][5] = "Obesidad III"
        contadorObesidadIII = contadorObesidadIII + 1
    os.system("pause")

os.system("cls")

print(header)
print(f"ESTUDIANTES CON PESO IDEAL : \t{contadorIdeal}")
print(f"ESTUDIANTES CON OBESIDAD I : \t{contadorObesidadI}")
print(f"ESTUDIANTES CON OBESIDAD II : \t{contadorObesidadII}")
print(f"ESTUDIANTES CON OBESIDAD III : \t{contadorObesidadIII}")
print(f"ESTUDIANTES CON SOBREPESO : \t{contadorSobrepeso}")
print(f"")

os.system("pause")