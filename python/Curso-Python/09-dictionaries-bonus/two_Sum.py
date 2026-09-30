lst = [1, 2, 3, 4, 5]
target = 6

st = set()

for i in range(len(lst)):

    current_element = lst[i]

    for j in range(i + 1, len(lst)):

        if (current_element + lst[j]) == target:
            st.add((current_element, lst[j]))

print(st)



