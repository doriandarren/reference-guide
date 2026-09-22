"""

my_list = [1, 2, 3, 4, 5]

my_list = ['a', 'b', 'c', 'd', 'e']

"""

input_list = input("Enter the list [ex. my_list = [1, 2, 3, 4, 5]]: ") # my_list = [1, 2, 3, 4, 5]
pos = int(input("Position: "))

#input_list = 'my_list = [1, 2, 3, 4, 5]'
#pos = 3

my_list_temp = input_list.split("=")[1].strip()
list_value = my_list_temp.replace("[", "").replace("]", "").replace("'", "").replace('"', '').split(",")
my_list = []

for ele in list_value:
    if ele.isdigit():
        my_list.append(int(ele.strip()))
    else:
         my_list.append(ele.strip())

new_list = my_list[pos:] + my_list[:pos]

print(new_list)
