


n = int(input("Introduce un número: "))

lst = []

for i in range(1, n + 1):
    
    if i % 2 == 0:
        
        if not i % 3 == 0:
            
            if i > 5:
                lst.append(i)
            

print("Numero encontrados:", lst)
print("Cantidad:", len(lst))
print("Suma:", sum(lst))