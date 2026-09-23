

text = "hello"
shift = 3



text = "zoo"
shift = 5


# text = "abc"
# shift = 1


text = "xyz"
shift = 3


# text = "shift"
# shift = 4


list_patterm = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

new_text = ''

for letter in text:
    
    pos = list_patterm.index(letter)    
    new_pos = (pos + shift) % len(list_patterm)
    new_text += list_patterm[new_pos]


print(new_text)