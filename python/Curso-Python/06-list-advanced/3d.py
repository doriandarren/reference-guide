matrices = [
    # Layer 1
    [
        [1, 5],
        [3, 2]
    ],

    # Layer 2
    [
        [6, 7],
        [4, 0]
    ]

]

threshold = 4



count = 0


for layer in matrices:
    for row in layer:
        for column in row:
            if column > threshold:
                count += 1 


print(count)