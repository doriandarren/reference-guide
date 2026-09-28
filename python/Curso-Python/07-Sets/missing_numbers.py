n = 10
rng = [4, 8, 2, 1, 3, 9]


all_lst = []

for i in range(0, (n + 1)):
    all_lst.append(i)

st = list(set(all_lst) - set(rng))

st.sort()

print(st)




# n = 10
# rng = [4, 8, 2, 1, 3, 9]

# full = set(range(n + 1))
# missing = full - set(rng)
# print(sorted(missing))