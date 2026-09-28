price = float(input("Enter the price: "))

#price = float(120)
total = 0
message = ''

if price > 0 and price <= 20:
    total = price
    message = f"The price is {total}€."
elif price <= 50:
    discount = price * 0.10
    total = price - discount
    message = f"The discounted price is {total}€."
elif price <= 100:
    discount = price * 0.20
    total = price - discount
    message = f"The discounted price is {total}€."
elif price > 100:
    discount = price * 0.30
    total = price - discount
    message = f"The discounted price is {total}€."

print(message)