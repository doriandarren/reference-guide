# from functools import reduce

# print(reduce(lambda x, y: x + y, [1, 2, 3, 4]))


# print(list(filter(lambda x: x % 3 == 0, [1, 2, 3, 4, 5, 6])))


print(list(map(lambda x: x * 2, range(3))))



from functools import reduce
print(reduce(lambda x, y: x if x > y else y, [3, 7, 2, 5]))