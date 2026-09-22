num = "8680960898"
i = 0
n_half = len(num) // 2
is_mirror = True

while i < n_half and is_mirror:
    if num[i] not in ["0", "6", "8", "9"]:
        is_mirror = False
    elif num[i] == "0" and num[-i-1] !="0":
        is_mirror = False
    elif num[i] == "8" and num[-i-1] !="8":
        is_mirror = False
    elif num[i] == "6" and num[-i-1] !="9":
        is_mirror = False
    elif num[i] == "9" and num[-i-1] !="6":
        is_mirror = False
    i = i +1

if is_mirror:
    print("Mirror")
else:
    print("Not Mirror")




# number = 8680960898
# number = 123
# number = 609

# n_list1 = ['0', '8', '6', '9']
# n_list2 = ['0', '8', '9', '6']


# number_format = str(number)

# has_mirror = True

# half = (len(number_format) + 1) // 2 ## Comparar hasta la mitad

# for i in range(half):

#     n = number_format[i]

#     if n in n_list1:

#         pos = n_list1.index(n)

#         last_number = number_format[-i - 1]

#         if n_list2[pos] != last_number:
#             has_mirror = False

#     else:
#         has_mirror = False

# if not has_mirror:
#     print("Not Mirror")
# else:
#     print("Mirror")
