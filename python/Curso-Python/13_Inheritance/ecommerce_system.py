"""
Design a basic e-commerce system that includes products, a store, and a shopping cart.

The system consists of a Product base class with attributes such as product_id, name, and price.

Two subclasses inherit from Product: Electronics, which has an additional warranty attribute, and Clothing, which includes a size attribute.

The Store class manages a dictionary of products, where keys are product IDs and values are the quantities available. It includes methods to add and remove stock, ensuring that stock levels do not fall below zero.

The Cart class allows customers to add products from the store, remove products, view the cart contents, and finalize purchases, which updates the stock in the store accordingly.


-------



Diseña un sistema básico de comercio electrónico que incluya productos, una tienda y un carrito de compras.

El sistema consta de una Product clase base con atributos como product_id, name, y price.

Dos subclases heredan de Product: , que tiene un atributo Electronics adicional , y , que incluye un atributo.warrantyClothingsize

La Storeclase gestiona un diccionario de productos, donde las claves son los identificadores de producto y los valores son las cantidades disponibles. Incluye métodos para añadir y eliminar existencias, garantizando que los niveles de stock no caigan por debajo de cero.

Esta Cartclase permite a los clientes añadir productos de la tienda, eliminarlos, ver el contenido del carrito y finalizar las compras, lo que actualiza el stock de la tienda en consecuencia.


"""





# Your code goes here


#------------------
# Product
#------------------
class Product:
    
    def __init__(self, product_id, name, price):
        self.product_id = product_id 
        self.name = name
        self.price = price




#------------------
# Electronics
#------------------
class Electronics(Product):
    
    def __init__(self, product_id, name, price, warranty):
        super().__init__(product_id, name, price)
        self.warranty = warranty
    
    
    def __repr__(self):
        return f"{self.product_id} {self.name} {self.price} {self.warranty}"

    
    


#------------------
# Clothing
#------------------
class Clothing(Product):
    
    def __init__(self, product_id, name, price, size):
        super().__init__(product_id, name, price)
        self.size = size


    def __repr__(self):
        return f"{self.product_id} {self.name} {self.price} {self.size}"



#------------------
# Store
#------------------
class Store:
    
    def __init__(self):
        self.products = {} ## key = clave producto y value = cantidad disponibles


    def add_stock(self, product_id, quantity):
        
        if quantity <= 0:
            print("Quantity debe ser mayor a cero.")
            return
        
        if product_id not in self.products:
            self.products[product_id] = quantity
        else:
            self.products[product_id] += quantity
    
        
    def __repr__(self):
        return f"Store: {self.products}"
    

#------------------
# Cart
#------------------
class Cart:
    
    def __init__(self):
        self.items = {}
        
    
    def add_product(self, store, product, quantity=1):
        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return

        if product.product_id not in store.products:
            print(f"The product {product.name} does not exist.")
            return

        store_quantity = store.products[product.product_id]
        cart_quantity = self.items.get(product, 0)

        if cart_quantity + quantity > store_quantity:
            print("Not enough stock available.")
            return

        if product not in self.items:
            self.items[product] = quantity
        else:
            self.items[product] += quantity
        
        
        
        
    def remove_product(self, product, quantity=1):

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return

        if product not in self.items:
            print(f"The product {product.name} is not in the cart.")
            return

        cart_quantity = self.items[product]

        if cart_quantity <= quantity:
            del self.items[product]
        else:
            self.items[product] -= quantity
            
            
    
    def view_cart(self):    
        print("-" * 30)
        print("Shopping Cart")
        print("-" * 30)

        if not self.items:
            print("Your cart is empty.")
            return

        for product, quantity in self.items.items():
            print(f"{product.name} | Quantity: {quantity}")
        
        
    def checkout(self, store):
        """Complete the purchase and update store stock."""

        if not self.items:
            print("Your cart is empty.")
            return

        total = 0

        # Comprobar que todos los productos tienen stock
        for product, quantity in self.items.items():

            available_stock = store.products.get(product.product_id, 0)

            if quantity > available_stock:
                print(f"Not enough stock for {product.name}.")
                return

        # Calcular total y descontar stock
        for product, quantity in self.items.items():

            total += product.price * quantity

            store.products[product.product_id] -= quantity

        # Vaciar carrito
        self.items.clear()

        print(f"Total paid: {total:.2f}€")
    
    
    
    
    def __repr__(self):
        return f"Cart: {self.items}"




# Example usage

# Create products
iphone = Electronics(1, "iPhone", 999.99, "1 year")
shirt = Clothing(2, "Shirt", 29.99, "L")
laptop = Electronics(3, "Laptop", 1299.99, "2 years")

# Create store and add stock
store = Store()
store.add_stock(iphone.product_id, 10)
store.add_stock(shirt.product_id, 15)
store.add_stock(laptop.product_id, 5)



# Create a cart and add products to it
cart = Cart()
cart.add_product(store, iphone, 2)  # Add 2 iPhones to cart
cart.add_product(store, shirt, 3)   # Add 3 shirts to cart
cart.add_product(store, laptop)     # Add 1 laptop to cart


print(cart)

# Remove a product from the cart
cart.remove_product(shirt, 1)  # Remove 1 shirt from the cart

print(cart)

# View updated cart
cart.view_cart()

# Checkout and finalize purchase
cart.checkout(store)
# Expected output:
#   Total paid: 3359.95€

# Check remaining stock in the store
print("Remaining stock:")
print("- iPhones:", store.products[1])  # 8 (2 iPhones were purchased)
print("- Shirts:", store.products[2])  # 13 (2 shirts were purchased)
print("- Laptops:", store.products[3])  # 4 (1 laptop was purchased)