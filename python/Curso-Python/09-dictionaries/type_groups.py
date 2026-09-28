items = [1, 'apple', 3.14]
#items = [True, 'hello', 2.718, 'world', 3, False, '!']

dic = {}

for ele in items:

    type_name = type(ele).__name__

    if type_name not in dic:
        dic[type_name] = [ele]
    else:
        dic[type_name].append(ele)

print(dic)