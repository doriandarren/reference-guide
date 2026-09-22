ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'
LIZARD = 'lizard'
SPOCK = 'spock'

# player_1 = input("Player 1 choice: ").lower()
# player_2 = input("Player 2 choice: ").lower()

player_1 = 'spock'
player_2 = 'rock'


if player_1 == player_2:
    print("It's a tie!")

elif player_1 == ROCK and (player_2 == LIZARD or player_2 == SCISSORS):
    print("Player 1 wins!")

elif player_1 == PAPER and (player_2 == ROCK or player_2 == SPOCK):
    print("Player 1 wins!")

elif player_1 == SCISSORS and (player_2 == PAPER or player_2 == LIZARD):
    print("Player 1 wins!")

elif player_1 == LIZARD and (player_2 == SPOCK or player_2 == PAPER):
    print("Player 1 wins!")

elif player_1 == SPOCK and (player_2 == SCISSORS or player_2 == ROCK):
    print("Player 1 wins!")

else:
    print("Player 2 wins!")

