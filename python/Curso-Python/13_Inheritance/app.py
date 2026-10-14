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



class AError(Exception): pass
class BError(AError): pass

try:
    raise BError("problem")
except AError:
    print("Caught A Error")
except BError:
    print("Caught B Error")