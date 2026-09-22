card_nb = '4123456789012345'
card_nb = '5123-4567-8910-1234'
card_nb = '61234'
#card_nb = '7123456789012345'

card_nb = input("Enter the card number: ")

msg = ''

if not card_nb.isdigit():
    msg = 'Invalid credit card number: Must contain only digits.'
elif len(card_nb) != 16:
    msg = 'Invalid credit card number: Must have exactly 16 digits.'
elif not card_nb.startswith('4') and not card_nb.startswith('5') and not card_nb.startswith('6'):
    msg = 'Invalid credit card number: Must start with 4, 5, or 6.'
else:
    msg = 'Valid credit card number.'

print(msg)
    