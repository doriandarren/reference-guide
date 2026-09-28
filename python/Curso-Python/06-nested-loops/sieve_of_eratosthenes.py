n = 100

numbers = list(range(2, n + 1))

new_numbers = []


for i in numbers:

    prime = i

    for number in numbers:
        if number == prime or number % prime != 0:
            new_numbers.append(number)


print(new_numbers)
