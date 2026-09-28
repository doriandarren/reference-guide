
#string = input('Enter a string: ')

#string = 'Hello World'
string = 'AEIOUaeiou'
#string = 'Python Programming'

string = string.replace('a', '').replace('A', '')
string = string.replace('e', '').replace('E', '')
string = string.replace('i', '').replace('I', '')
string = string.replace('o', '').replace('O', '')
string = string.replace('u', '').replace('U', '')

print(string)