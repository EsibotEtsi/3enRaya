import random

wellcomeImage = """X    X| OOOO
 X  X |OO  OO
  XX  |O    O
 X  X |OO  OO
X    X| OOOO
  3EN RAYA"""

gameSelectionText = '''   1 Jugador: "1"
   2 Jugadores: "2"
   Salir: "exit"'''
x = 'X'
o = 'O'

genericErrorMsg = "\nNo se como te la has apañado, pero la has cagado, enhorabuena"

def homecoming():
    print(f'{wellcomeImage}\n')
    gameSelection()

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

def winnerManager(winnerMain, isIA, possitionList):
    a, b, c, d, e, f, g, h, i = possitionList
    print(f"\n {a} | {b} | {c}\n-----------\n {d} | {e} | {f}\n-----------\n {g} | {h} | {i}")
    if winnerMain == -1:
        print(f"¡¡¡EMPATE!!!")
    elif winnerMain == 0:
        if isIA == True:
            print("Introducir texto de victoria de IA")
        elif isIA == False:
            print("Introducir mensaje de que j2 (O) ha ganado")
        else:
            print(genericErrorMsg, "0")
    elif winnerMain == 1:
        if isIA == True:
            print("Introducir mensaje de victoria humano contra IA")
        elif isIA == False:
            print("Introducir mensaje de victoria de J1 (X)")
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

def autoIAnt(possitionList):
    availableList = []
    for tile in possitionList:
        if tile != o and tile != x:
            availableList.append(tile)
    randomEl = random.choice(availableList)
    elIndex = possitionList.index(randomEl)
    possitionList[elIndex] = o

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

homecoming()