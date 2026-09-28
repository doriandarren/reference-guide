matrix = [
    [1, 0, 1, 0],
    [1, 1, 1, 0],
    [1, 1, 1, 0],
    [0, 1, 1, 1]
]

max_size = 0

rows = len(matrix)
cols = len(matrix[0])

# Probamos diferentes tamaños de cuadrados
for size in range(1, min(rows, cols) + 1):

    # Recorremos las posiciones donde puede empezar el cuadrado
    for i in range(rows - size + 1):

        for j in range(cols - size + 1):

            is_square = True

            # Comprobamos todos los elementos del cuadrado
            for row in range(i, i + size):

                for col in range(j, j + size):

                    if matrix[row][col] == 0:
                        is_square = False
                        break

                if not is_square:
                    break

            # Si todos son 1, actualizamos el tamaño máximo
            if is_square:
                max_size = max(max_size, size)

print(max_size)
