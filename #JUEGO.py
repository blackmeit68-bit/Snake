#JUEGO

print("SNAKE")

x = 5
y = 5

comida_x = 8
comida_y = 3

jugando = True

while jugando:

    # Mostrar posiciones
    print("Posicion de la serpiente:")
    print("x =", x)
    print("y =", y)

    print("Comida en:", comida_x, ",", comida_y)

    # Pedir una direccion
    direccion = input("Mover (W=Arriba, S=Abajo, A=Izquierda, D=Derecha, X=Salir): ")

    # Mover a la serpiente
    if direccion == "W" or direccion == "w":
        y = y - 1

    elif direccion == "S" or direccion == "s":
        y = y + 1

    elif direccion == "A" or direccion == "a":
        x = x - 1

    elif direccion == "D" or direccion == "d":
        x = x + 1

    elif direccion == "X" or direccion == "x":
        print("EFE")
        jugando = False

    else:
        print("PA DONDE ?")

    # Verificar si comió
    if x == comida_x and y == comida_y:
        print("MMM YOMMY")

        # Nueva posicion de la comida
        comida_x = comida_x + 2
        comida_y = comida_y + 1

    # Verificar si coliciono
    if x < 0 or y < 0:
        print("AUCHHH")
        jugando = False
