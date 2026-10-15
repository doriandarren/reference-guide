number = int(input("Enter a number: "))

if number < 0:
    print("Numero negativo")
elif number > 0:
    print("Numero positivo")
else:
    print("numero es cero")
    
    
    
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
    



if number % 3 == 0 and number % 5 == 0:
    print("Divisible entre 3 y 5: Sí")
else:
    print("Divisible entre 3 y 5: No")