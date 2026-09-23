import math

"""
'C'— la posición del personaje (hay exactamente una en el mapa),
'T'— la posición del tesoro (también exactamente una),
'.'— una celda vacía.
"""


grid = [
    ['.', 'T'],
    ['C', '.']
]

grid = [['C', '.', '.', '.', 'T']]

grid = [
    ['.', '.', '.', '.'],
    ['.', 'C', '.', '.'],
    ['.', '.', '.', 'T'],
    ['.', '.', '.', '.']
]



pos_character = [0, 0]
pos_treasure = [0, 0]


for i, row in enumerate(grid):
    
    for j, column in enumerate(row):
        
        if column == 'C':
            pos_character = [i, j]
        
        if column == 'T':
            pos_treasure= [i, j]
        

euclidean = math.sqrt(
    (pos_treasure[0] - pos_character[0]) ** 2 + 
    (pos_treasure[1] - pos_character[1]) ** 2 
)

print(f"{euclidean:.2f}")







# import math

# grid = [
#     ['.', 'T'],
#     ['C', '.']
# ]

# char_pos = []
# treasure_pos = []

# for i, row in enumerate(grid):
#     for j, cell in enumerate(row):
#         if cell == 'C':
#             char_pos = [i, j]
#         elif cell == 'T':
#             treasure_pos = [i, j]
    
#     if len(char_pos) == len(treasure_pos) == 2:
#         break

# x1, y1 = char_pos
# x2, y2 = treasure_pos

# dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
# print(f'The Euclidean distance to the treasure is: {dist:.2f}.')