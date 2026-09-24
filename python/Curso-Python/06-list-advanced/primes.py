n = 50

prime_list = []


if n > 2:
    prime_list.append(2)
    

for i in range(3, n, 2):
    
    is_prime = True
    
    for j in range(3, int(i ** 0.5) + 1, 2):
        if i % j == 0:
            is_prime = False
            break
            
    if is_prime:
        prime_list.append(i)

print(prime_list)