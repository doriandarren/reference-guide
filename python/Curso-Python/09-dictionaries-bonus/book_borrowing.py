library = {
    "The Hobbit": 3,
    "1984": 2,
    "Frankenstein": 1,
    "Pride and Prejudice": 4,
    "To Kill a Mockingbird": 2,
    "Moby Dick": 1,
    "The Great Gatsby": 3,
    "War and Peace": 2
}

# Your code


while True:
    
    opc = input("""[1] View available books
[2] Borrow a book 
[3] Return a book 
[4] Add new book / Add copies  
[5] exit: 
Choose: """).lower()
    
    if opc == '1':
        print()
        print("--------------------")
        print("View available books")
        print("--------------------")
        for name, count in library.items():
            print(f"{name}: {count}")
        print()
    elif opc == '2':
        # 2. Borrow a book
        print()
        print("--------------------")
        print("Borrow a book")
        print("--------------------")
        name_input = input("Book title: ")
        if name_input in library:
            if library[name_input] > 0:
                library[name_input] -= 1
                print(f'You borrowed "{name_input}"')
            else:
                print(f'No copies available for "{name_input}".')
        else:
            print("Error! Book not found. Try again.")
        print()
    elif opc == '3': 
        # 3. Return a book  
        print()
        print("--------------------")
        print("Return a book")
        print("--------------------")        
        name_input = input("Book title: ")
        if name_input in library:
            library[name_input] += 1
            print("Updated!")
        else:
            print("Error! Book not found. Try again.")
        print()
    elif opc == '4':
        # 4. Add new book / Add copies
        name_input = input("Book title: ")
        count_input = int(input("How many copies to add?: "))
        
        if name_input not in library:
            library[name_input] = count_input
        else:
            temp_count = library[name_input]
            library[name_input] = temp_count + count_input
            print(f'Updated {name_input} to copies.')
        
    elif opc == '5':
        # 5. Exit
        print("Bye!")
        break
