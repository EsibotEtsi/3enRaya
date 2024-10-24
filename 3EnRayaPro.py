#Modulo necesario para el funcionamiento de la IAnt
import random
import copy
from colorama import init, Fore


#Cadena de texto que sirve como un pequeño y cutre menu ASCII para el juego
wellcomeImage = f"""\n\n{Fore.BLUE}X    X{Fore.RESET}\t {Fore.RED}OOOO{Fore.RESET} \t{Fore.BLUE}X    X
 X  X {Fore.RESET}\t{Fore.RED}OO  OO{Fore.RESET}\t{Fore.BLUE} X  X 
  XX  {Fore.RESET}\t{Fore.RED}O    O{Fore.RESET}\t{Fore.BLUE}  XX  
 X  X {Fore.RESET}\t{Fore.RED}OO  OO{Fore.RESET}\t{Fore.BLUE} X  X 
X    X{Fore.RESET}\t {Fore.RED}OOOO {Fore.RESET}\t{Fore.BLUE}X    X{Fore.RESET}

  {Fore.YELLOW}EL UNICO Y ORIGINAL
      3 EN RAYA{Fore.RESET}"""

#Cadena de texto que se usa para la seleccion del modo de juego
gameSelectionText = '''   1 Jugador: "1"
   2 Jugadores: "2"
   Salir: "exit"'''

#Sendas variables usadas como X y O del juego, puestas con el mero proposito de ahorrarme al maximo poner comillas
x = f"{Fore.BLUE}X{Fore.RESET}"
o = f"{Fore.RED}O{Fore.RESET}"

xWin = f"{Fore.GREEN}X{Fore.RESET}"
oWin = f"{Fore.GREEN}O{Fore.RESET}"

#Mensaje de error humoristico(aunque no tiene ni puta gracia la verdad) que NO DEBERIA de aparecer en la ejecucion
#   este solo sirve para el desarrollador para hacer pequeñas pruebas y comprobar las salidas o ubicar un error
genericErrorMsg = "\nNo se como te la has apañado, pero la has cagado, enhorabuena"



init()

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
def winnerManager(winnerMain, isIA, possitionListIN):
    possitionList = winColorCheck(possitionListIN)
    a, b, c, d, e, f, g, h, i = possitionList
    print(f"\n{Fore.LIGHTYELLOW_EX}#############\n#{Fore.RESET} {a} {Fore.LIGHTYELLOW_EX}|{Fore.RESET} {b} {Fore.LIGHTYELLOW_EX}|{Fore.RESET} {c} {Fore.LIGHTYELLOW_EX}#\n#-----------#\n#{Fore.RESET} {d} {Fore.LIGHTYELLOW_EX}|{Fore.RESET} {e} {Fore.LIGHTYELLOW_EX}|{Fore.RESET} {f} {Fore.LIGHTYELLOW_EX}#\n#-----------#\n#{Fore.RESET} {g} {Fore.LIGHTYELLOW_EX}|{Fore.RESET} {h} {Fore.LIGHTYELLOW_EX}|{Fore.RESET} {i} {Fore.LIGHTYELLOW_EX}#\n#############\n{Fore.RESET}")
    if winnerMain == -1:
        print(f"{Fore.LIGHTMAGENTA_EX}¡¡¡EMPATE!!!{Fore.RESET}")
    elif winnerMain == 0:
        if isIA == True:
            print(f"\t{Fore.RED}¡¡VICTORIA DE LA IA!!{Fore.RESET}\n\nIllo, en verdad me joderia que unos numeros random me ganasen\n  jeje paquete")
        elif isIA == False:
            print(f"\t{Fore.GREEN}¡¡VICTORIA DE LAS{Fore.RESET} {Fore.RED}O{Fore.RESET}{Fore.GREEN}!!{Fore.RESET}\n\nEl jugador 2 ha ganado\nEspero que J1 no se haya apostado nada")
        else:
            print(genericErrorMsg, "0")
    elif winnerMain == 1:
        if isIA == True:
            print(f"\t{Fore.GREEN}¡¡VICTORIA DEL JUGADOR!!{Fore.RESET}\n\nAsi es, demuestrale a un cacho de metal quien manda")
        elif isIA == False:
            print(f"\t{Fore.GREEN}¡¡VICTORIA DE LAS{Fore.RESET} {Fore.BLUE}X{Fore.RESET}{Fore.GREEN}!!{Fore.RESET}\n\nEl jugador 1 ha ganado")
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

#Efectivamente, por flojo y no reestructurar el codigo he metido una nueva funcion (como si no hubiera ya)
# Basicamente recomprueba las posiciones en las que se ha ganado, y cambia el color de azul a rojo, a verde
# en esas casillas unicamente
def winColorCheck(possitionList):
    a, b, c, d, e, f, g, h, i = possitionList
    if a == b == c:
        if a == x:
            a = xWin
            b = xWin
            c = xWin
        else:
            winnerMain = 0
            a = oWin
            b = oWin
            c = oWin
    elif a == d == g:
        if a == x:
            a = xWin
            d = xWin
            g = xWin
        else:
            a = oWin
            d = oWin
            g = oWin
    elif g == h == i:
        if g == x:
            g = xWin
            h = xWin
            i = xWin
        else:
            g = oWin
            h = oWin
            i = oWin
    elif c == f == i:
        if c == x:
            c = xWin
            f = xWin
            i = xWin
        else:
            c = oWin
            f = oWin
            i = oWin
    elif a == e == i:
        if a == x:
            a = xWin
            e = xWin
            i = xWin
        else:
            a = oWin
            e = oWin
            i = oWin
    elif b == e == h:
        if b == x:
            b = xWin
            e = xWin
            h = xWin
        else:
            b = oWin
            e = oWin
            h = oWin
    elif c == e == g:
        if c == x:
            c = xWin
            e = xWin
            g = xWin
        else:
            c = oWin
            e = oWin
            g = oWin
    elif d == e == f:
        if d == x:
            d = xWin
            e = xWin
            f = xWin
        else:
            d = oWin
            e = oWin
            f = oWin
    newPossitionList = [a, b, c, d, e, f, g, h, i]
    return newPossitionList

#Esta funcion es parte fundamental del bucle de juego,
# imprime por pantalla a quien le toca el siguiente turno y el 
# estado actual del tablero. Cuando acaba de imprimir los datos
# necesarios llama a la otra parte del bucle para seguir el juego
# Toma como parametros cuantos turnos se lleva jugando, si es contra 
# la IA, si es el jugador principal quien juega, y el estado del tablero
def tileDrawer(possitionList, isIA, isMain, turnCount):
    if isIA == True:
        if isMain == True:
            print(f"\nTurno del {Fore.BLUE}jugador{Fore.RESET}:")
        elif isMain == False:
            print(f"\nTurno de la {Fore.RED}IA{Fore.RESET}")
        else:
            print(genericErrorMsg, "3")
    elif isIA == False:
        if isMain == True:
            print(f"\nTurno del {Fore.BLUE}jugador 1{Fore.RESET} ({x})")
        elif isMain == False:
            print(f"\nTurno del {Fore.RED}jugador 2{Fore.RESET} ({o})")
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
            autoIA(possitionList)
            isMain = True
            turnCount += 1
            hasWon = winCheck(possitionList, turnCount)
            if hasWon == 2: #No se ha acabado la partida
                return(tileDrawer(possitionList, isIA, isMain, turnCount))
            elif hasWon == -1: #Empate
                return(-1)
            elif hasWon == 0:
                return(0)
            elif hasWon == 1:
                return(1)
    else:
        if isMain == True: #2P J1
            tileChecker(possitionList, isMain)
            isMain = False
            turnCount += 1
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
            hasWon = winCheck(possitionList, turnCount)
            if  hasWon== 2: #No se ha acabado la partida
                return(tileDrawer(possitionList, isIA, isMain, turnCount))
            elif hasWon == -1: #Empate
                return(-1)
            elif hasWon == 0:
                return(0)
            elif hasWon == 1:
                return(1)

#Esta funcion es la que controla a la IA en su turno, despues de analizar las
# casillas optimas para x e y, en funcion de estas elige la siguiente posicion
def autoIA(possitionList):
    availableListIndex = []
    for tile in possitionList: #Este bucle for guarda en una lista las casillas disponibles
        if tile != o and tile != x:
            availableListIndex.append(possitionList.index(tile))
    xListIndex = []
    cont = 0
    for tile in possitionList: #Este bucle for guarda en una lista las casillas ocupadas por x
        if tile == x:
            xListIndex.append(cont)
        cont += 1
    oListIndex = []
    cont = 0
    for tile in possitionList: #Este bucle for guarda en una lista las casillas ocupadas por o
        if tile  == o:
            oListIndex.append(cont)
        cont += 1
    xListIndexBkUp = copy.deepcopy(xListIndex)
    oListIndexBkUp = copy.deepcopy(oListIndex)
    xPropossenTileIndex = optimunTileIndex(xListIndex, oListIndexBkUp)
    oPropossenTileIndex = optimunTileIndex(oListIndex, xListIndexBkUp)
    if xPropossenTileIndex == -1:
        if oPropossenTileIndex == -1:
            if 4 in availableListIndex:
                possitionList[4] = o
            else:
                randomEl = random.choice(availableListIndex)
                possitionList[randomEl] = o
        else:
            possitionList[oPropossenTileIndex] = o
    else:
        if oPropossenTileIndex == -1:
            possitionList[xPropossenTileIndex] = o
        else:
            possitionList[oPropossenTileIndex] = o

#Esta funcion es el nucleo de la IA, analiza el estado de la partida y completa los 
# patrones posibles para x e y, devolviendo la casilla optima o -1 si la casilla
# a escoger no evita directamente la victoria
def optimunTileIndex(contentList, vsListBkUp):
    chossenTileIndex = -1
    if 4 in contentList:
        if 0 in contentList:
            if 8 not in vsListBkUp:
                chossenTileIndex = 8
            else:
                contentList.remove(0)
                chossenTileIndex = optimunTileIndex(contentList, vsListBkUp)
        elif 8 in contentList:
            if 0 not in vsListBkUp:
                chossenTileIndex = 0
            else:
                contentList.remove(8)
                chossenTileIndex = optimunTileIndex(contentList, vsListBkUp)
        elif 1 in contentList:
            if 7 not in vsListBkUp:
                chossenTileIndex = 7
            else:
                contentList.remove(1)
                chossenTileIndex = optimunTileIndex(contentList, vsListBkUp)
        elif 7 in contentList:
            if 1 not in vsListBkUp:
                chossenTileIndex = 1
            else:
                contentList.remove(7)
                chossenTileIndex = optimunTileIndex(contentList, vsListBkUp)
        elif 2 in contentList:
            if 6 not in vsListBkUp:
                chossenTileIndex = 6
            else:
                contentList.remove(2)
                chossenTileIndex = optimunTileIndex(contentList, vsListBkUp)
        elif 6 in contentList:
            if 2 not in vsListBkUp:
                chossenTileIndex = 2
            else:
                contentList.remove(6)
                chossenTileIndex = optimunTileIndex(contentList, vsListBkUp)
        elif 3 in contentList:
            if 5 not in vsListBkUp:
                chossenTileIndex = 5
            else:
                contentList.remove(3)
                chossenTileIndex = optimunTileIndex(contentList, vsListBkUp)
        elif 5 in contentList:
            if 3 not in vsListBkUp:
                chossenTileIndex = 3
            else:
                contentList.remove(5)
                chossenTileIndex = optimunTileIndex(contentList, vsListBkUp)
    elif 0 in contentList:
        if 1 in contentList:
            if 2 not in vsListBkUp:
                chossenTileIndex = 2
            else:
                contentList.remove(1)
                chossenTileIndex = optimunTileIndex(contentList, vsListBkUp)
        elif 2 in contentList:
            if 1 not in vsListBkUp:
                chossenTileIndex = 1
            else:
                contentList.remove(2)
                chossenTileIndex = optimunTileIndex(contentList, vsListBkUp)
        elif 3 in contentList:
            if 6 not in vsListBkUp:
                chossenTileIndex = 6
            else:
                contentList.remove(3)
                chossenTileIndex = optimunTileIndex(contentList, vsListBkUp)
        elif 6 in contentList:
            if 3 not in vsListBkUp:
                chossenTileIndex = 3
            else:
                contentList.remove(6)
                chossenTileIndex = optimunTileIndex(contentList, vsListBkUp)
        elif 8 in contentList:
            if 4 not in vsListBkUp:
                chossenTileIndex = 4
            else:
                contentList.remove(8)
                chossenTileIndex = optimunTileIndex(contentList, vsListBkUp)
    elif 1 in contentList:
        if 2 in contentList:
            if 0 not in vsListBkUp:
                chossenTileIndex = 0
            else:
                contentList.remove(2)
                chossenTileIndex = optimunTileIndex(contentList, vsListBkUp)
        if 7 in contentList:
            if 4 not in vsListBkUp:
                chossenTileIndex = 4
            else:
                contentList.remove(7)
                chossenTileIndex = optimunTileIndex(contentList, vsListBkUp)
    elif 2 in contentList:
        if 6 in contentList:
            if 4 not in vsListBkUp:
                chossenTileIndex = 4
            else:
                contentList.remove(6)
                chossenTileIndex = optimunTileIndex(contentList, vsListBkUp)
        if 5 in contentList:
            if 8 not in vsListBkUp:
                chossenTileIndex = 8
            else:
                contentList.remove(5)
                chossenTileIndex = optimunTileIndex(contentList, vsListBkUp)
        if 8 in contentList:
            if 5 not in vsListBkUp:
                chossenTileIndex = 5
            else:
                contentList.remove(8)
                chossenTileIndex = optimunTileIndex(contentList, vsListBkUp)
    elif 3 in contentList:
        if 6 in contentList:
            if 0 not in vsListBkUp:
                chossenTileIndex = 0
            else:
                contentList.remove(6)
                chossenTileIndex = optimunTileIndex(contentList, vsListBkUp)
        if 5 in contentList:
            if 4 not in vsListBkUp:
                chossenTileIndex = 4
            else:
                contentList.remove(5)
                chossenTileIndex = optimunTileIndex(contentList, vsListBkUp)
    elif 5 in contentList:
        if 8 in contentList:
            if 2 not in vsListBkUp:
                chossenTileIndex = 2
            else:
                contentList.remove(8)
                chossenTileIndex = optimunTileIndex(contentList, vsListBkUp)
    elif 6 in contentList:
        if 7 in contentList:
            if 8 not in vsListBkUp:
                chossenTileIndex = 8
            else:
                contentList.remove(7)
                chossenTileIndex = optimunTileIndex(contentList, vsListBkUp)
        elif 8 in contentList:
            if 7 not in vsListBkUp:
                chossenTileIndex = 7
            else:
                contentList.remove(8)
                chossenTileIndex = optimunTileIndex(contentList, vsListBkUp)
    elif 7 in contentList:
        if 8 in contentList:
            if 6 not in vsListBkUp:
                chossenTileIndex = 6
            else:
                contentList.remove(8)
                chossenTileIndex = optimunTileIndex(contentList, vsListBkUp)
    return(chossenTileIndex)

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
            if g == x:
                winnerMain = 1
            else:
                winnerMain = 0
        elif c == f == i:
            if c == x:
                winnerMain = 1
            else:
                winnerMain = 0
        elif a == e == i:
            if a == x:
                winnerMain = 1
            else:
                winnerMain = 0
        elif b == e == h:
            if b == x:
                winnerMain = 1
            else:
                winnerMain = 0
        elif c == e == g:
            if c == x:
                winnerMain = 1
            else:
                winnerMain = 0
        elif d == e == f:
            if d == x:
                winnerMain = 1
            else:
                winnerMain = 0
        elif turnCount >= 9:
            winnerMain = -1
    return winnerMain



#Llama a la funcion homonima para iniciar el codigo
homecoming()