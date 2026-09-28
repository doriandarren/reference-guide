n = 100

numbers = list(range(2, n + 1))

prime_list = []

while numbers:

    prime = numbers[0]

    prime_list.append(prime)

    new_numbers = []

    for number in numbers:

        if number % prime != 0:
            new_numbers.append(number)

    numbers = new_numbers

print(prime_list)
