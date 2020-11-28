# estadisticas-de-inversiones
El programa realizado tiene dos funciones.
- 1 - Agregar datos a un archivo csv para llevar el control de las inversiones realizadas
- 2 - Consultar esos datos y ver las estadisticas generales o por liga segun desee

Recomendaciones para la introduccion de datos:
- 1 - Para seguir un orden se debe iniciar cada palabra con mayuscula y luego minuscula, cuando el nombre de un equipo tenga varias palabras se debe iniciar siempre con         mayusculas
- 2 - la variable "RESULTADO" se debe completar con "W" si la inversion dio ganancias y con "L" si la inversion dio perdidas 
- 3 - La variable "INVERSION" se debe completar con un "NUMERO ENTERO" sino el programa dara ERROR
- 4 - Las variables  "CUOTA" y "GANANCIA" se deben completar con "NUMEROS ENTEROS O DECIMALES" sino el programa dara ERROR

Ejemplo de como cargar datos
- mes : Noviembre
- liga : España
- local : Villarreal
- visitante : Valencia
- linea : 1.5 (las inversiones son a total de corners, ahi estoy indicando que la linea es + 1.5 corners)
- inversion : 2 (es el capital a invertir)
- cuota : 1.9
- resultado : W
- ganancias : 1.8

La funcion de consultar estadisticas tine dos partes:
- 1 - Consultar las estadisticas generales
- 2 - Consultar las estadisticas por ligas ingresando por comando las ligas deseada respentando mayusculas y minusculas
