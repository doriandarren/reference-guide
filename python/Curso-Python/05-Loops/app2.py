plan = input("Plan [Basic/Plus/Premium]: ").lower()
student_status =  input("Student? [Yes/No]: ").lower()


# plan = "Basic".lower()
# is_student = 'yes'


if plan != "basic" and plan != "plus" and plan != "premium":
    print("Invalid plan selected.")
else:

    monthly_bill = 0

    if plan == "basic":
        monthly_bill = 5
    elif plan == "plus":
        monthly_bill = 15
    elif plan == "premium":
        monthly_bill = 25

    if student_status == "yes":
        monthly_bill -= 5    
    
    print(f"Your monthly bill is {monthly_bill}€.")