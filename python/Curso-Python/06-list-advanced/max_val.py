matrix = [[1, 2], [3, 4]]

max_value = matrix[0][0]
position = '0, 0'


for i, row in enumerate(matrix):

    for j, colum in enumerate(row):

        if colum > max_value:
            max_value = colum
            position = f"{i}, {j}"

print(f"Max value: {max_value}, Position: ({position})")
