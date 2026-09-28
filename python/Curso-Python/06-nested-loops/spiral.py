matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# [1, 2, 3, 6, 9, 8, 7, 4, 5]

spiral_lst = []

top = 0
bottom = len(matrix) - 1

left = 0
right = len(matrix[0]) - 1


while top <= bottom and left <= right:

    # Derecha 
    for i in range(left, right + 1):
        spiral_lst.append(matrix[top][i])

    # Update top
    top += 1

    # Abajo
    for j in range(top, bottom + 1):
        spiral_lst.append(matrix[j][right])

    # Update right
    right -= 1

    # Izquierda
    if top <= bottom:

        for k in range(right, left - 1, -1):
            spiral_lst.append(matrix[bottom][k])

        bottom -= 1

    # Arriba
    if left <= right:

        for i in range(bottom, top - 1, -1):
            spiral_lst.append(matrix[i][left])

        left += 1


print(spiral_lst)
    

    