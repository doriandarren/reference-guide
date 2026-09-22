#age = 18
#if age >= 18:
#    eligibility = "eligible"
#else:
#    eligibility = "not eligible"
#print(f"You are {eligibility} to vote.")




# Ternario:
#age = 18
#eligibility = "eligible" if age >= 18 else "not eligible"
#print(f"You are {eligibility} to vote.")


#import random
#random.randint()


score = 9
score = 7.5
score = 6
score = 5.5
# score = -1



# if score >= 9 and score <= 10:
#     print("Your grade is: Excellent")
# elif score >= 7 and score < 9:
#     print("Your grade is: Very good")
# elif score >= 6 and score < 7:
#     print("Your grade is: Good")
# elif score >= 5 and score < 6:
#     print("Your grade is: Pass")
# elif score >= 0 and score < 5:
#     print("Your grade is: Fail")
# else:
#     print("Error: Scores should be a number between 0 and 10.")


# if 9 <= score <= 10:
#     print("Your grade is: Excellent")
# elif 7 <= score < 9:
#     print("Your grade is: Very good")
# elif 6 <= score < 7:
#     print("Your grade is: Good")
# elif 5 <= score < 6:
#     print("Your grade is: Pass")
# elif 0 <= score < 5:
#     print("Your grade is: Fail")
# else:
#     print("Error: Scores should be a number between 0 and 10.")



x = 3
result = x > 2
print(type(result))

x = 4
if x > 5:
    print("A")
elif x > 3:
    print("B")
else:
    print("C")



x = 8
if x % 2 == 0:
    print("Even")
else:
    print("Odd")


x = 3
y = 4

if x > y:
    print("X")
elif x == y:
    print("Y")
else:
    print("Z")



answer = "YES"

if answer == "yes":
    print("OK")
elif len(answer) == 3:
    print("Maybe OK")
else:
    print("Not OK")







x = 4
y = 1
z = 7

if x > y and z > y and x < z:
    if y * 2 == 14 or y < z:
        if x + y == z or x + y + 1 >= z:
            print("Nice")
        elif z + y <= 8 and z - x + y == 0:
            print("Try again")
        elif x * y == z:
            print("Salchipapa")
        else:
            print("Here we are")
    else:
        print("Right turn")
else:
    print("Yes")