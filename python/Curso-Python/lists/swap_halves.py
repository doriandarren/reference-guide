
my_list = ['Python', 'is', 'so', 'good']

half = len(my_list) // 2

new_list = my_list[half:] + my_list[:half]

print(new_list)