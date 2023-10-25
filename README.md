# IA-REVERSI
#Integrantes# #Diego Pizarro   19.639.215-7  nrc:6909 #Diego Troncoso  20.462.209-8  nrc:6908 #Matías Riveros  20.676.480-5  nrc:6908 #Jorge Sandoval  20.214.231-1  nrc:6908

I. Objetivo.
El objetivo de este proyecto es evaluar su capacidad para:
- Aplicar técnicas de búsqueda y razonamiento en juegos.
- Diseñar sistemas computacionales basados en agentes inteligentes.
- Implementar sistemas inteligentes orientados a resolver problemas reales.
II. Enunciado.
En este proyecto deberás implementar un agente para el juego Reversi 6x6
(https://en.wikipedia.org/wiki/Reversi). Este juego se realiza sobre un tablero de 6 filas y 6
columnas con fichas de dos colores (blanco y negro, generalmente). Un ejemplo de posición
de inicio se puede ver en la figura 1:

![image](https://github.com/jsandovalsantibez/IA-REVERSI/assets/111337634/ab52e772-3dc1-44c3-a2e9-72099fc5c1ab)

En la figura 1, aparecen marcadas con una x las posiciones en donde puede jugar el jugador
negro. Una jugada válida es aquella que “salta” sobre fichas de color contrario al del
jugador y cae en un espacio vacío adyacente a la última ficha saltada, como en el ejemplo
mostrado en la figura 2. Todas las fichas que se han saltado cambian de color.

![image](https://github.com/jsandovalsantibez/IA-REVERSI/assets/111337634/c3375d34-25f9-498f-9b0d-f6c1bb71c181)

Para jugar una versión en línea de este juego, pueden consultar el siguiente link:
https://www.mathsisfun.com/games/reversi-small.html.
Tu juego debe:
1. Permitir escoger el tamaño del tablero (6x6 u 8x8).
2. Permitir escoger el nivel de dificultad, entre al menos tres niveles.
3. Registrar e imprimir el número de nodos explorados y el tiempo utilizado durante la
selección de la jugada que realizará la computadora.
4. Poseer una interfaz que sea de fácil uso, que permita ver el estado del juego en forma
clara y seleccionar una jugada sin inducir a errores.
5. Debes agregar a tu juego una característica adicional, que puedes escoger entre:
a. Sugerir una jugada al jugador humano si es que lo pide.
b. Ajustar el nivel de dificultad de acuerdo a la habilidad del jugador, recordando
partidas anteriores.


