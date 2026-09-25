matrix = [[4, 2], [8, 7]]
matrix = [[1, 2, 3], [4, 5, 6]]


matrix_new = []


for j in range(len(matrix[0])):         # Columns

    columns = []

    for i in range(len(matrix)):        # Rows

        columns.append(matrix[i][j])

    matrix_new.append(columns)

print(matrix_new)
