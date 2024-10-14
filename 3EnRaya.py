wellcomeImage = """X    X| OOOO
 X  X |OO  OO
  XX  |O    O
 X  X |OO  OO
X    X| OOOO
  3EN RAYA"""

gameSelectionText = '''   1 Jugador: "1"
   2 Jugadores: "2"
   Salir: "EXIT"'''


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
    print("1jugador seleccionado")

def p2Game():
    print("2Jugadores seleccionado")


homecoming()