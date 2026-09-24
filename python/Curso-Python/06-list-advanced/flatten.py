
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]


new_list = []


for i, row in enumerate(nested_list):
    for j, column in enumerate(row):    
        new_list.append(column)


print(new_list)