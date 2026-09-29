
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Output:
# Odd numbers: {1, 3, 5, 7, 9}
# Even numbers: {2, 4, 6, 8, 10}


odd_numbers = set()
even_numbers = set()


for n in numbers:
    if n % 2 == 0:
        even_numbers.add(n)
    else:
        odd_numbers.add(n)


# odd_numbers = {n for n in numbers if n % 2 != 0}
# even_numbers = {n for n in numbers if n % 2 == 0}

print(odd_numbers)
print(even_numbers)
