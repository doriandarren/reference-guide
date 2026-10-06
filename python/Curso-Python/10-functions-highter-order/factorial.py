import functools

number = 0

lst_nb = [i for i in range(1, number + 1)]

result = functools.reduce(lambda a, b: a * b, lst_nb, 1) # 3er parametro en 1. Valor por defecto

print(f"{number}! = {result}")