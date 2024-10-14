wellcomeImage = """X    X| OOOO
 X  X |OO  OO
  XX  |O    O
 X  X |OO  OO
X    X| OOOO
  3EN RAYA"""

gameSelectionText = '''   1 Jugador: "1"
   2 Jugadores: "2"
   Salir: "EXIT"'''
x = 'X'
o = 'O'

def homecoming():
    print(f'{wellcomeImage}\n')
    gameSelection()

def gameSelection():
    print(f'Opciones:\n{gameSelectionText}')
    gameMode = input("Introduzca el numero de jugadores: ")
    if gameMode != "1" and gameMode != "2" and gameMode != "EXIT":
        print("Entrada erronea")
        gameSelection()
    elif(gameMode == "1"):
        p1Game()
    elif(gameMode == "2"):
        p2Game()
    elif(gameMode == "EXIT"):
        print("Saliendo del juego...")

def p1Game():
    autoPlayer(1)

def p2Game():
    autoPlayer(2)

def autoPlayer(playerNumber):
    possitionList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    isIA = False #True significa que se juega contra la ia, false que es JcJ
    isMain = False #True significa que es turno del jugador principal, par1 1J el humano, y para 2J el jugador 1
    if playerNumber == 1:
        isIA = True
        isMain = True
        winnerMain = tileDrawer(possitionList,isIA, isMain)
    else:
        isIA = False
        isMain = True
        winnerMain = tileDrawer(possitionList, isIA, isMain)
    winnerManager(winnerMain, isIA, possitionList)

def winnerManager(winnerMain, isIA, possitionList):
    print(x)

def tileDrawer(possitionList, isIA, isMain):
    winnerMain = 0 #-1 empate, 0 pierde el Main, 1 gana el Main
    turnCount = 0 #Cuenta cuantos turnos llevan
    if isIA == True:
        if isMain == True:
            print(f"Su turno:")
        elif isMain == False:
            print(f"Turno de la IA")
        else:
            print(f"No se como te la has apañado, pero la has cagado, enhorabuena")
    elif isIA == False:
        if isMain == True:
            print(f"Turno del jugador 1 (X)")
        elif isMain == False:
            print(f"Turno del jugador 2 (O)")
        else:
            print(f"No se como te la has apañado, pero la has cagado, enhorabuena")
    else:
        print(f"No se como te la has apañado, pero la has cagado, enhorabuena")
    a, b, c, d, e, f, g, h, i = possitionList
    print(f" {a} | {b} | {c}\n-----------\n {d} | {e} | {f}\n-----------\n {g} | {h} | {i}")
    winnerMain = loopGestor(possitionList, isIA, isMain, turnCount)
    return(winnerMain)

def loopGestor(possitionListIN, isIAIN, isMainIN, turnCount):
    return(False)

def winCheck(possitionList, turnCount):
    winnerMain = 2;
    if turnCount >= 5:
        a, b, c, d, e, f, g, h, i = possitionList
        if a == b == c:
            if a == x:
                winnerMain = 1
            else:
                winnerMain = 0
        if a == d == g:
            if a == x:
                winnerMain = 1
            else:
                winnerMain = 0

homecoming()