ESPRESSO = 'espresso'
AMERICANO = 'americano'
LATTE = 'latte'

MAX_CAFFEINE = 400

coffee_type = input("Enter coffee type [espresso/americano/latte]: ").lower()
shots = int(input("Enter number of shots: "))

if coffee_type != ESPRESSO and coffee_type != AMERICANO and coffee_type != LATTE:
    print("Invalid coffee type.")

elif shots <= 0:
    print("Invalid number of shots.")

else:

    if coffee_type == ESPRESSO:
        caffeine = shots * 64

    elif coffee_type == AMERICANO:
        caffeine = shots * 12

    else:
        caffeine = shots * 32

    if caffeine <= MAX_CAFFEINE:
        print(f"You will consume {caffeine} mg of caffeine, which is within your tolerance.")
    else:
        print(f"You will consume {caffeine} mg of caffeine, which exceeds your tolerance.")