import math

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        # Eliminate even numbers greater than 2
        return False
    
    # Optimization: check only odd divisors and up to sqrt(num)
    limit = int(math.sqrt(num))+1
    for i in range(3, limit, 2):
        if num % i == 0:
            return False
    return True

numbers = list(range(1, 51))
primes = list(filter(is_prime, numbers))
print(primes)