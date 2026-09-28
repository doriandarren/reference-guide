matrix = [[1, 2, 4], [3, 6, 9], [8, 7, 10]]

count_even = 0

for row in matrix:
    for ele in row:
        if ele % 2 == 0:
            count_even += 1

print(count_even)
