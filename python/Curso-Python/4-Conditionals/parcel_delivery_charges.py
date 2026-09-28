# destination = input("Enter a destination [local/domestic/international]: ").lower()
# weight = float(input("Enter weight: "))



# destination = 'domestic'
# weight = 5.2

# destination = 'international'
# weight = 0.8


destination = 'local'
weight = 1


option_list = ['local', 'domestic', 'international']


if not destination in option_list:
    print("Invalid destination.")
else:
    
    # Local
    if destination == option_list[0]:
        cost = 5
        if weight > 1:
            t_weight = (weight - 1) * 2
            cost = cost + t_weight
    
    # Domestic
    elif destination == option_list[1]:
        cost = 10
        if weight > 1:
            t_weight = (weight - 1) * 4
            cost = cost + t_weight
    
    # International
    elif destination == option_list[2]:
        cost = 20
        if weight > 1:
            t_weight = (weight - 1) * 10
            cost = cost + t_weight
    
    print(f"Total cost: {cost:.1f}€.")
