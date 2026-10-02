
def is_prime(n):
    
    primes = []

    limit = n

    if n > 2:
        primes.append(2)

    for i in range(3, limit, 2):
        is_prime = True

        for j in range(3, i, 2):
            if i % j == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(i)
        
    print(primes)
    
    if n in primes:
        return True
    else:
        return False



n = 10

result = "is" if is_prime(n) else "is not"  

print(f"{n} { result} a prime number.")