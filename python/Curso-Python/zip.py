tablero = [
    [1,2,3],
    [3,5,6],
    [7,8,9],
]

numbers = set(range(1, 10))
    

def chech_row(row):
    for row in row:
        if set(row) != numbers:
            return False


print(chech_row(zip(*tablero)))


