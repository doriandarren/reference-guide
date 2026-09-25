matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

new_matrix = []
matrix_temp = matrix[::-1]

for j, row in enumerate(matrix_temp):

    column_list = []

    for i, column in enumerate(row):
        column_list.append(matrix_temp[i][j])
        #print(matrix[i][j])

    new_matrix.append(column_list)

print(new_matrix)
# [[7, 4, 1], [8, 5, 2], [9, 6, 3]]







# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# # Solution
# n = len(matrix)
# rotated = [[0]*n for _ in range(n)]

# for i in range(n):
#     for j in range(n):
#         rotated[j][n - 1 - i] = matrix[i][j]

# print(rotated)
