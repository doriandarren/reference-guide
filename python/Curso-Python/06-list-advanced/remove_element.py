original_list = [1, 2, 3, 4, 3, 5, 3, 3]

number = int(input("Number to delete: "))   # 3

while number in original_list:
    original_list.remove(number)
        
print(original_list)