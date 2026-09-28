
text_list = ['apple', 'banana', 'cherry']


text_list_new = []

for t in text_list:
    t = t.lower()
    t_format = ''
    for s in t:
        if s == 'a':
            t_format += '@'
        elif s in 'eiou':
            t_format += ''
        elif s == ' ':
            t_format += '_'
        else:
            t_format += s
    
    text_list_new.append(t_format)


print(text_list_new)
