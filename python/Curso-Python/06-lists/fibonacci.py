n = 2

fibonacci = []
if n == 1:
    fibonacci = [0]
elif n >= 2:
    fibonacci = [0, 1]
    for i in range(2, n):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])

print(fibonacci)