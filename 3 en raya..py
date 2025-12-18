#    1   2   3                              DIFERENTES TIPOS DE VICTORIA
#1 |-#-|-#-|-#-|        |-G-|-#-|-#-|     |-#-|-#-|-G-|     |-G-|-#-|-#-|        |-G-|-G-|-G-|

#2 |-#-|-#-|-#-|        |-#-|-G-|-#-|     |-#-|-G-|-#-|     |-G-|-#-|-#-|        |-#-|-#-|-#-|

#3 |-#-|-#-|-#-|        |-#-|-#-|-G-|     |-G-|-#-|-#-|     |-G-|-#-|-#-|        |-#-|-#-|-#-|
#                            VICTORIA ESQUINERA           VICTORIA VERTICAL    VICTORIA HORIZONTAL
#                           DESDE AMBAS ESQUINAS        EN LAS TRES COLUMNAS    EN LAS TRES FILAS

def info():
    print("--------------------------------------------------------------------------------")
    print("""Bienvenido a 3 en raya, el juego consta de 3 columnas por 3 filas que terminan
conformando un total de 9 celdas. En la mitad de cada una de las celdas se
puede observar un simbolo "#". Para jugar se necesita de 2 personas,
cada una tendra su turno para cambiar el simbolo # por uno de su preferencia,
puede ser "X" o "0", al conseguir un 3 en raya conformado por los simbolos
de uno de los dos jugadores se ganara el juego.
A la hora de escoger la celda en la que se quiere ingresar su simbolo debe
tener en cuenta que existen numeros de filas y de columnas, la manera de
seleccionar una celda en concreto es de la forma: numero de fila numero de columna
(12) de esta manera se cambiara la celda en la posicion 1,2 ejemplo:
#    1   2   3
#1 |-#-|-X-|-#-|

#2 |-#-|-#-|-#-|

#3 |-#-|-#-|-#-|

¡Suerte!
""")
    print("---------------------------------------------------------------------------------")

def victoria():
    print("""                       DIFERENTES TIPOS DE VICTORIA
|-G-|-#-|-#-|     |-#-|-#-|-G-|     |-G-|-#-|-#-|         |-G-|-G-|-G-|
|-#-|-G-|-#-|     |-#-|-G-|-#-|     |-G-|-#-|-#-|         |-#-|-#-|-#-|
|-#-|-#-|-G-|     |-G-|-#-|-#-|     |-G-|-#-|-#-|         |-#-|-#-|-#-|
     VICTORIA ESQUINERA           VICTORIA VERTICAL     VICTORIA HORIZONTAL
    DESDE AMBAS ESQUINAS        EN LAS TRES COLUMNAS     EN LAS TRES FILAS

--------------------------------------------------------------------------------------------
""")

def visualizar(matriz):
    cont = 0
    fila = 1
    print("     1     2     3")
    for i in range(0, len(matriz)):
        print(fila, end=" ")
        fila += 1
        for j in range(0, len(matriz)):
            if cont >= 1:
                print("-",matriz[i][j],"-|", end="")
            if cont == 0:
                print("|-",matriz[i][j],"-|", end="")
                cont = cont + 1
        cont = 0
        print()

def indice(dato):
    if dato < 3:
        if dato < 2:
            indice = 0
        else:
            indice = 1
    else:
        indice = 2


    return indice

def validar_empate(matriz):
    cont = 0
    for i in range(0, len(matriz)):
        for j in range(0, len(matriz)):
            if matriz[i][j] == "#":
                cont = cont + 1

    if cont == 0:
        return True
    else:
        return False


#Hay 8 formas posibles de ganar en 3 en raya, en esta funcion se valida cada una de ellas.
#Si en verdad se da la victoria se retorna True, en caso contrario False

def ganador(matriz):
    #VICTORIA HORIZONTAL
    veredicto = False
    for i in range(0, len(matriz)):
        cont = 0
        skin = "f"
        for j in range(0, len(matriz)):
            if j == 0:
                if matriz[i][j] != "#":
                    skin = matriz[i][j]
                    cont = cont + 1
            else:
                if matriz[i][j] == skin:
                    cont = cont + 1
                if cont == 3:
                    veredicto = True

    #VICTORIA VERTICAL

    for i in range(0,len(matriz)):
        cont = 0
        skin = "f"
        for j in range(0,len(matriz)):
            if j == 0:
                if matriz[j][i] != "#":
                    skin = matriz[j][i]
                    cont = cont + 1

            if matriz[j][i] == skin and j != 0:
                cont = cont + 1

        if cont == 3:
            veredicto = True


    #VICTORIA POR ESQUINAS
    #ESQUINA #1
    #LA QUE SE FORMA DE ESTA MANERA: \
    skin = "f"
    cont = 0
    for i in range(0, len(matriz)):
        if i == 0:
            if matriz[i][i] != "#":
                skin = matriz[i][i]
                cont = cont + 1
        else:
            if matriz[i][i] == skin:
                cont = cont + 1

        if cont == 3:
            veredicto = True

    #VICTORIA POR ESQUINAS
    #ESQUINA #2
    #LA QUE SE FORMA DE ESTA MANERA: /
    skin = "f"
    cont = 0
    if matriz[2][0] != "#":
        skin = matriz[2][0]
        cont = cont + 1
    if matriz[1][1] == skin:
        cont = cont + 1
    if matriz[0][2] == skin:
        cont = cont + 1


    if cont == 3:
        veredicto = True



    return veredicto



def juego(matriz):
    finalizacion = False
    player = 1
    simbolo = "X"
    while finalizacion == False:
        bandera = False

        print(f"Jugador {player}")
        movimiento = int(input("¿Que movimiento desea realizar? (numfilanumcolumna) >"))

        if movimiento < 10:
            bandera = True

        if movimiento > 33:
            bandera = True

        if bandera == False:
            fila = movimiento // 10
            columna = movimiento % 10
            #Necesitamos determinar el indice tanto de la fila como de la columna en nuestra matriz
            #Para no sobre cargar esta funcion de codigo realizare una nueva que automatice este preceso
            fila = indice(fila)
            columna = indice(columna)


            if matriz[fila][columna] == "#":
                matriz[fila][columna] = simbolo
                finalizacion = ganador(matriz)

                empate = validar_empate(matriz)

                if empate == True:
                    print("¡Es un empate! ")
                    visualizar(matriz)
                    finalizacion = True
                else:
                    if finalizacion == True:
                        print(f"Felicidades jugador {player} Tu ganas.")
                        visualizar(matriz)
                    else:
                        if player == 1:
                            player = 2
                            simbolo = "0"
                            visualizar(matriz)
                        else:
                            player = 1
                            simbolo = "X"
                            visualizar(matriz)


            else:
                print("Movimiento no valido. ")

        else:
            print("Se ingreso una casilla no valida, deben ingresar dos numeros en la forma (filacolumna). ")





def menu():
    opc = 0
    while opc != 4:
        matriz = [["#","#","#"],["#","#","#"],["#","#","#"]]
        print("""¡Bienvenido a 3 en raya!
1.Jugar.
2.¿Como jugar?
3.¿Como se gana?
4.Salir del juego.""")
        print("---------------------------------------------------------------------------------")
        opc = int(input("¿Que desea hacer? "))
        if opc == 1:
            visualizar(matriz)
            juego(matriz)
        if opc == 2:
            info()
        if opc == 3:
            victoria()

menu()
