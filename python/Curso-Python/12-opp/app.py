
# class Product():

#     # Construct
#     def __init__(self, name, quantity=1) -> None:
#         self.name = name
#         self.quantity = quantity
#         self.active = True

#     def update_stock(self, amount):
#         self.quantity += amount
#         print(f"Quantity: {self.quantity}")


# p1 = Product("Cake")
# p2 = Product("Cepillos")


# print(p1.name)
# print(p1.quantity)
# print(p1.update_stock)




class A:
    def __init__(self, x=5):
        self.x = x

a = A(10)
print(a.x)
