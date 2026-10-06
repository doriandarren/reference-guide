def init_board() -> list[list[str]]:
    ''' Returns a 3 x 3 board with all cells empty. '''
    # Asi:
    # board = []
    # for i in range(3):
    #     board.append([" ", " ", " "])
    # return board

    # O asi:
    return [[" ", " ", " "] for _ in range(3)]



def print_board(board: list[list[str]]) -> None:
    ''' Prints the 3x3 board. '''
    for row in board:
        print(row)


def enter_row_and_col() -> tuple[int, int]:
    ''' Returns the row and column entered by the user. Rows and columns are zero-based. 
        Make sure the user enters valid values.'''

    ##i, j = map( int, input("Enter row and col [i,j]: ").split(",") )

    i, j = -1, -1
    while (i < 0 or i > 2) or (j < 0 or j > 2):
        i, j = map( int, input("Enter row and col [i,j]: ").split(",") )
    return (i,j)
    


def check_winner(board: list[list[str]], player: str) -> bool:
    ''' Returns True if the given player has won the game. '''
    
    # Check row
    for row in board:
        if row[0] == row[1] == row[2] == player:
            return True
    
    # Check col
    for col in zip(*board):
        if col[0] == col[1] == col[2] == player:
            return True
    

    # Diagonal 1
    diag1 = []
    diag2 = []
    
    j = 2

    for i in range(3):
        diag1.append(board[i][i] == player)
        
        diag2.append(board[i][j] == player)

        j -= 1
 

    if all(diag1) or all(diag2):
        return True
    

    return False



def is_full(board: list[list[str]]) -> bool:
    ''' Returns True if the board is full. '''
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

def is_cell_empty(cell: str) -> bool:
    ''' Returns True if the board cell is empty. '''
    return cell == " "


import time

# Initialize the board (3x3 list)
board = init_board()
current_player = "X"
winner = False

while not is_full(board):
    # Print 3x3 board
    print_board(board)
    time.sleep(0.2)
    print()
    print(f"Player {current_player}'s turn.")
    # Wait for the user to input a correct row and column separated by a comma
    row, col = enter_row_and_col()

    # Check if the cell (row and column) is empty
    if is_cell_empty(board[row][col]):
        # Update the board with the current player's mark
        board[row][col] = current_player
        # Check if the current player has won the game
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            winner = True
            break
        # Switch the current player
        current_player = "O" if current_player == "X" else "X"
    else:
        print("Cell is already occupied. Try again.")

if not winner:
    # Board is full and no winner
    print_board(board)
    print("It's a draw!")