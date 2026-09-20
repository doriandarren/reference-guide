side1 = int(input("Enter a first number: "))
side2 = int(input("Enter a second number: "))
side3 = int(input("Enter a third number: "))

side1 = 5
side2 = 5
side3 = 5


if side1 == side2 and side1 == side3:
    print("These sides form an equilateral triangle.")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("These sides form an isosceles triangle.")
else:
    print("These sides form a scalene triangle.")