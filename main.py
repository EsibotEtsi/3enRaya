import random
import os

def print_board(board):
    display_board = ["_" if x == 0 else x for x in board]
    print(f"\n {display_board[0]} | {display_board[1]} | {display_board[2]} \n {display_board[3]} | {display_board[4]} | {display_board[5]} \n {display_board[6]} | {display_board[7]} | {display_board[8]} \n")

def check_winner(board):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] and board[a] != 0:
            return board[a]
    return None

os.system('cls||clear')
print("Welcome to 3 in a Row!")
print("The board is numbered as follows:")
print(" 1 | 2 | 3 \n 4 | 5 | 6 \n 7 | 8 | 9 \n")
board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
print_board(board)

while True:
    try:
        pos = int(input("Select a position to start playing: ")) - 1
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 9.")
        continue

    if 0 <= pos <= 8:
        if board[pos] == 0:
            board[pos] = "X"
            winner = check_winner(board)
            if winner:
                print_board(board)
                print(f"Player {winner} wins!")
                break

            m_pos = random.randint(0, 8)
            while board[m_pos] != 0:
                m_pos = random.randint(0, 8)
            board[m_pos] = "O"
            print_board(board)
            winner = check_winner(board)
            if winner:
                print(f"Player {winner} wins!")
                break
        else:
            print("That position is already taken, choose another one.")
    else:
        print("Invalid position. Please enter a number between 1 and 9.")

