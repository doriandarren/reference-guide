grid = [
    ['.', 'T'],
    ['C', '.']
]

"""
'C'— la posición del personaje (hay exactamente una en el mapa),
'T'— la posición del tesoro (también exactamente una),
'.'— una celda vacía.
"""

pos_character = [0,0]
pos_treasure = [0,0]


for i, row in enumerate(grid):

    for j, column in enumerate(row):

        print(column)

        if column == 'C':
            pos_character = [i,j]

        if column == 'T':
            pos_treasure = [i,j]

        


print(pos_character)
print(pos_treasure)