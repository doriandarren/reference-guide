t_list = [(1, 2), (3, 4), (9, 1), (5, 8)]


current = t_list[0][0]

for ele in t_list:
    for num in ele:
        if num > current:
            current = num

print(current)





# t_list = [(1, 2), (3, 4), (9, 1), (5, 8)]
# max(max(a, b) for a, b in t_list)