
lst = [1, 2, 3, 4, 5]
target = 6

st = {}

for i in range(len(lst)):

    current_num = lst[i]

    for j in range(len(lst)):

        if (current_num + lst[j]) + current_num == current_num:
            pair = (current_num, lst[j])

            st.add(pair)


print(st)
