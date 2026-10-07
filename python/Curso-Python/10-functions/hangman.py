def print_screen(s):
    return input(s).strip().upper()



def play_hangman(w):
    
    remaining_attempts = 5
    char_lst = ["_" for c in w ]
    
    
    while True:
        
        print(' '.join(char_lst))
        char = print_screen("[Player 2] - Enter a character: ")
        
        
        if len(char) != 1:
            print("Enter only one character.")
            continue
        
        
        if char in w:
            
            for i, c in enumerate(w):
                if c == char:
                    char_lst[i] = char
            
        else: 
            remaining_attempts -= 1
            print(f"{char} is a wrong guess.")
            
        
        print(f"Remaining attempts: {remaining_attempts}")

        # Comprobar si ya no quedan "_"
        if "_" not in char_lst:
            print(" ".join(char_lst))
            print("You won!")
            break
        
        if remaining_attempts <= 0:
            print(f"You lost! The word was: {w}")
            break




# Start  
word = print_screen("[Player 1] - Enter a word: ")
play_hangman(word)