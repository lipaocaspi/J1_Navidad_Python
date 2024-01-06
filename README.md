# J1_navidad_python

## Ejercicios Principiante
#### 1. Análisis:
* **Problema:** realizar un programa que reciba 3 números enteros positivos e imprima la sumatoria de ellos.
* **Cómo:** 
	* Crear una lista que almacene los valores de los números a ingresar.
	* Por medio de un **while**, repetir la solicitud de ingreso de los valores hasta que los valores correspondan al tipo de dato y se ingresen 3 de ellos.
	* Dentro del mismo **while**, verificar, haciendo uso de un **if**, que los valores ingresados sean números enteros positivos y agregarlos a la lista creada.
	* Realizar la suma de los valores ingresados en la lista y asignarla a una variable.
	* Imprimir el valor de la variable correspondiente a la suma.

* **Variables:**

| Variable   |      E/S      |  Tipo de Dato |
|----------|:-------------:|------:|
| num | E |    int |
| nums|  S | list |
| suma | S |    int |

En el archivo [01_principiante.py](https://github.com/lipaocaspi/J1_navidad_python/blob/main/01_principiante.py) se encuentra el código.

#### 2. Análisis:
* **Problema:** calcular el IMC de los estudiantes nuevos de Campuslands, teniendo en cuenta su altura y peso. Mostrar el nombre, la edad, el IMC y la categoría según el IMC obtenido.
* **Cómo:** 
	* Crear una función que realice el correspondiente manejo de excepciones.
	* Pedir al usuario que ingrese los datos relacionados con el estudiante (nombre, edad, peso y altura).
	* Calcular el IMC: $\frac{peso (Kg)}{(altura (m))^2}$
	* Inicializar la variable de categoria.
	* Crear un lista que almacene los datos ingresados y calculados.
	* Haciendo uso de un **if**, asignar el nombre de la categoría correspondiente, teniendo en cuenta el valor calculado del IMC.
	* Imprimir los datos solicitados (nombre, edad, IMC y categoría).

* **Variables:**

| Variable   |      E/S      |  Tipo de Dato |
|----------|:-------------:|------:|
| nombre | E |    str |
| edad|  E | int |
| peso |    E  |   float |
| altura | E |    float |
| imc |    E  |   float |
| categoria | S |    str |
| estudiante | S |    list |

En el archivo [02_principiante.py](https://github.com/lipaocaspi/J1_navidad_python/blob/main/02_principiante.py) se encuentra el código.

#### 3. Análisis:
* **Problema:** teniendo en cuenta el ejercicio anterior, realizar el ingreso de los datos de 20 estudiantes, haciendo un conteo de la cantidad de estudiantes pertenecientes a cada categoría.
* **Cómo:** 
	* Crear una función que realice el correspondiente manejo de excepciones.
	* Inicializar las variables del conteo de cada categoría.
	* Crear una lista vacía (estudiantes) que almacene las listas correspondientes a cada estudiante.
	* Haciendo uso de un **for**:
		* Pedir al usuario que ingrese los datos relacionados con el estudiante (nombre, edad, peso y altura).
		* Calcular el IMC: $\frac{peso (Kg)}{(altura (m))^2}$
		* Inicializar la variable de categoria.
		* Crear un lista que almacene los datos ingresados y calculados.
		* Agregar la lista creada a la lista estudiantes.
		* Haciendo uso de un **if**, asignar el nombre de la categoría correspondiente, teniendo en cuenta el valor del IMC y sumar 1 al valor de la variable correspondiente al conteo de cada categoría.
	* Imprimir el reporte de la cantidad de estudiantes que hay en cada categoría.

* **Variables:**

| Variable   |      E/S      |  Tipo de Dato |
|----------|:-------------:|------:|
| nombre | E |    str |
| edad|  E | int |
| peso |    E  |   float |
| altura | E |    float |
| imc |    S  |   float |
| categoria | S |    str |
| estudiante | S |    list |
| estudiantes |    S  |   list |
| contadorIdeal | S |    int |
| contadorObesidadI |    S  |   int |
| contadorObesidadII | S |    int |
| contadorObesidadIII | S |    int |
| contadorSobrepeso | S |    int |

En el archivo [03_principiante.py](https://github.com/lipaocaspi/J1_navidad_python/blob/main/03_principiante.py) se encuentra el código.

#### 4. Análisis:
* **Problema:** recibir n números enteros positivos, y al recibir un número entero negativo, mostrar un reporte de la cantidad de números registrados teniendo en cuenta varias condiciones, y el promedio de los pares e impares.
* **Cómo:** 
	* Crear una lista para almacenar cada uno de los números, dependiendo de:
		* Total de números ingresados.
		* Total de números pares ingresados.
		* Total de números impares ingresados.
		* Total de números menores a 10.
		* Total de números entre 20 y 50.
		* Total de números mayores que 100.
	* Dentro de un **while**, pedir al usuario que ingrese un número entero positivo, y por medio de un **try-except**, verificar que el tipo de dato sea correcto.
	* Si el tipo de dato es correcto, se verifica por medio de varios **if** si es par o impar, así como si es menor de 10, está entre 20 y 50, o es mayor a 100. Se agrega a la lista correspondiente.
   	* Si el número ingresado es negativo, se detiene la iteración **while**.
	* Para calcular el promedio de los números pares e impares:
		* promedioPares = $\frac{sum(paresIngresados)}{len(paresIngresados)}$
	
		* promedioImpares = $\frac{sum(imparesIngresados)}{len(imparesIngresados)}$
	* Se imprime el reporte.

* **Variables:**

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

## Ejercicios Intermedio
#### 1. Análisis:
* **Problema:** llevar un registro de los sismos ocurridos en 5 ciudades del país, calcular su promedio y asignar la clasificación dependiendo de su valor.
* **Cómo:** 
	* Dividir el programa en 4 módulos:
		* ciudades
		* menu
		* sismos
		* principal
	* **Módulo ciudades:**
		se definen:
		* **regCiudad() :** solicita el código de la ciudad y si el código digitado no existe, se solicita el nombre de la ciudad y se agrega a una lista, junto a una lista vacía, un promedio igual a 0 y un riesgo igual a "". Esta lista se agrega a una lista que contiene las listas de las ciudades.
  		* * **buscarId(codigoCiudad) :** toma el código de la ciudad digitado por el usuario y lo busca dentro de la lista que almacena todas las listas de las ciudades. Si encuentra el código de la ciudad, devuelve el índice. Si no lo encuentra, devuelve un índice = -1.
		* **buscarCiudad(codigoCiudad) :** toma el código de la ciudad digitado por el usuario y lo busca dentro de la lista que almacena todas las listas de las ciudades. Si encuentra el código de la ciudad, devuelve el índice e imprime la información correspondiente a esa ciudad. Si no lo encuentra, devuelve un índice = -1.
	* **Módulo menu:**
		se define:
		* **menuShow() :** repite la impresión del menú mientras el dato ingresado no corresponda al tipo definido.
	* **Módulo sismos:**
		se definen:
		* **regSismo(ciudadSismo) :** recibe el índice de la ciudad. Solicita el dato digitado de la intensidad del sismo, y si el dato es correcto, agrega el valor a la lista que se encuentra dentro de la lista correspondiente al índice de la ciudad.
		* **reporte() :** verificando que se hayan registrado las 5 ciudades, que haya al menos un sismo registrado en cada ciudad y que el número de sismos en cada ciudad sea el mismo, se calcula el promedio de los sismos de cada ciudad y se asigna su clasificación. Se imprime la tabla mostrando: la ciudad, el promedio de sismos y la clasificación.
	* **Módulo principal:**
		* Haciendo uso de un **while** y un **try-except**, se muestra el menú de opciones.
		* Dependiendo de la opción que digite el usuario, se llaman a las funciones creadas en los distintos módulos.

* **Variables:**

| Variable   |      E/S      |  Tipo de Dato |
|----------|:-------------:|------:|
| opMenu| E |    int |
| codigo| E |    str|
| ciudad| E |    str|
| nombre| E |    str|
| sismo| E |    float|
| rta| E |    str|
| indice| S |    int|
| registroCiudad|  S | list |
| sismos| S |    list|
| promedio| S |    float |
| riesgo| S |    str |

En el directorio [01_intermedio](https://github.com/lipaocaspi/J1_navidad_python/tree/main/01_intermedio) se encuentra el código con sus respectivos módulos.

#### 2. Análisis:
* **Problema:** calcular el CO2 producido en diferentes instalaciones gubernamentales de la ciudad.
* **Cómo:** 
	* Dividir el programa en 3 módulos:
		* dependencias
		* menus
		* principal
	* **Módulo dependencias:**
		se definen:
		* **buscarDependencia(codigoDependencia) :** toma el código de la dependencia digitado por el usuario y lo busca dentro de la lista que almacena todas las listas de las dependencias. Si encuentra el código de la dependencia, extrae el índice de la lista. Si no lo encuentra, devuelve un índice = -1.
		* **regDependencia(valorDato, nombreDato) :** toma el valor del dato y el nombre del dato correspondiente a la dependencia y, si el dato digitado es diferente a "" y es correcto, sale de la función.
		* **regConsumoDispositivos(indiceDependencia) :** recibe el índice de la dependencia. Solicita el dato digitado de la potencia del dispositivo y el tiempo de uso del dispositivo, y si los datos son correctos, calcula el valor del consumo del dispositivo: $\frac{potencia * tiempoUso}{1000}$. Agrega el valor a la primera lista que se encuentra dentro de la lista correspondiente al índice de la dependencia.
		* **regConsumoTransporte(indiceDependencia) :** recibe el índice de la dependencia. Solicita el dato digitado de la cantidad de kilómetros recorridos por el transporte, y si el dato es correcto, agrega el valor a la segunda lista que se encuentra dentro de la lista correspondiente al índice de la dependencia.
		* **calcularEmisiones() :** hace la sumatoria de los valores ingresados en cada lista de cada una de las dependencias y las multiplica por el factor de emisión correspondiente. Se suman los dos resultados y se imprime la información correspondiente.
	* **Módulo menus:**
		se definen:
		* **menuPrincipal() :** repite la impresión del menú mientras el dato ingresado no corresponda al tipo definido.
		* **menuDependencia() :** repite la impresión del menú mientras el dato ingresado no corresponda al tipo definido. Dependiendo de la opción que digite el usuario, se llaman a las funciones creadas en los distintos módulos.
	* **Módulo principal:**
		* Haciendo uso de un **while** y un **try-except**, se muestra el menú de opciones.
		* Dependiendo de la opción que digite el usuario, se llaman a las funciones creadas en los distintos módulos.

* **Variables:**

| Variable   |      E/S      |  Tipo de Dato |
|----------|:-------------:|------:|
| opMenu| E |    int |
| codigo| E | str|
| nombre| E | str|
| valorDato | E |    str|
| potencia| E | float |
| tiempoUso| E | int|
| kmRecorridos| E | float |
| consumoDispositivo| S | float|
| emiDispositivos | S | float |
| emiTransporte | S | float|
| emiTotal | S | float |
| co2Producido| S | float |
| dependencias| S |    list|
| registroDependencia| S |    list|
| valorDato | S |    float |
| riesgo| S |    str |
| max| S | float|
| nomMax| S | str|

En el directorio [02_intermedio](https://github.com/lipaocaspi/J1_navidad_python/tree/main/02_intermedio) se encuentra el código con sus respectivos módulos.

#### 3. Análisis:
* **Problema:** realizar el control detallado de productos en un negocio.
* **Cómo:** 
	* Dividir el programa en 3 módulos:
		* productos
		* menu
		* principal
	* **Módulo productos:**
		se definen:
		* **regProducto(valorDato, nombreDato, tipoDato) :** recibe el valor del dato, el nombre del dato y el tipo de dato correspondiente al producto y si el dato digitado es correcto, sale de la función. Si el dato digitado se trata del código del producto, se verifica que el código digitado no pertenezca a ningún producto.
		* **mostrarInventario() :** imprime una tabla con los datos registrados de cada producto en el inventario.
		* **buscarProducto(codigoProducto) :** recibe el código del producto digitado por el usuario y lo busca dentro de la lista que almacena todas las listas de los productos. Si encuentra el código del producto, define el índice de la lista. Si no lo encuentra, devuelve un índice = -1.
		* **actStock() :** solicita el valor del stock que se desea añadir o restar a un producto en específico y, si el valor digitado es correcto y el cálculo del nuevo stock no es menor a 0, se actualiza el valor del stock.
		* **imprimeInforme() :** imprime una tabla con los datos registrados de cada producto cuyo stock actual se encuentra por debajo del stock mínimo.
		* **calGanancia() :** realiza la diferencia entre el valor de venta y valor de compra, multiplicado por el stock actual de cada producto, e imprime el valor resultante.
	* **Módulo menu:**
		se define:
		* **menuShow() :** repite la impresión del menú mientras el dato ingresado no corresponda al tipo definido.
	* **Módulo principal:**
		* Haciendo uso de un **while** y un **try-except**, se muestra el menú de opciones.
		* Dependiendo de la opción que digite el usuario, se llaman a las funciones creadas en los distintos módulos.

* **Variables:**

| Variable   |      E/S      |  Tipo de Dato |
|----------|:-------------:|------:|
| opMenu| E |    int |
| codigo| E | str|
| nombre| E | str|
| valorCompra| E | float|
| valorVenta| E | float|
| stockMin| E | int|
| stockMax| E | int|
| stockActual| E | int|
| nombreProveedor| E | str|
| valorDato | E |    str|
| stock | E |    int|
| productos| S |    list|
| registroProducto| S |    list|
| suma| S |    int|

En el directorio [03_intermedio](https://github.com/lipaocaspi/J1_navidad_python/tree/main/03_intermedio) se encuentra el código con sus respectivos módulos.

## Ejercicio Avanzado
#### 1. Análisis:
* **Problema:** llevar el registro de los jugadores y los partidos de un torneo de tenis de mesa en Campus.
* **Cómo:** 
	* Dividir el programa en 5 módulos:
		* categorias
		* jugadores
		* menus
  		* partidos
		* principal
	* **Módulo categorias:**
		se define:
		* **defCategoria(categoriaJ) :** recibe un número del 1 al 3. Dependiendo del valor, se asigna el nombre de la categoría.
   	* **Módulo jugadores:**
		se definen:
		* **verificarEdad() :** verifica que la edad ingresada por el usuario sea un número entero.
  		* **buscarId(codJugador, jugadores) :** recibe el código del jugador y el diccionario que contiene a los jugadores. Busca el código dentro del diccionario indicado, y si lo encuentra, extrae el valor del Id del jugador.
   	  	* **regJugador(categoriaJugador, edadJugador, jugadores) :** recibe la categoría del jugador, la edad del jugador y el diccionario que contiene a los jugadores. Solicita el id y el nombre del jugador, verificando que los datos digitados sean diferentes a "". En el caso del id, verifica que no exista un jugador con el id digitado. Se define la categoría con la función **defCategoria(categoriaJ)** y se crea el diccionario del jugador.
  		* **buscarJugador(codJugador, jugadores) :** recibe el código del jugador y el diccionario que contiene a los jugadores. Busca el código dentro del diccionario indicado, y si lo encuentra, extrae el valor del Id del jugador. Si no lo encuentra, imprime un mensaje al usuario.
   	  	* **actualizarJugador(codJugador, jugadores, puntosA, partidosG, partidosP, totalP) :** recibe el código del jugador, el diccionario que contiene a los jugadores, los puntos a favor, los partidos ganados, los partidos perdidos y el total de puntos. Busca el diccionario con el código recibido, extrae los valores correspondientes y le agrega los datos recibidos. Por último, actualiza el diccionario con la nueva información.
  		* **mostrarTabla(jugadores) :** recibe el diccionario e imprime su contenido organizado en una tabla.
   	  	* **mostrarGanador(jugadores) :** recibe el diccionario y compara el valor correspondiente a los puntos totales de cada jugador para encontrar el mayor de ellos. Si existen varios jugadores con el mismo puntaje total, se compara el valor del los puntos a favor. Por último, se imprime el nombre del ganador.
  	* **Módulo partidos:**
  	  	se definen:
  	  	* **verificarTipo(valorDato, nombreDato, tipoDato) :** recibe el valor del dato, el nombre del dato y el tipo de dato correspondiente al set y si el dato digitado es correcto, sale de la función.
  		* **verificarPartido(id1, id2, partidos) :** recibe el valor del id del jugador 1, id del jugador 2 y el diccionario donde se encuentran guardados los partidos. Verifica que el partido que el usuario está tratando de registrar no se haya registrado anteriormente.
  		* **regPartidos(categoria) :** recibe el número correspondiente a la categoría. Solicita los ids de los dos jugadores que se enfrentaron, verifica que los jugadores se encuentren registrados y que el partido no se haya registrado aún. Solicita el ingreso de los puntos realizados por cada jugador en cada set, realiza los respectivos cálculos y define el ganador del partido. Actualiza el registro de los jugadores y crea el diccionario del partido.
  		* **calNumPartidos(numJugadores) :** recibe el número de jugadores que existen en la categoría y calcula el número de partidos que se deben jugar para poder finalizar el torneo: $\frac{numJugadores!}{jugadoresPorPartido! * (numJugadores - jugadoresPorPartido)!}$
   	* **Módulo menus:**
		se definen:
		* **menuPrincipal() :** repite la impresión del menú principal mientras el dato ingresado no corresponda al tipo definido.
  		* **menuRegistroJ() :** repite la impresión del menú mientras el dato ingresado no corresponda al tipo definido. Dependiendo de la opción que digite el usuario, se llaman a las funciones creadas en los distintos módulos, teniendo en cuenta la edad del jugador y si el torneo ya ha comenzado.
  		* **menuRegistroP() :** repite la impresión del menú mientras el dato ingresado no corresponda al tipo definido. Dependiendo de la opción que digite el usuario, se llaman a las funciones creadas en los distintos módulos, teniendo en cuenta el número de jugadores registrados y si un partido en específico ya ha sido registrado.
   	  	* **menuTablas() :** repite la impresión del menú mientras el dato ingresado no corresponda al tipo definido. Dependiendo de la opción que digite el usuario, se muestra la tabla de puntajes correspondiente a la categoría.
  		* **menuGanadores() :** repite la impresión del menú mientras el dato ingresado no corresponda al tipo definido. Dependiendo de la opción que digite el usuario, se llaman a las funciones creadas en los distintos módulos, teniendo en cuenta el número de jugadores registrados y si ya se registraron todos los partidos del torneo.
	* **Módulo principal:**
		* Haciendo uso de un **while** y un **try-except**, se muestra el menú principal.
		* Dependiendo de la opción que digite el usuario, se llaman a las funciones creadas en los distintos módulos.

* **Variables:**

| Variable   |      E/S      |  Tipo de Dato |
|----------|:-------------:|------:|
| opMenu| E |    int |
| id| E | str|
| nombre| E | str|
| edad| E | int|
| categoria| S | str|
| idJ1| E | str|
| idJ2| E | str|
| set1J1| E | int|
| set1J2| E | int|
| set2J1| E | int|
| set2J2| E | int|
| set3J1| E | int|
| set3J2| E | int|
| puntosJ1S1| S | int|
| puntosJ2S1| S | int|
| puntosJ1S2| S | int|
| puntosJ2S2| S | int|
| puntosJ1S3| S | int|
| puntosJ2S3| S | int|
| id1| S | str|
| id2| S | str|
| PJ| S | int|
| PG| S | int|
| PP| S | int|
| PA| S | int|
| TP| S | int|
| maxNombre| S | str|
| maxTP| S | int|
| maxPA| S | int|
| partido| S | dict|
| partidosNovatos| S | dict|
| partidosIntermedios| S | dict|
| partidosAvanzados| S | dict|
| jugadoresNovatos| S | dict|
| jugadoresIntermedios| S | dict|
| jugadoresAvanzados| S | dict|

En el directorio [01_avanzado](https://github.com/lipaocaspi/J1_navidad_python/tree/main/01_avanzado) se encuentra el código con sus respectivos módulos.
