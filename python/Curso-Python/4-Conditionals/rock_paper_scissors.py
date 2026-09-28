import random

ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'

computer_options = [ROCK, PAPER, SCISSORS]

#user_chose = input("Piedra, papel o tijera, 1,2,3... [piedra/papel/tijera]: ")
user_chose = 'rock'

computer_chose = computer_options[random.randint(0,2)] 

message = ''

if user_chose == computer_chose:
    message = 'Tie!'
elif user_chose == ROCK and computer_chose == SCISSORS:
    message = 'You win! Rock smashes scissors.'
elif user_chose == PAPER and computer_chose == ROCK:
    message = 'You win! Paper covers rock.'
elif user_chose == SCISSORS and computer_chose == PAPER:
    message = 'You win! Scissors cut paper.'
else:
    message = 'You lose...'


print(f'The computer chose {computer_chose}.')
print(message)
