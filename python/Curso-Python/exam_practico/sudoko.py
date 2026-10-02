from turtle import st


sudoku = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]



def print_sudoku(sudoku):
    
    
    numbers = set(range(1, 10))
    
    # validar Filas
    for row in sudoku:
        if set(row) != numbers:
            return False
    
    
    # Validar column
    for col in range(9):
        column = []
        
        for row in range(9):
            column.append(sudoku[row][col])
            
        if set(column) != numbers:
            return False
    
    
    
    
    # Validar 3x3
    for start_row in range(0, 9, 3):
        
        print(start_row)
        
        for start_col in range(0, 9, 3):
            print(start_col)
            
            square = []
            
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    square.append(sudoku[i][j])
            
            if set(square) != numbers:
                return False
            
            
    return True
        


print(print_sudoku(sudoku))







# tab = [
#     [5, 3, 4, 6, 7, 8, 9, 1, 2],
#     [6, 7, 2, 1, 9, 5, 3, 4, 8],
#     [1, 9, 8, 3, 4, 2, 5, 6, 7],
#     [8, 5, 9, 7, 6, 1, 4, 2, 3],
#     [4, 2, 6, 8, 5, 3, 7, 9, 1],
#     [7, 1, 3, 9, 2, 4, 8, 5, 6],
#     [9, 6, 1, 5, 3, 7, 2, 8, 4],
#     [2, 8, 7, 4, 1, 9, 6, 3, 5],
#     [3, 4, 5, 2, 8, 6, 1, 7, 9]
# ]


# corr = set(range(1,10))

# check_rows = all([set(row) == corr for row in tab ])
# check_rows = all([set(col) == corr for col in zip(*tab) ])

