n = 246323

n_format = str(n)

count_odd = 0   # Impar
count_even = 0  # Par

for i, ele in enumerate(n_format[::-1]):
    if i % 2 == 0:
        count_odd += int(ele)
    else:
        count_even += int(ele)

if count_even == count_odd:
    print("Balanced")
else:
    print("Not Balanced")