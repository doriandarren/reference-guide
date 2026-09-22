my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]

max_nb = my_list[0]
min_nb = my_list[0]

for i in range(1, len(my_list)):

    if my_list[i] > max_nb:
        max_nb = my_list[i]
    
    if my_list[i] < min_nb:
        min_nb = my_list[i]

print(f"{min_nb} {max_nb}")