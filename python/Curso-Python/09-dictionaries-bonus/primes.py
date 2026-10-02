
n = 50

primes = []


if n > 2:
    primes.append(2)
    
    
    
for i in range(3, n, 2):
    
    is_prime = True
    
    for j in range(3, n, 2):
        if i % j == 0:
            is_prime = False
            break
        
    if is_prime:
        primes.append(i)
        
        
print(primes)    







n = 50
fibonacci = []


if n == 1:
    fibonacci = [0]
    
elif n > 2:
    
    fibonacci = [0, 1]
    
    for i in range(2, n):
        fibonacci.append( fibonacci[-1] + fibonacci[-2] ) 
        
    
    
    
    
    