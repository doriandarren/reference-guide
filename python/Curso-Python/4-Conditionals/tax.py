#salary = input("Salary: ")


salary = 60000.0
tax = 0

if salary <= 10000:
    tax = 0

elif salary <= 25000:
    tax += (salary - 10000) * 0.15

elif salary <= 38000:
    tax = 15000 * 0.15
    tax += (salary - 25000) * 0.20
    
else:
    tax = 15000 * 0.15
    tax += 13000 * 0.20
    tax += (salary - 38000) * 0.40


print(f"The total amount to pay in taxes is {tax}€.")