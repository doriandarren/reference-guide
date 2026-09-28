my_list = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]


# impares de una lista
odd_indexed_elements = my_list[1::2]
print(odd_indexed_elements)




## First Half: el medio
count = len(my_list)
first_half = count // 2
print(my_list[:first_half])


## Dos ultimos elementos
print(my_list[-2:])
