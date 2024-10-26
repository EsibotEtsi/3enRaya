
tablero = [' ' for _ in range(9)]
tablero_explicativo = ['1','2','3','4','5','6','7','8','9']

def mostrar_explicacion():
    print("3 EN RAYA")
    print("Estas serán las posiciones en el tablero:")
    print(tablero_explicativo[0], " |", tablero_explicativo[1], "| ", tablero_explicativo[2])
    print("---+---+---")
    print(tablero_explicativo[3], " |", tablero_explicativo[4], "| ", tablero_explicativo[5])     #esto muestra el tablero, con sus respectivas jugadadas
    print("---+---+---")
    print(tablero_explicativo[6], " |", tablero_explicativo[7], "| ", tablero_explicativo[8])

def mostrar_tablero():
    print(tablero[0], "|", tablero[1], "|", tablero[2])
    print("---+---+---")
    print(tablero[3], "|", tablero[4], "|", tablero[5])     #esto muestra el tablero, con sus respectivas jugadadas
    print("---+---+---")
    print(tablero[6], "|", tablero[7], "|", tablero[8])
    
def victoria(jugador):
    combinaciones=[
        [0,1,2], [3,4,5],[6,7,8],   #filas
        [0,3,6], [1,4,7],[2,5,8],   #columnas
        [0,4,8],[2,4,6]             #diagonales
    ]
    for combo in combinaciones:
        if tablero[combo[0]]==tablero[combo[1]]==tablero[combo[2]]== jugador:
            print("El jugador " + jugador + " es el ganador")
            return True
    return False

def lleno():
    if ' ' in tablero:
        return False
    else:
        print("Empate ")
        return True

def jugadas(jugador):
    juego=int(input(f"Jugador {jugador}, elige una casilla (1-9): " ))-1
    if juego in range(9):
        if tablero[juego]==' ':
            tablero[juego]=jugador
            mostrar_tablero()  
        else:
            print("La casilla que has seleccionado ya está ocupada, prueba otra vez.")   
            jugadas(jugador)        
    else:
        print("Jugada no válida, prueba otra vez: ")
        jugadas(jugador)


def turno(jugador):
    if (jugador=='X'):
        return 'O'
        print(jugador)
    else:
        return 'X'
        print("lo que sea")

def jugar():
    
    mostrar_explicacion()
    jugador='O'
    print("hola")
    while True:
        jugador=turno(jugador)
        jugadas(jugador)
        if victoria(jugador):
            break
        if lleno():
            break
jugar()
