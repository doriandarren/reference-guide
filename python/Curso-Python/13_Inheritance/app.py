# class Parent:
#     def __init__(self):
#         pass

#     def hello(self):
#         print("Hi from Parent.")


# class Child(Parent):
#     def hello(self):
#         super().hello()
#         print("Hi from Child.")


# p = Parent()
# c = Child()
# c.hello()




### Listas:
    
import functools    
    
    
    
students = [
    ("Ana", 7),
    ("Luis", 9),
    ("Eva", 8)
]

ordered = sorted(students, key=lambda x: x[1], reverse=True)

print(ordered)
    


## Filter
numbers = [1, 2, 3, 4, 5, 6]

filtered = list(
    filter(
        lambda x: x % 2 == 0,
        numbers
    )
)
print(filtered)



## Map
result = list(
    map(
        lambda x: x * 2,
        numbers
    )
)

print(result)



## Reduce
res = functools.reduce(
    lambda a,b: a * b,
    numbers
)

print(res)





## Recursividad:


def countdown(n):
    if n == 0:
        print("Go!!!")
    else:
        print(n)
        countdown(n - 1)



countdown(3)