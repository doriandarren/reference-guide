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





#-------------------------
# MinMax
#-------------------------

def minimax(board, is_maximizing):

    # Check if someone has won
    if check_winner(board, "O"):
        return 1

    if check_winner(board, "X"):
        return -1

    if is_full(board):
        return 0

    if is_maximizing:
        best_score = -float("inf")

        for i in range(3):
            for j in range(3):
                if is_cell_empty(board[i][j]):
                    board[i][j] = "O"

                    score = minimax(board, False)

                    board[i][j] = " "

                    best_score = max(score, best_score)

        return best_score

    else:
        best_score = float("inf")

        for i in range(3):
            for j in range(3):
                if is_cell_empty(board[i][j]):
                    board[i][j] = "X"

                    score = minimax(board, True)

                    board[i][j] = " "

                    best_score = min(score, best_score)

        return best_score



def best_move(board) -> tuple[int, int]:

    best_score = -float("inf")
    move = (-1, -1)

    for i in range(3):
        for j in range(3):

            if is_cell_empty(board[i][j]):

                board[i][j] = "O"

                score = minimax(board, False)

                board[i][j] = " "

                if score > best_score:
                    best_score = score
                    move = (i, j)

    return move



#-------------------------
# END MinMax
#-------------------------







# Initialize the board (3x3 list)
board = init_board()
current_player = "X"
winner = False

while not is_full(board):

    print_board(board)
    print()
    print(f"Player {current_player}'s turn.")

    if current_player == "X":
        row, col = enter_row_and_col()

    else:
        row, col = best_move(board)
        print(f"AI chooses: ({row}, {col})")

    if is_cell_empty(board[row][col]):

        board[row][col] = current_player

        if check_winner(board, current_player):

            print_board(board)
            print(f"Player {current_player} wins!")

            winner = True
            break

        current_player = "O" if current_player == "X" else "X"

    else:
        print("Cell is already occupied. Try again.")

if not winner:
    print_board(board)
    print("It's a draw!")
