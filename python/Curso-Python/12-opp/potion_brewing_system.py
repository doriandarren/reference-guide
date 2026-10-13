"""
In the mystical land of Altheria, wizards brew various magical potions using specific ingredients. Each ingredient has a name and a potency level, which indicates its strength. Potions are created by combining these ingredients, and their overall strength is determined by the sum of the potency levels of all included ingredients.

Wizards have the ability to manage their potion-making process. They can store brewed potions in their potion cabinet and consume them when desired. A wizard can only brew a potion if they possess all the necessary ingredients, and they can only drink a potion if it is present in their cabinet.

The following classes are defined to implement this system:

Ingredient: Represents a potion ingredient with a name and potency level.
Potion: Represents a potion with a name and a list of ingredients. It includes an automatic method to calculate the potion's strength.
Wizard: Represents a wizard with a name, a collection of ingredients, and a potion cabinet. It includes methods to add ingredients, brew potions (adding them to the cabinet and removing the used ingredients), and drink potions (removing them from the cabinet).
Consider the necessary ingredients to brew a potion might not be available. Also, maybe the wizard wants to drink an elixir but it is not in the cabinet.


-----------------------




En la mística tierra de Altheria, los magos preparan diversas pociones mágicas con ingredientes específicos. 
Cada ingrediente tiene un nombre y un nivel de potencia, que indica su fuerza. Las pociones se crean combinando estos ingredientes, 
y su fuerza total se determina sumando los niveles de potencia de todos ellos.

Los magos tienen la capacidad de gestionar el proceso de elaboración de pociones. 
Pueden almacenar las pociones preparadas en su armario de pociones y consumirlas cuando lo deseen. 
Un mago solo puede preparar una poción si posee todos los ingredientes necesarios, y solo puede beberla si se encuentra en su armario.

Las siguientes clases se definen para implementar este sistema:

Ingrediente: Representa un ingrediente de poción con un nombre y un nivel de potencia.
Poción: Representa una poción con un nombre y una lista de ingredientes. Incluye un método automático para calcular la potencia de la poción.
Mago: Representa a un mago con nombre, una colección de ingredientes y un armario de pociones. Incluye métodos para añadir ingredientes, preparar pociones (añadiéndolos al armario y retirando los ingredientes usados) y beber pociones (retirándolas del armario).


Considera que los ingredientes necesarios para preparar una poción podrían no estar disponibles. 
Además, tal vez el mago quiera beber un elixir, pero no lo encuentre en el armario.










Example 1

Input:

herb = Ingredient("Herb", 5)

crystal = Ingredient("Crystal", 10)

elixir = Potion("Elixir", [herb, crystal])

print("Potion's strengh:", elixir.strength)

Output:

Potion's strengh: 15

Example 2

Output:

Merlin has brewed Elixir!

Example 3

Input:

merlin.drink(elixir)

Output:

Merlin drank Elixir!

Example 4

Input:

merlin.drink(elixir)

Output:

Merlin doesn't have Elixir in the cabinet.

Example 5

Input:

merlin.brew(Potion("Potion of Strength", [herb]))

Output:

Merlin doesn't have all the ingredients to brew Potion of Strength.


"""





# Your code goes here










# Example usage

herb = Ingredient("Herb", 5)
crystal = Ingredient("Crystal", 10)

elixir = Potion("Elixir", [herb, crystal])
print("Potion's strengh:", elixir.strength)

merlin = Wizard("Merlin")
merlin.add_ingredient(herb)
merlin.add_ingredient(crystal)

merlin.brew(elixir)
merlin.drink(elixir)

print(f"Ingredients left: {merlin.ingredients}.")