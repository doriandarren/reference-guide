height = 5
char = 'n'

for i in range(1, height + 1):
    white_space = (height - i) * " "
    print(white_space + (char * ((i * 2) - 1)))
    
# range(inicio, fin, paso)
for i in range(height - 1, 0, -1):
    white_space = (height - i) * " "
    print(white_space + (char * ((i * 2) - 1)))
