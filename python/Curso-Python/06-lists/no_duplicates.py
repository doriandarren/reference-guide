original_list = [1, 2, 3, 2, 4, 5, 4, 6, 7, 5, 8, 9, 8]

new_list = []

for ele in original_list:
    if ele in original_list and not ele in new_list:
        new_list.append(ele)


print(new_list)