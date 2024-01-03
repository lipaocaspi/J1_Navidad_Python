#### Ejercicios Principiante
#### 1. Análisis:
**Problema:** realizar un programa que reciba 3 números enteros positivos e imprima la sumatoria de ellos.
**Cómo:** 
* Crear una lista que almacene los valores de los números a ingresar.
* Por medio de un **while**, repetir la solicitud de ingreso de los valores hasta que los valores correspondan al tipo de dato y se ingresen 3 de ellos.
* Dentro del mismo **while**, verificar, haciendo uso de un **if**, que los valores ingresados sean números enteros positivos y agregarlos a la lista creada.
* Realizar la suma de los valores ingresados en la lista y asignarla en una variable.
* Imprimir el valor de la variable correspondiente a la suma.

**Variables:**
| Variable   |      E/S      |  Tipo de Dato |
|----------|:-------------:|------:|
| num | E |    int |
| nums|  S | list |
| suma | S |    int |

En el archivo [01_principiante.py](https://github.com/lipaocaspi/J1_navidad_python/blob/main/01_principiante.py) se encuentra el código.

#### 2. Análisis:
**Problema:** calcular el IMC de los estudiantes nuevos de Campuslands, teniendo en cuenta su altura y peso. Mostrar el nombre, la edad, el IMC y la categoría según el IMC obtenido.
**Cómo:** 
* Crear una función que realice el correspondiente manejo de excepciones.
* Pedir al usuario que ingrese los datos relacionados con el estudiante (nombre, edad, peso y altura).
* Calcular el IMC: $\frac{peso (Kg)}{(altura (m))^2}$
* Inicializar la variable de categoria.
* Crear un lista que almacene los datos ingresados y calculados.
* Haciendo uso de un **if**, asignar el nombre de la categoría correspondiente, teniendo en cuenta el valor del IMC.
* Imprimir los datos solicitados (nombre, edad, IMC y categoría).

**Variables:**
| Variable   |      E/S      |  Tipo de Dato |
|----------|:-------------:|------:|
| nombre | E |    str |
| edad|  E | int |
| peso |    E  |   float |
| altura | E |    float |
| imc |    E  |   float |
| categoria | S |    float |
| estudiante | S |    list |

En el archivo [02_principiante.py](https://github.com/lipaocaspi/J1_navidad_python/blob/main/02_principiante.py) se encuentra el código.

#### 3. Análisis:
**Problema:** teniendo en cuenta el ejercicio anterior, realizar el ingreso de los datos de 20 estudiantes, haciendo un conteo de la cantidad de estudiantes pertenecientes a cada categoría.
**Cómo:** 
* Crear una función que realice el correspondiente manejo de excepciones.
* Inicializar las variables del conteo de cada categoría.
* Crear una lista vacía (estudiantes) que almacene las listas correspondientes a cada estudiante.
* Haciendo uso de un **for**:
	* Pedir al usuario que ingrese los datos relacionados con el estudiante (nombre, edad, peso y altura).
	* Calcular el IMC: $\frac{peso (Kg)}{(altura (m))^2}$
	* Inicializar la variable de categoria.
	* Crear un lista que almacene los datos ingresados y calculados.
	* Agregar la lista creada a la lista estudiantes.
	* Haciendo uso de un **if**, asignar el nombre de la categoría correspondiente, teniendo en cuenta el valor del IMC y sumar 1 al valor de la variable correspondiente a la categoría.
* Imprimir los datos solicitados (nombre, edad, IMC y categoría).

**Variables:**
| Variable   |      E/S      |  Tipo de Dato |
|----------|:-------------:|------:|
| nombre | E |    str |
| edad|  E | int |
| peso |    E  |   float |
| altura | E |    float |
| imc |    S  |   float |
| categoria | S |    float |
| estudiante | S |    list |
| estudiantes |    S  |   list |
| contadorIdeal | S |    int |
| contadorObesidadI |    S  |   int |
| contadorObesidadII | S |    int |
| contadorObesidadIII | S |    int |
| contadorSobrepeso | S |    int |

En el archivo [03_principiante.py](https://github.com/lipaocaspi/J1_navidad_python/blob/main/03_principiante.py) se encuentra el código.

#### 4. Análisis:
**Problema:** recibir n números enteros positivos, y al recibir un número entero negativo, mostrar un reporte de la cantidad de números registrados y el promedio de los pares e impares.

**Cómo:** 
* Crear una lista para almacenar cada uno de los números, dependiendo de:
	* Total de números ingresados.
	* Total de números pares ingresados.
	* Total de números impares ingresados.
	* Total de números menores a 10.
	* Total de números entre 20 y 50.
	* Total de números mayores que 100.
* Pedir al usuario que ingrese un número entero positivo, y por medio de un **while** y un **try-except**, verificar que el tipo de dato sea correcto.
* Si el tipo de dato es correcto, se verifica por medio de **if** si es par o impar, así como si es menor de 10, está entre 20 y 50, o es mayor a 100. Se agrega a la lista correspondiente.
* Para calcular el promedio de los números pares e impares:
	* promedioPares = $\frac{sum(paresIngresados)}{len(paresIngresados)}$
	
	* promedioImpares = $\frac{sum(imparesIngresados)}{len(imparesIngresados)}$
* Se imprime el reporte.

**Variables:**

| Variable   |      E/S      |  Tipo de Dato |
|----------|:-------------:|------:|
| num | E |    int |
| ingresados | S |    list |
| paresIngresados|  S | list |
| imparesIngresados |    S  |   list |
| promedioPares | S |    float |
| promedioImpares |    S  |   float |
| menoresDiez | S |    list |
| veinteCincuenta | S |    list |
| mayoresCien | S |    list |

En el archivo [04_principiante.py](https://github.com/lipaocaspi/J1_navidad_python/blob/main/04_principiante.py) se encuentra el código.
