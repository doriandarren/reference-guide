PLAN_BASIC = 'basic'
PLAN_PREMIUM = 'premium'

age = int(input('Enter age: '))
any_accident = input('Enter any accident [Yes/No]: ')
plan = input(f'Plan [{PLAN_BASIC}/{PLAN_PREMIUM}]: ')


# Datos:
# age = 24
# any_accident = 'Yes'
# plan = 'basic'


if plan != PLAN_BASIC and plan != PLAN_PREMIUM:
    print("Invalid insurance plan")
    
elif any_accident != 'Yes' and any_accident != 'No':
    print("Invalid response for previous accidents.")
    
else:
    
    if plan == PLAN_BASIC:
        total = 200
    elif plan == PLAN_PREMIUM:
        total = 500
    
    if age < 25 and any_accident == 'Yes':
        recharge = (total * 0.30)
        total += recharge
    elif age < 25 and any_accident == 'No':
        recharge = (total * 0.05)
        total += recharge
    
    print(f"Your insurance premium is {total}€.")