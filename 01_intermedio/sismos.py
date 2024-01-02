import ciudades as ciudad

isIncorrect = True

def regSismo(ciudadSismo : int) -> list:
    global isIncorrect
    isIncorrect = True
    while (isIncorrect):
        try:
            sismo = float(input(f"Ingrese la intensidad del sismo : "))
        except ValueError:
            print(f"Ingrese un dato correcto")
        else:
            ciudad.sismos[ciudadSismo][1].append(sismo)
            isIncorrect = False
            return ciudad.sismos
        
def reporte():
    if (len(ciudad.sismos) < 5):
        print(f"Por favor registre las 5 ciudades")
    elif (len(ciudad.sismos[0][1]) == len(ciudad.sismos[1][1]) == len(ciudad.sismos[2][1]) == len(ciudad.sismos[3][1]) == len(ciudad.sismos[4][1]) > 0):
        if (len(ciudad.sismos[0][1]) == len(ciudad.sismos[1][1]) == len(ciudad.sismos[2][1]) == len(ciudad.sismos[3][1]) == len(ciudad.sismos[4][1])):
            print(f"INFORME DE RIESGOS")
            print(f"")
            print("{:<15} {:<15} {:<20}".format("CIUDAD", "PROMEDIO", "RIESGO"))
            print(f"----------------------------------------------------------")
            for i in range(len(ciudad.sismos)):
                ciudad.sismos[i][2] = (sum(ciudad.sismos[i][1])) / len(ciudad.sismos[i][1])
                if (float(ciudad.sismos[i][2]) < 2.5):
                    ciudad.sismos[i][3] = "Amarillo - Sin Riesgo"
                elif (float(ciudad.sismos[i][2]) >= 2.6 and int(ciudad.sismos[i][2]) <= 4.5):
                    ciudad.sismos[i][3] = "Naranja - Riesgo Medio"
                elif (float(ciudad.sismos[i][2]) > 4.5):
                    ciudad.sismos[i][3] = "Rojo - Riesgo Alto"
                print("{:<15} {:<15} {:<20}".format(ciudad.sismos[i][0], ciudad.sismos[i][2], ciudad.sismos[i][3]))
                print(f"")
        else:
            print(f"Deben haber el mismo número de registros en cada ciudad")
    else:
            print(f"Debe existir al menos un registro de sismo en cada ciudad")