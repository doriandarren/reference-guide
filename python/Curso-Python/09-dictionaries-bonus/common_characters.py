string1 = "The quick brown fox"
string2 = "Jumped over the lazy dog"

## ('e', 'o', 'r', 't', 'h', 'u')

format_string_1 = set(string1.replace(" ", "").lower())
format_string_2 = set(string2.replace(" ", "").lower())

st = format_string_1 & format_string_2

print(tuple(st))





string1 = "The quick brown fox"
string2 = "Jumped over the lazy dog"

set1 = set(string1.replace(" ", "").lower())
set2 = set(string2.replace(" ", "").lower())
common_characters = tuple(set1.intersection(set2))

print("Common characters:", common_characters)