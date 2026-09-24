size = 5


for i in range(size):
    print()
    
    for j in range(size):
        if (j + i) % 2 == 0:
            print("X", end="")
        else: 
            print("0", end="")