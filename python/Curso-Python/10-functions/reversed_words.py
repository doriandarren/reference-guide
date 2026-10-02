def reverse_words(s):
    return " ".join([ ele[::-1] for ele in s.split() ])


sentence = "This is a reversed sentence"

print(reverse_words(sentence))