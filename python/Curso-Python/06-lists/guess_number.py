import random

random_nb = random.randint(1,100)

print(random_nb)

msg = "Enter a number [1-100]"
user_nb = int(input(f"{msg}: "))

while user_nb != random_nb:

    if user_nb > random_nb:
        msg = "Too high! Guess again"
    else:
        msg = "Too low! Guess again"
    
    user_nb = int(input(f"{msg}: "))

print("Congratulations! You guessed the correct number.")
