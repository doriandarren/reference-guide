# n = 2

# fibonacci = []
# if n == 1:
#     fibonacci = [0]
# elif n >= 2:
#     fibonacci = [0, 1]
#     for i in range(2, n):
#         fibonacci.append(fibonacci[-1] + fibonacci[-2])

# print(fibonacci)





def fibonacci(n):


    n = 2
    fibonacci_lst = []

    if n == 1:
        fibonacci_lst = [0]
    elif n >= 2:
        fibonacci_lst = [0, 1]

        for i in range(2, n):
            fibonacci_lst.append(fibonacci_lst[-1] + fibonacci_lst[-2])

    return fibonacci_lst



n = 2
lst = fibonacci(n)

print(lst)
