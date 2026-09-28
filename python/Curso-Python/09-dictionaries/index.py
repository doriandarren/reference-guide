my_dict = {'key1': 1, 'key2': 2, 'key3': 3}



print(type({}))


# keys()
print(my_dict.keys())

# values()
print(my_dict.values())


# items()
print(my_dict.items())
for k, v in my_dict.items():
    print(k, v)




# Crear una copia
second_dict = my_dict.copy()



# Update
second_dict = {'key3': 10, 'key4': 4}
my_dict.update(second_dict)
print(my_dict)

# {'key1': 1, 'key2': 2, 'key3': 10, 'key4': 4}




# Get
print(my_dict.get('key1'))      # Returns value of 'key1'
print(my_dict.get('key4'))      # Returns None because 'key4' doesn't exist
print(my_dict.get('key4', 0))   # Returns 0 because 'key4' doesn't exist



# in 
print('key2' in my_dict)
print('abcd' in my_dict)



# Comprension
even_dict = {i: i * 2 for i in range(5)}
print(even_dict)

# {0: 0, 1: 2, 2: 4, 3: 6, 4: 8}



text = "one two three four three two one and one"
word_lst = text.split()

d = {}

for w in word_lst:

    if w in d:
        d[w] += 1
    else:
        d[w] = 1  



# word_frequency[word] = word_frequency.get(word, 0) + 1


print(d)
