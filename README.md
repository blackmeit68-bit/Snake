# Snake

AUTONOMO N3

El código del juego Snake consiste de una serpiente que se mueve dentro de una pantalla en este caso aun no tengo conocimientos para recrearlo con imágenes pero también es divertido ver lo que hace mediante textos, come comida, ete programa utiliza bucles, condicionales y variables para controlar el movimiento y las reglas del juego, despues se crea un bucle principal (while), que es el encargado de mantener el juego funcionando continuamente, dentro de este bucle se detectan las teclas que presiona el usuario para cambiar la dirección de la serpiente.
La serpiente se mueve cambiando su posición, también se genera comida en posiciones aleatorias como mencione toda esa informacio se muestra en texto, y cuando la serpiente toca la comida, aumenta su tamaño y la puntuación del jugador
Finalmente, el programa verifica si la serpiente choca contra los bordes o contra sí misma. Si esto ocurre, el juego termina y se muestra un mensaje de fin del juego

Mi codigo integra lo siguiente
print = muestra el nombre del juego
posicion inicial de la serpiente con variables, de igual manera la comida = (X) horizontal, (Y) vertical
Esta variable mantiene el juego funcionando hasta perder,( jugando = True ) este es el que hace funcionar el comando while
Mientras la variable jugando sea verdadero el juego muestra todo en texto, muestra posicion, pide una direccion, verifica si la serpiente coliciono & mueve a la serpiente imaginaria jaja
Importante mostrar en todo momento la posicion de la serpiente con, print("Posicion de la serpiente:") 
Con este codigo movemos a la serpiente, creamos una variable donde pedimos datos de parte del jugador, direccion = input("Mover (W=Arriba, S=Abajo, A=Izquierda, D=Derecha, X=Salir): ")
& con este codigo nos movemos, if direccion == "W" or direccion == "w":
                                                y = y - 1 (recorremos menos uno)
                                                
Si el jugador escribe otra letra en vvez de las designadas utilize este codigo. else:
                                                                                 print("PA DONDE ?")                                                

La comida tambien tiene una posicion & con este codigo detecta colicion con la comida & muestra un mensaje: if x == comida_x and y == comida_y:
                                                                                                                  print("MMM YOMMY")

Este codigo verifica si colicionó & la variable jugando pasa a ser falso terminando el bucle & terminando el juego, if x < 0 or y < 0:
                                                                                                                       print("AUCHHH")
                                                                                                                       jugando = False

Por el momento el codigo al ejecutarse tiene bugs, como por ejemplo no colicionar e irse muy lejos hasta el infinito xd 
