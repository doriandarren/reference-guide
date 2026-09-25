matrix = [[4, -3, 2], [-1, 6, -7]]

for i, row in enumerate(matrix):
    for j, col in enumerate(row):
        if col < 0:
            matrix[i][j] = 0

print(matrix)
