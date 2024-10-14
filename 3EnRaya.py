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
    if winnerMain == -1:
        print(f"¡¡¡EMPATE!!!")
    elif winnerMain == 0:
        if isIA == True:
            print("\nIntroducir texto de victoria de IA")
        elif isIA == False:
            print("\nIntroducir mensaje de que j2 (O) ha ganado")
        else:
            print(genericErrorMsg)
    elif winnerMain == 1:
        if isIA == True:
            print("\nIntroducir mensaje de victoria humano contra IA")
        elif isIA == False:
            print("\nIntroducir mensaje de victoria de J1 (X)")
        else:
            print(genericErrorMsg)
    else:
        print(genericErrorMsg)
    print("\n¿Pega una revanchita o algo no?")
    retry = input("s/n: ")
    if retry == 's':
            gameSelection()
            exit
    if retry == 'n':
            print("\nSaliendo del juego...")
            exit
    else:
            print("\n¿Tu eres tonto o que? no es tan dificil poner s o n, por el amor de dios, por tonto repites, ea, porque me ha costado mucho hacerlo >:(\n")
            gameSelection()

def tileDrawer(possitionList, isIA, isMain):
    winnerMain = 0 #-1 empate, 0 pierde el Main, 1 gana el Main
    turnCount = 0 #Cuenta cuantos turnos llevan
    if isIA == True:
        if isMain == True:
            print(f"\nSu turno:")
        elif isMain == False:
            print(f"\nTurno de la IA")
        else:
            print(f"No se como te la has apañado, pero la has cagado, enhorabuena")
    elif isIA == False:
        if isMain == True:
            print(f"\nTurno del jugador 1 (X)")
        elif isMain == False:
            print(f"\nTurno del jugador 2 (O)")
        else:
            print(genericErrorMsg)
    else:
        print(genericErrorMsg)
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
        if g == h == i:
            if a == x:
                winnerMain = 1
            else:
                winnerMain = 0
        if c == f == i:
            if a == x:
                winnerMain = 1
            else:
                winnerMain = 0
        if a == e == i:
            if a == x:
                winnerMain = 1
            else:
                winnerMain = 0
        if b == e == h:
            if a == x:
                winnerMain = 1
            else:
                winnerMain = 0
        if c == e == g:
            if a == x:
                winnerMain = 1
            else:
                winnerMain = 0
        if d == e == f:
            if a == x:
                winnerMain = 1
            else:
                winnerMain = 0
    if turnCount >= 9:
        winnerMain = -1
    return winnerMain

homecoming()