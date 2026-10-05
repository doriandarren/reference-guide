# Your code here

def filter_sentences(sentences, word):
    lst = []

    word_format = word.lower()

    for element in sentences:
        if word_format in element.lower().split():
            lst.append(element)
    return lst



def count_word(sentences, word):
    filtered_lst = filter_sentences(sentences, word)

    count = 0

    for s in filtered_lst:
        count += s.lower().split().count(word.lower())

    return count



# Example usage
sentences = [
    "I love apples and bananas",
    "Bananas are great for breakfast bananas are the best",
    "I prefer apples over pears",
    "Pears are tasty but I like bananas too"
]

print(count_word(sentences, "bananas"))