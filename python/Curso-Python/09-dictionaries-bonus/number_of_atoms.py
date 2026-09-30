
string = "Mg2N12"


atoms = {}

i = 0

while i < len(string):
    
    element = string[i]
    i += 1
    
    while i < len(string) and string[i].islower():
        element += string[i]
        i += 1
        
    number = ""
    
    while i < len(string) and string[i].isdigit():
        number +=  string[i]
        i += 1
    
    
    
    if number == "":
        count = 1
    else:
        count = int(number)
    
    
    atoms[element] = count
    

print(atoms)
