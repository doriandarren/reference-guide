
def is_palidrome(s):

    s_format = s.lower().strip().replace(" ", "")
    palindrome = s[::-1].lower().strip().replace(" ", "")

    if s_format == palindrome:
        return True

    return False





#string = input("Enter a string: ")

string = 'A man a plan a canal Panama'
#string = 'Never odd or even'
#string = 'none'

result = "is" if is_palidrome(string) else "is not"

print(f"'{string}' {result} a palindrome")

