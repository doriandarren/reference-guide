import random


deck = [
    "2♠", "3♠", "4♠", "5♠", "6♠", "7♠", "8♠", "9♠", "10♠", "J♠", "Q♠", "K♠", "A♠",
    "2♥", "3♥", "4♥", "5♥", "6♥", "7♥", "8♥", "9♥", "10♥", "J♥", "Q♥", "K♥", "A♥",
    "2♦", "3♦", "4♦", "5♦", "6♦", "7♦", "8♦", "9♦", "10♦", "J♦", "Q♦", "K♦", "A♦",
    "2♣", "3♣", "4♣", "5♣", "6♣", "7♣", "8♣", "9♣", "10♣", "J♣", "Q♣", "K♣", "A♣"
]


# Player
player_hand = []

# Dealer
dealer_hand = []


def shuflle_deck():
    random.shuffle(deck)


def initial_distribute():
    for i in range(2):
        player_hand.append(deck.pop())
        dealer_hand.append(deck.pop())


def calculate_hand(hand):
    total = 0
    aces = 0

    for c in hand:
        value = c[:-1]

        if value in ["J", "Q", "K"]:
            total += 10

        elif value == "A":
            total += 11
            aces += 1

        else:
            total += int(value)

    # Si nos pasamos de 21, convertimos ases de 11 a 1
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1

    return total


def request_player():
    return input("Hit or stand? [h/s]: ").lower()


def show_hand(hand):
    return " ".join(hand)


def play():

    shuflle_deck()
    initial_distribute()

    print(f"Dealer's displayed card is {dealer_hand[-1]}.")
    print(
        f"Player's hand: {show_hand(player_hand)} "
        f"(Total: {calculate_hand(player_hand)})"
    )

    # -------------------
    # TURNO DEL JUGADOR
    # -------------------

    while True:

        response = request_player()

        if response == "h":

            card = deck.pop()
            player_hand.append(card)

            player_total = calculate_hand(player_hand)

            print(
                f"Player draws {card}. "
                f"Player's hand: {show_hand(player_hand)} "
                f"(Total: {player_total})"
            )

            # Jugador se pasa
            if player_total > 21:
                print(
                    f"Player's hand value: {player_total}. "
                    f"Dealer wins!"
                )
                return

        elif response == "s":
            player_total = calculate_hand(player_hand)

            print(f"Player stands with total: {player_total}.")
            break

        else:
            print("Invalid option. Enter 'h' or 's'.")


    # TURNO DEL DEALER

    dealer_total = calculate_hand(dealer_hand)

    print(
        f"Dealer's turn begins. "
        f"Dealer's hand: {show_hand(dealer_hand)} "
        f"(Total: {dealer_total})."
    )

    # Dealer roba mientras tenga menos de 17
    while dealer_total < 17:

        card = deck.pop()
        dealer_hand.append(card)

        dealer_total = calculate_hand(dealer_hand)

        print(
            f"Dealer draws {card}. "
            f"Dealer's hand: {show_hand(dealer_hand)} "
            f"(Total: {dealer_total})."
        )



    # RESULTADO

    player_total = calculate_hand(player_hand)

    if dealer_total > 21:
        print(
            f"Dealer busts with {dealer_total}. "
            f"Player wins!"
        )

    elif player_total > dealer_total:
        print(
            f"Player wins with {player_total} "
            f"against {dealer_total}!"
        )

    elif dealer_total > player_total:
        print(
            f"Dealer wins with {dealer_total} "
            f"against {player_total}!"
        )

    else:
        print(
            f"Both players have a hand value of "
            f"{player_total}, it's a tie!"
        )


play()