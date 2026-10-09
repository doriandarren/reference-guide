"""
You are building an inventory management system for a local store called MiniMart. The goal is to help the store track products, manage stock, and generate simple sales reports.

In this system, the MiniMart class is responsible for keeping track of how many units of each product are in stock. Each product itself only describes what it is and how much it costs.

Class Product: represents an item that can be sold by the store.
Each product should have:
product_id: a unique identifier.
name: the product’s name (e.g., "Apple").
price: the price per unit.
This class does not manage stock quantities — the store does.
* Class MiniMart: represents the store and manages:
+ The available products and their current quantities. The store keeps track of available products and their quantities using a dictionary. 
Each key is a product ID, and its value is another dictionary containing the product object under the key "product" and the current stock under the key "quantity"
+ Adding new products to the store inventory. Consider a product might already be in the store, so you should not be able to add it.
+ Selling products (reducing stock and increasing total revenue). When attempting to sell a product, if the requested quantity exceeds the available stock, 
the sale should be blocked — the stock should remain unchanged, and an error message should be displayed indicating insufficient stock. 
Also, display an error message if the product to be sold is not in the store.
+ Restocking products (increasing stock).
+ Generating sales reports that display total revenue and list products that are low in stock (less than 5 units).

Check the example code to see how the classes should work together.


---



Estás creando un sistema de gestión de inventario para una tienda local llamada MiniMart . 
El objetivo es ayudar a la tienda a realizar un seguimiento de los productos, gestionar el stock y generar informes de ventas sencillos.

En este sistema, la clase MiniMart se encarga de llevar un registro de cuántas unidades de cada producto hay en stock.
Cada producto solo describe qué es y cuánto cuesta.

ClaseProduct : representa un artículo que puede ser vendido por la tienda.
Cada producto debe tener:
product_id: un identificador único.
name: el nombre del producto (por ejemplo, "Apple").
price: el precio por unidad.
Esta clase no gestiona las cantidades de stock; lo hace la tienda.


* ClaseMiniMart : representa la tienda y gestiona:
+ Los productos disponibles y sus cantidades actuales. La tienda realiza un seguimiento de los productos disponibles y sus cantidades mediante un diccionario. 
Cada clave es un ID de producto, y su valor es otro diccionario que contiene el objeto del producto bajo la clave "producto" y el stock actual bajo la clave "cantidad".

+ Agregar nuevos productos al inventario de la tienda. Considere que un producto podría estar ya en la tienda, por lo que no debería poder agregarlo.

+ Vender productos (reducir el stock y aumentar los ingresos totales). Al intentar vender un producto, si la cantidad solicitada excede el stock disponible, 
la venta debe bloquearse; el stock debe permanecer sin cambios y debe mostrarse un mensaje de error que indique stock insuficiente. 
También, muestre un mensaje de error si el producto que se va a vender no está en la tienda.

+ Reabastecer productos (aumentar el stock).
+ Generar informes de ventas que muestren los ingresos totales y enumeren los productos que tienen poco stock (menos de 5 unidades).

Consulta el código de ejemplo para ver cómo deberían funcionar las clases en conjunto

"""

# Your code goes here
# Example usage


#------------------------
# Product
#------------------------
class Product:

    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.product_id} {self.name} {self.price}"
    
    def __repr__(self):
        return f"Product({self.product_id}, {self.name}, {self.price})"





#------------------------
# MiniMart
#------------------------
class MiniMart:

    def __init__(self):
        self.stock_dic = {}
        self.total_revenue = 0.0


    def add_product(self, product, quantity):
        ## print(product, quantity)

        if product.product_id not in self.stock_dic:
            self.stock_dic[product.product_id] = {
                "product": product,
                "quantity": quantity
            }
        else:
            print("Product already exists.")
        

    def sell_product(self, product_id, quantity):
        
        if product_id in self.stock_dic:
            dic = self.stock_dic[product_id]
            stock_product = dic["product"]
            stock_quantity = dic["quantity"]

            if stock_quantity < quantity:
                print(f"Product {stock_product.name} have insufficient stock. Stock: {stock_quantity}")
                return

            dic["quantity"] -= quantity
            self.total_revenue += quantity * stock_product.price

        else:
            print(f"Product with ID: {product_id} not available.")


    
    def restock_product(self, product_id, quantity):
        if product_id in self.stock_dic:
            dic = self.stock_dic[product_id]
            stock_product = dic["product"]
            dic["quantity"] += quantity
            print(f"Product: {stock_product.name} restock done! Stock: {dic["quantity"]}")
        else:
            print(f"Product with ID: {product_id} not available.")



    def generate_sales_report(self):
        report = f"""
------------------------
        Report
------------------------
Total revenue: {self.total_revenue:.2f}

Stock < 5:

"""
        
        for product_id, dic in self.stock_dic.items():
            stock_product = dic["product"]
            stock_quantity = dic["quantity"]

            if stock_quantity < 5:
                report += f"Product {stock_product.name} - Stock: {stock_quantity}\n"
        
        print(report)
        

    def __str__(self):
        return f"{self.stock_dic}"
    
    def __repr__(self):
        return f"{self.stock_dic}"







# Create products
apple = Product(1, "Apple", 0.5)
banana = Product(2, "Banana", 0.3)
orange = Product(3, "Orange", 0.75)

# Create the store
store = MiniMart()

# Add products with initial stock
store.add_product(apple, 100)
store.add_product(banana, 50)
store.add_product(orange, 5)


# Sell some products
store.sell_product(apple.product_id, 20)
store.sell_product(banana.product_id, 48)
store.sell_product(orange.product_id, 2)



# Restock oranges
store.restock_product(orange.product_id, 10)

# Attempt to add an existing product
store.add_product(apple, 30)  # Should not add again


# Attempt to sell more than available
store.sell_product(orange.product_id, 50)  # Error message of insufficient stock
melon = Product(4, "Melon", 1.5)
store.sell_product(melon.product_id, 4)  # Error message of product not available

store.generate_sales_report()
