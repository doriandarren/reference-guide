msg = ''

for num in range(1, 21):
    if num % 3 == 0 and num % 5 == 0:
        msg += "FizzBuzz"
    elif num % 3 == 0:
        msg += "Fizz"
    elif num % 5 == 0:
        msg += "Buzz"
    else:
        msg += str(num)

    if num != 20:
        msg += ', '

print(msg)