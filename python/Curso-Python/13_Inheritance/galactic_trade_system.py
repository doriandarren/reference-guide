"""
Eres desarrollador de software para el Consejo Galáctico, encargado de crear un sistema automatizado para gestionar el comercio interplanetario entre diversos planetas. El sistema simula las visitas de naves espaciales a los planetas, la compra y venta de recursos, y la gestión de la capacidad de carga y las restricciones financieras.

Clase:Planet
Representa un planeta que ofrece diversos recursos a la venta a precios fijos.

Atributos:
name(str): Nombre del planeta.
resources(dict[str, int]): Un mapeo de nombres de recursos a su precio por unidad en el planeta.
Métodos:
add_resource(resource: Resource, price: int): Agrega un recurso al mercado del planeta con un precio específico por unidad.


Clase:Spaceship
Representa una nave espacial comercial capaz de visitar planetas, comprar y vender recursos, y gestionar la carga y las finanzas.

Atributos:
name(str): Nombre de la nave espacial.
captain(str): Nombre del capitán.
capacity(int): Peso total máximo que puede transportar la nave espacial.
money(int): Cantidad actual de dinero que tiene la nave espacial.
inventory(dict[str, int]): Asignación de nombres de recursos a la cantidad almacenada.
current_planet(Planeta | Ninguno): El planeta en el que se encuentra actualmente atracada la nave espacial.
Métodos:
visit_planet(planet: Planet)Actualiza la ubicación de la nave espacial.
buy_resource(resource: Resource, amount: int): Intenta comprar una cantidad específica de un recurso del planeta actual (dada por el método ejecutado previamente) visit_planet, imponiendo restricciones de capacidad y dinero.
sell_resource(resource: Resource, amount: int = 1): Vende una cantidad específica de un recurso al planeta actual, lo que obliga a realizar comprobaciones de inventario.
inventory_value() → intCalcula el valor total del inventario basándose en los precios actuales del planeta.


Clase:Resource
Representa un tipo de recurso comercializable.

Atributos:
name(str): Nombre del recurso (por ejemplo, "Oro").
weight(int): Peso por unidad del recurso.
Nota: En los diccionarios de planetas y naves espaciales solo se utiliza el nombre del recurso.

Asumir
Todos los recursos deben estar disponibles en todos los planetas para ser comprados y vendidos.
La cantidad de cada recurso por planeta es infinita.
Se aplican las normas comerciales.
La nave espacial debe tener capacidad suficiente (en peso) para comprar un recurso.
La nave espacial debe tener suficiente dinero para cubrir el costo total.
Los recursos solo se pueden vender si están presentes en el inventario de la nave espacial.
No está permitido vender más de lo que se posee.
Los precios pueden variar entre planetas para un mismo recurso.



"""

#-----------------
# Resource
#-----------------
class Resource:
    """Representa un tipo de recurso comercializable."""
    
    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight
    
    
    def __str__(self):
        return f"{self.name} {self.weight}"
    
    def __repr__(self):
        return f"{self.name} {self.weight}"



#-----------------
# Resource
#-----------------
class Planet:
    """Representa un planeta que ofrece diversos recursos a la venta a precios fijos."""
    def __init__(self, name: str):
        self.name = name
        self.resources: dict[str, int] = {}
    
    
    def add_resource(self, resource: Resource, price: int):
        if resource.name not in self.resources:
            self.resources[resource.name] = price
        else:
            price_temp = self.resources[resource.name]
            self.resources[resource.name] = price_temp + price
        
        
    
    
    
    def __str__(self):
        return f"{self.name} {self.resources}"
    
    def __repr__(self):
        return f"{self.name} {self.resources}"



#-----------------
# Spaceship
#-----------------
class Spaceship:
    """Representa una nave espacial comercial capaz de visitar planetas, comprar y vender recursos, y gestionar la carga y las finanzas."""
    
    
    def __init__(
        self,
        name: str,
        captain: str,
        capacity: int,
        money: int
    ):
        
        
        self.inventory: dict[str, int] = {}
        self.current_planet: (Planet | None) = None
    
    
    
    
    def __str__(self):
        return f""
    
    def __repr__(self):
        return f""
    




# Resources
gold = Resource("Gold", 10)
silver = Resource("Silver", 5)
water = Resource("Water", 1)



# Planets with different prices
earth = Planet("Earth")
mars = Planet("Mars")
venus = Planet("Venus")

earth.add_resource(gold, 1000)
earth.add_resource(silver, 500)
earth.add_resource(water, 50)


mars.add_resource(gold, 800)
mars.add_resource(silver, 550)
mars.add_resource(water, 20)

venus.add_resource(gold, 1200)
venus.add_resource(silver, 480)
venus.add_resource(water, 100)

print(earth)
print(mars)
print(venus)


# Spaceships
falcon = Spaceship("Falcon", "Han Solo", capacity=1000, initial_money=5000)
enterprise = Spaceship("Enterprise", "Picard", capacity=3000, initial_money=10000)

# === Falcon trades on Earth ===
# falcon.visit_planet(earth)

# Try to buy 10 gold → too expensive
# falcon.buy_resource(gold, 10)  # 10000 > 5000, should fail
# assert "Gold" not in falcon.inventory

# Buy 2 gold (2000) → should work
# falcon.buy_resource(gold, 2)
# assert falcon.inventory["Gold"] == 2
# assert falcon.money == 5000 - 2 * 1000
# assert falcon.capacity == 1000 - 2 * 10

# Buy 10 water (500) → should fail (500 > 3000 left)
# falcon.buy_resource(water, 10)  # 500 > 3000 left, money is only 3000, so OK
# assert falcon.inventory["Water"] == 10
# assert falcon.money == 3000 - 10 * 50
# assert falcon.capacity == 1000 - (2 * 10 + 10 * 1)

# === Falcon sells on Mars ===
# falcon.visit_planet(mars)

# Sell 1 gold (800 income)
# falcon.sell_resource(gold, 1)
# assert falcon.inventory["Gold"] == 1
# assert falcon.money == 3000 - 500 + 800
# assert falcon.capacity == 1000 - (1 * 10 + 10 * 1)

# Try to sell more silver than you own
# falcon.sell_resource(silver, 1)  # should print warning

# === Enterprise trades on Mars ===
# enterprise.visit_planet(mars)

# Buy 5 gold (4000) → should work
# enterprise.buy_resource(gold, 5)
# assert enterprise.inventory["Gold"] == 5
# assert enterprise.money == 10000 - 5 * 800
# assert enterprise.capacity == 3000 - 5 * 10

# Buy 200 water (4000) → should work
# enterprise.buy_resource(water, 200)
# assert enterprise.inventory["Water"] == 200
# assert enterprise.capacity == 3000 - (5 * 10 + 200 * 1)
# assert enterprise.money == 10000 - 5 * 800 - 200 * 20

# === Inventory value checks ===
# enterprise.visit_planet(venus)
# Gold: 1200 * 5, Water: 100 * 200
# assert enterprise.inventory_value() == 5 * 1200 + 200 * 100



# === Selling water ===
# enterprise.sell_resource(water, 50)
# assert enterprise.inventory["Water"] == 150
# assert enterprise.money == (
#     10000 - 5 * 800 - 200 * 20 + 50 * 100
# )
# assert enterprise.capacity == 3000 - (5 * 10 + 150 * 1)

# print("✅ All tests passed.")