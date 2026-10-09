class Parent:
    def __init__(self):
        pass

    def hello(self):
        print("Hi from Parent.")


class Child(Parent):
    def hello(self):
        super().hello()
        print("Hi from Child.")


p = Parent()
c = Child()
c.hello()