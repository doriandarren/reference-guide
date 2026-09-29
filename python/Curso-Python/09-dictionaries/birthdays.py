
agenda = {}


agenda['dorian'] = {
    "name": 'dorian',
    "date_of_birth": '2018-05-01',
}


agenda['pepe'] = {
    "name": 'pepe',
    "date_of_birth": '2020-06-10',
}


while True:
    
    opc = input("Options [1] New Friend | [2] Find Friend | [done] exit: ").lower()
    
    if opc == '1':
        print("****** New Friend ******")
        name = input("Enter a name: ")
        date_of_birth = input("Enter a date of birth [AAAA-MM-DD]: ")

        agenda[name] = {
            "name": name,
            "date_of_birth": date_of_birth,
        }

        
    elif opc == '2':
        print("****** Find Friend ******")
        name = input("Enter a name to find: ")

        if name not in agenda:
            print(f"{name}'s birthday is not in the database.")
        else:
            person = agenda[name]
            print(f"""
Name: {person["name"]} 
Date of birth: {person["date_of_birth"]}
""")


    if opc == 'done':
        print("Bye")
        break

