# Inputs
credit_score = int(input("Credit score: "))
income = float(input("Annual income: "))


# Messages
message_ok = "You are eligible for a loan."
message_ko = "You are not eligible for a loan."


if credit_score < 300 or credit_score > 850:
    print("Invalid range")
else:
    if credit_score >= 300 and credit_score <= 579:
        print(message_ko)

    elif credit_score <= 669:
        print(message_ko)
        
    elif credit_score <= 739:
        if income >= 30_000:
            print(message_ok)
        else:
            print(message_ko)

    elif credit_score <= 799:
        if income >= 25_000:
            print(message_ok)
        else:
            print(message_ko)

    elif credit_score <= 850:
        if income >= 20_000:
            print(message_ok)
        else:
            print(message_ko)