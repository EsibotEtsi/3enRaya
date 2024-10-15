#Modulo necesario para el funcionamiento de la IAnt
import random



#Cadena de texto que sirve como un pequeño y cutre menu ASCII para el juego
wellcomeImage = """\n\nX    X\t OOOO \tX    X
 X  X \tOO  OO\t X  X 
  XX  \tO    O\t  XX  
 X  X \tOO  OO\t X  X 
X    X\t OOOO \tX    X

  EL UNICO Y ORIGINAL
      3 EN RAYA"""

#Cadena de texto que se usa para la seleccion del modo de juego
gameSelectionText = '''   1 Jugador: "1"
   2 Jugadores: "2"
   Salir: "exit"'''

#Sendas variables usadas como X y O del juego, puestas con el mero proposito de ahorrarme al maximo poner comillas
x = 'X'
o = 'O'

#Mensaje de error humoristico(aunque no tiene ni puta gracia la verdad) que NO DEBERIA de aparecer en la ejecucion
#   este solo sirve para el desarrollador para hacer pequeñas pruebas y comprobar las salidas o ubicar un error
genericErrorMsg = "\nNo se como te la has apañado, pero la has cagado, enhorabuena"



#Esta es la funcion de entrada del codigo, a partir de esta se llama a las otras
# Se ejecuta por separado de GameSelection ya que esta inprime el texto de 
# bienvenida y este no se ha de poner cada vez que se inicia un nuevo juego
# sino cuando se ejecuta por primera vez el programa
def homecoming():
    print(f'{wellcomeImage}\n')
    gameSelection()

#Esta funcion se encarga de imprimir por pantalla las opciones de juego
# y escanear la respuesta del usuario para a posteriori empezar con el
# juego, o salir del programa
def gameSelection():
    gameMode = "exit"
    print(f'Opciones:\n{gameSelectionText}')
    gameMode = input("Introduzca el numero de jugadores: ")
    if gameMode != "1" and gameMode != "2" and gameMode != "exit":
        print("\nEntrada erronea\n")
        gameSelection()
    elif(gameMode == "1"):
        autoPlayer(1)
    elif(gameMode == "2"):
        autoPlayer(2)
    elif(gameMode == "exit"):
        print("\nSaliendo del juego...")
        exit

#Esta funcion recibe como argumento el numero de jugadores que se ha seleccionado, y 
# en funcion de este, habilita la IA o no e inicia el orden de jugadores (jugador 1 o dos,
# IA o humano), y crea una lista en blanco que representa las casillas de juego
# A su vez, cuando se finaliza el bucle principal de juego, ejecuta un gestor de victoria
def autoPlayer(playerNumber):
    turnCount = 0 #Cuenta cuantos turnos llevan
    possitionList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    isIA = False #True significa que se juega contra la ia, false que es JcJ
    isMain = False #True significa que es turno del jugador principal, par1 1J el humano, y para 2J el jugador 1
    if playerNumber == 1:
        isIA = True
        isMain = True
        winnerMain = tileDrawer(possitionList,isIA, isMain, turnCount)
    else:
        isIA = False
        isMain = True
        winnerMain = tileDrawer(possitionList, isIA, isMain, turnCount)
    winnerManager(winnerMain, isIA, possitionList)

#Esta funcion es la que se encarga de poner el mensaje de victoria e imprimir
# por pantalla el estado final del tablero, asi como poner la opcion de
# jugar otra vez o salir del programa. Toma como parametros si ha ganado
# el jugador principal de la sesion(J1 o el humano(contra la IA)), si
# era juego contra la IA y la lista que representa el estado del tablero
def winnerManager(winnerMain, isIA, possitionList):
    a, b, c, d, e, f, g, h, i = possitionList
    print(f"\n#############\n# {a} | {b} | {c} #\n#-----------#\n# {d} | {e} | {f} #\n#-----------#\n# {g} | {h} | {i} #\n#############\n")
    if winnerMain == -1:
        print(f"¡¡¡EMPATE!!!")
    elif winnerMain == 0:
        if isIA == True:
            print("\t¡¡VICTORIA DE LA IA!!\n\nIllo, en verdad me joderia que unos numeros random me ganasen\n  jeje paquete")
        elif isIA == False:
            print("\t¡¡VICTORIA DE LAS O!!\n\nEl jugador 2 ha ganado\nEspero que J1 no se haya apostado nada")
        else:
            print(genericErrorMsg, "0")
    elif winnerMain == 1:
        if isIA == True:
            print("\t¡¡VICTORIA DEL JUGADOR!!\n\nAsi es, demuestrale a un cacho de metal quien manda")
        elif isIA == False:
            print("\t¡¡VICTORIA DE LAS X!!\n\nEl jugador 1 ha ganado")
        else:
            print(genericErrorMsg, "1")
    else:
        print(genericErrorMsg, "2")
    print("\n¿Pega una revanchita o algo no?")
    retry = input("s/n: ")
    if retry == 's':
            gameSelection()
            exit
    if retry == 'n':
            print("\nSaliendo del juego...")
            exit

#Esta funcion es parte fundamental del bucle de juego,
# imprime por pantalla a quien le toca el siguiente turno y el 
# estado actual del tablero. Cuando acaba de imprimir los datos
# necesarios llama a la otra parte del bucle para seguir el juego
# Toma como parametros cuantos turnos se lleva jugando, si es contra 
# la IA, si es el jugador principal quien juega, y el estado del tablero
def tileDrawer(possitionList, isIA, isMain, turnCount):
    if isIA == True:
        if isMain == True:
            print(f"\nSu turno:")
        elif isMain == False:
            print(f"\nTurno de la IA")
        else:
            print(genericErrorMsg, "3")
    elif isIA == False:
        if isMain == True:
            print(f"\nTurno del jugador 1 (X)")
        elif isMain == False:
            print(f"\nTurno del jugador 2 (O)")
        else:
            print(genericErrorMsg, "4")
    else:
        print(genericErrorMsg, "5")
    a, b, c, d, e, f, g, h, i = possitionList
    print(f" {a} | {b} | {c}\n-----------\n {d} | {e} | {f}\n-----------\n {g} | {h} | {i}\n")
    winnerMain = loopGestor(possitionList, isIA, isMain, turnCount)
    return(winnerMain)

#Es la parte mas importante del bucle, gestiona el orden de juego, modifica
# los datos necesarios para que se lleve bien las cuentas de las rondas y los
# turnos. Ademas gestiona las llamadas a las funciones auxiliares
# Toma como parametros cuantos turnos se lleva jugando, si es contra 
# la IA, si es el jugador principal quien juega, y el estado del tablero
def loopGestor(possitionList, isIA, isMain, turnCount):
    if isIA == True:
        if isMain == True: #1P IA
            tileChecker(possitionList, isMain)
            isMain = False
            turnCount += 1
            print(f"Turno {turnCount}")
            hasWon = winCheck(possitionList, turnCount)
            if  hasWon== 2: #No se ha acabado la partida
                return(tileDrawer(possitionList, isIA, isMain, turnCount))
            elif hasWon == -1: #Empate
                return(-1)
            elif hasWon == 0:
                return(0)
            elif hasWon == 1:
                return(1)
        else: #1P IA
            autoIAnt(possitionList)
            isMain = True
            turnCount += 1
            hasWon = winCheck(possitionList, turnCount)
            if hasWon == 2: #No se ha acabado la partida
                return(tileDrawer(possitionList, isIA, isMain, turnCount))
            elif hasWon == -1: #Empate
                return(-1)
            elif hasWon == 0:
                return(1)
            elif hasWon == 1:
                return(0)
    else:
        if isMain == True: #2P J1
            tileChecker(possitionList, isMain)
            isMain = False
            turnCount += 1
            print(f"Turno {turnCount}")
            hasWon = winCheck(possitionList, turnCount)
            if  hasWon == 2: #No se ha acabado la partida
                return(tileDrawer(possitionList, isIA, isMain, turnCount))
            elif hasWon == -1: #Empate
                return(-1)
            elif hasWon == 0:
                return(0)
            elif hasWon == 1:
                return(1)
        else: #2P J2
            tileChecker(possitionList, isMain)
            isMain = True
            turnCount += 1
            print(f"Turno {turnCount}")
            hasWon = winCheck(possitionList, turnCount)
            if  hasWon== 2: #No se ha acabado la partida
                return(tileDrawer(possitionList, isIA, isMain, turnCount))
            elif hasWon == -1: #Empate
                return(-1)
            elif hasWon == 0:
                return(1)
            elif hasWon == 1:
                return(0)

#Esta es la funcion que gestiona el turno de la IAnt(Se llama IAnt porque de
# inteligente no tiene nada). Toma como parametro la lista que contiene el 
# estado de las casillas de juego, ve cuales estan libre (sin X u O) y de
# forma aleatoria selecciona una y la marca (Siempre es el J2, asi que 
# con O)
def autoIAnt(possitionList):
    availableList = []
    for tile in possitionList:
        if tile != o and tile != x:
            availableList.append(tile)
    randomEl = random.choice(availableList)
    elIndex = possitionList.index(randomEl)
    possitionList[elIndex] = o

#Esta funcion es la que se llama cada vez que un usuario ha de modificar la
# la lista del tablero, y utilizando la recursividad se asegura de que se
# introduzca una entrada valida
# toma como parametros el estado de la lista y si el jugador es el principal
# para saber si colocar una X o una O
def tileChecker(possitionList, isMain):
    if isMain == True:
        tileSelection = int(input("Seleccione la casilla en la que jugar (X): "))
        if tileSelection <= 0 or tileSelection >= 10:
            print("El indice escogido esta fuera de la casilla, introduzca un numero valido (1-9)\n")
            tileChecker(possitionList, isMain)
            exit
        else:
            if possitionList[tileSelection -1] == x or possitionList[tileSelection -1] == o:
                print("El indice escogido ya está ocupado\n")
                tileChecker(possitionList, isMain)
                exit
            else:
                possitionList[tileSelection -1] = x
                exit
    else:
        tileSelection = int(input("Seleccione la casilla en la que jugar (o): "))
        if tileSelection <= 0 or tileSelection >= 10:
            print("El indice escogido esta fuera de la casilla, introduzca un numero valido (1-9)\n")
            tileChecker(possitionList, isMain)
            exit
        else:
            if possitionList[tileSelection -1] == x or possitionList[tileSelection -1] == o:
                print("El indice escogido ya está ocupado\n")
                tileChecker(possitionList, isMain)
                exit
            else:
                possitionList[tileSelection -1] = o
                exit

#Esta funcion comprueba el estado de la partida, si se ha conseguido hacer
# un tres en raya(comparando con los 8 posibles resultados de 3 en raya), 
# si se ha llegado a los 9 turnos(eso de inventarnos tablero sobre la marcha como que no), 
# y si no ha ocurrido nada de esto y se debe de seguir jugando con normalidad
def winCheck(possitionList, turnCount):
    winnerMain = 2
    if turnCount >= 5:
        a, b, c, d, e, f, g, h, i = possitionList
        if a == b == c:
            if a == x:
                winnerMain = 1
            else:
                winnerMain = 0
        elif a == d == g:
            if a == x:
                winnerMain = 1
            else:
                winnerMain = 0
        elif g == h == i:
            if a == x:
                winnerMain = 1
            else:
                winnerMain = 0
        elif c == f == i:
            if a == x:
                winnerMain = 1
            else:
                winnerMain = 0
        elif a == e == i:
            if a == x:
                winnerMain = 1
            else:
                winnerMain = 0
        elif b == e == h:
            if a == x:
                winnerMain = 1
            else:
                winnerMain = 0
        elif c == e == g:
            if a == x:
                winnerMain = 1
            else:
                winnerMain = 0
        elif d == e == f:
            if a == x:
                winnerMain = 1
            else:
                winnerMain = 0
        elif turnCount >= 9:
            winnerMain = -1
    return winnerMain



#Llama a la funcion homonima para iniciar el codigo
homecoming()