lst = ["apple", "banana", "cherry"]
lst = ["sky", "fly", "try"]

vocals = 'aeiou'
dic = {}


for string in lst:
    
    dic[string] = sum(1 for char in string.lower() if char in vocals)
    
print(dic)
## {"apple": 2, "banana": 3, "cherry": 1}





# lst = ["apple", "banana", "cherry"]
# vocals = 'aeiou'
# dic = {}

# for string in lst:
#     string = string.lower()
#     count_vocal = 0
    
#     for character in string:
#         if character in vocals:
#             count_vocal += 1
    
#     dic[string] = count_vocal

# print(dic)