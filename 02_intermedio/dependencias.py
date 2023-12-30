dependencias = []
registroDependencia = []
isIncorrect = True

def regDependencia(valorDato, nombreDato, tipoDato):
    global isIncorrect
    isIncorrect = True
    valorDato = 0
    while (isIncorrect):
        try:
            valorDato = tipoDato(input(f"Ingrese {nombreDato} de la dependencia: "))
        except ValueError:
            print(f"Ingrese un dato correcto")
        else:
            if (nombreDato == "código (3 cifras)" and len(str(valorDato)) != 3):
                regDependencia(valorDato, nombreDato, tipoDato)
            else: 
                isIncorrect = False
    return valorDato

def buscarDependencia(codigoDepedencia : int) -> int:
    global indice
    indice = -1
    for item in dependencias:
        if codigoDepedencia in item:
            indice = dependencias.index(item)
    return indice

def regConsumoDispositivos(indiceDependencia : int):
    potencia = float(input(f"Ingrese la potencia del dispositivo en W : "))
    tiempoUso = int(input(f"Ingrese el tiempo de uso en horas : "))
    consumoDispositivo = (potencia * tiempoUso) / 1000
    registroDependencia[indiceDependencia][2].append(consumoDispositivo)

def regConsumoTransporte(indiceDependencia : int):
    kmRecorridos = float(input(f"Ingrese el número de kilómetros recorridos por el transporte : "))
    registroDependencia[indiceDependencia][3].append(kmRecorridos)

def calcularEmisiones():
    for i in range(len(dependencias)):
        emiDispositivos = sum(registroDependencia[i][2]) * 0.1
        emiTransporte = sum(registroDependencia[i][3]) * 0.3
        emiTotal = emiDispositivos + emiTransporte
        registroDependencia[i][4] = emiTotal
    print(dependencias)