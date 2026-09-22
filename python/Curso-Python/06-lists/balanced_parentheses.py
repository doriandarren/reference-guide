
string = "(()())"
string = "(()"
string = "(()((()))(()((()))))"

counter = 0
is_balanced = True


for c in string:
    if c == "(":
        counter += 1
    else:
        counter -= 1
        
    if counter < 0:
        is_balanced = False
        break

if counter == 0 and is_balanced:
    print("Balanced")
else:
    print("Not Balanced")






# s = "(()((()))(()((()))))"

# count = 0
# i = 0
# balanced = True

# while balanced and i < len(s):
#     if s[i] == "(":
#         count += 1
#     else:
#         count -= 1
#         if count < 0:
#             balanced = False
#     i += 1

# if count != 0:
#     balanced = False

# print("Balanced" if balanced else "Not Balanced")