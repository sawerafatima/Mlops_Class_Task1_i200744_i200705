# Tic Tac Toe game

# Create the board
board = [' '] * 9

# Function to display the board
def display_board():
    print('-------------')
    for i in range(3):
        print('|', board[i * 3], '|', board[i * 3 + 1], '|', board[i * 3 + 2], '|')
    print('-------------')

# Function to check if a player has won
def check_win(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6],
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Function to check if the board is full
def is_board_full():
    return all(x != ' ' for x in board)

# Main game loop
player = 'X'
while True:
    display_board()

    # Get player input
    while True:
        move = input(f"Player {player}'s turn (1-9): ")
        try:
            move = int(move) - 1
            if 0 <= move <= 8 and board[move] == ' ':
                break
            else:
                print("Invalid move. Please choose an empty space (1-9).")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

    # Update board
    board[move] = player

    # Check for win
    if check_win(player):
        display_board()
        print(f"Player {player} wins!")
        break

    # Check for tie
    if is_board_full():
        display_board()
        print("It's a tie!")
        break

    # Switch player
    player = 'O' if player == 'X' else 'X'

print("Game over!")
