special_chars = "!@#$"

msg = ''

while True:

    has_password = False
    has_upper = False
    has_digit = False
    has_special_char = False

    password_input = input(f"{msg}Enter password: ")


    # Password
    if len(password_input) >= 8:
        has_password = True

    # Check upper and isdigit and special character
    for letter in password_input:    
        if letter.isupper():
            has_upper = True

        if letter.isdigit():
            has_digit = True
            
        if letter in special_chars:
            has_special_char = True


    
    if has_password and has_upper and has_digit and has_special_char:
        print("Your password is strong.")
        break
        
    msg = "Your password is weak. Please, enter another password. \n"