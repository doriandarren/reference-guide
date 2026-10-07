# Your code goes here

class Product():

    def __init__(self, product_id, product_name, product_price):
        self.product_id = product_id
        self.product_name = product_name
        self.product_price = product_price

    
    def display_product_info(self):
        print(f"""
Product Details
ID: {self.product_id}
Name: {self.product_name}
Price: {self.product_price}
""")
    
    def __repr__(self):
        return f"{self.product_id} - {self.product_name} - {self.product_price}€"



class ShoppingCart():

    def __init__(self):
        self.products = []
        self.total = 0


    def add_product(self, product, count):
        for i in range(count):
            self.products.append(product)

        self.total += product.product_price * count


    def remove_product(self, product_id, count):

        filtered_lst = list(filter( lambda p: p.product_id == product_id, self.products))

        for p in filtered_lst[:count]:
            self.products.remove(p)
            self.total -= p.product_price


    def total_cost(self):
        return self.total





# Example usage

# Create products
apple = Product(1, "Apple", 0.5)
banana = Product(2, "Banana", 0.3)

#orange = Product(3, "Orange", 0.6)


# Create cart and add items
cart = ShoppingCart()
cart.add_product(apple, 4)  # 4 apples
cart.add_product(banana, 3)  # 3 bananas

#cart.add_product(orange, 2)



# Remove 2 apples (apples have ID 1 as defined above in the product)
cart.remove_product(1, 2)


# Display total cost
print(f"Total cost: {cart.total_cost():.2f}€")