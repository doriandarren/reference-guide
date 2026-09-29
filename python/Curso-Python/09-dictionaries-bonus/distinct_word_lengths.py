words = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi"]

st = set()

for w in words:
    st.add(len(w))

print(st)






# words = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi"]
# distinct_lengths = {len(word) for word in words}
# print("Distinct word lengths:", distinct_lengths)