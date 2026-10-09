"""
You’ve been hired to build the management system for the first Intergalactic Zoo — a facility that shelters alien species from all over the galaxy. Your task is to design a small Object-Oriented Program that models how the zoo tracks species, habitats, and breeding rules.

🎋 Classes and Responsibilities
Class AlienSpecies: represents an alien species in the zoo.
Each species should have:
species_id: a unique identifier.
name: the name of the species (e.g., "Zorgon", "Nebulon").
diet: what they eat (e.g., "Plasma Berries").
population: the number of individuals in the zoo.
min_population_to_breed: the minimum number of individuals required to reproduce.
offspring_range: a tuple (min_offspring, max_offspring) defining how many new individuals are born when breeding succeeds. See breed() method.
The class should include methods:

feed(): prints a message informing the species is eating their specific diet, for example: "Zorgons are eating Plasma Berries!".
breed(): increases the population by a random number between min_offspring and max_offspring, both included. The reproduction only takes place if the current population is at least min_population_to_breed, if not, display a message.


Class Habitat: represents an area in the zoo where alien species live.
Each habitat should have:
name: the habitat’s name (e.g., "CryoDome", "Lava Swamp").
capacity: the maximum total number of individuals that the habitat can support.
alien_species: the AlienSpecies living in the habitat. Each habitat has only one type of species living in there.
Methods:

add_species(species): adds a species to the habitat if it’s not already there and if total population does not exceed the capacity.
breed(): calls breed() on the species. Before breeding, check if the species’ current population plus the maximum possible offspring would exceed the habitat’s capacity.
If it would, breeding should not take place.
report(): prints all species with their population and diet, plus how much free space remains in the habitat.


Class Zoo: represents the overall intergalactic zoo.
It should:
Store all habitats in a list.
Be able to add new habitats with the add_habitat(habitat) method.
Generate a full report that displays information from all habitats with a report() method.
Feel free to consider and display warning messages for other possible problems we may encounter. For example, trying to add a species in an habitat that already has species.


----

Te han contratado para construir el sistema de gestión del primer Zoológico Intergaláctico , una instalación que alberga especies alienígenas de toda la galaxia. Tu tarea consiste en diseñar un pequeño programa orientado a objetos que modele cómo el zoológico realiza el seguimiento de las especies, los hábitats y las reglas de reproducción.

🎋 Clases y responsabilidades
ClaseAlienSpecies : representa una especie alienígena en el zoológico.
Cada especie debe tener:
species_id: un identificador único.
name: el nombre de la especie (p. ej., "Zorgon", "Nebulon").
diet: lo que comen (por ejemplo, "Bayas de plasma").
population: el número de individuos en el zoológico.
min_population_to_breed: el número mínimo de individuos necesarios para reproducirse.
offspring_range: una tupla (min_offspring, max_offspring)que define cuántos individuos nuevos nacen cuando la reproducción tiene éxito. Véase breed()método.
La clase debe incluir los siguientes métodos:

feed(): imprime un mensaje informando que la especie está comiendo su dieta específica, por ejemplo: "¡Los Zorgons están comiendo bayas de plasma!" .
breed(): incrementa la población en un número aleatorio entre min_offspringy max_offspring, ambos incluidos. 
La reproducción solo se realiza si la población actual es al menos min_population_to_breed, de lo contrario, muestra un mensaje.


ClaseHabitat : representa un área del zoológico donde viven especies exóticas.
Cada hábitat debe tener:
name: el nombre del hábitat (por ejemplo, "Criodomo", "Pantano de lava").
capacity: el número total máximo de individuos que el hábitat puede soportar.
alien_species: los AlienSpeciesque viven en el hábitat. Cada hábitat tiene solo un tipo de especie que vive allí.
Métodos:

add_species(species): agrega una especie al hábitat si aún no está allí y si la población total no excede la capacidad.
breed(): se deben considerar breed()las necesidades de la especie. Antes de la reproducción, compruebe si la población actual de la especie, sumada a la descendencia máxima posible, excedería la capacidad del hábitat.
De ser así, no se debería llevar a cabo la reproducción.
report(): Imprime todas las especies con su población y dieta, además de cuánto espacio libre queda en el hábitat.


ClaseZoo : representa el zoológico intergaláctico en general.
Debería:
Almacena todos los hábitats en una lista.
Con este método se podrán añadir nuevos hábitats add_habitat(habitat).
Generar un informe completo que muestre información de todos los hábitats con un report()método.
No dudes en considerar y mostrar mensajes de advertencia sobre otros posibles problemas que podamos encontrar. Por ejemplo, intentar agregar una especie en un hábitat que ya contiene especies.



"""


# Your code goes here

import random

#------------------------
# AlienSpecies
#------------------------
class AlienSpecies:

    def __init__(self, species_id, name, diet, population, min_population_to_breed, offspring_range):
        self.species_id = species_id
        self.name = name
        self.diet = diet
        self.population = population
        self.min_population_to_breed = min_population_to_breed
        self.offspring_range = offspring_range


    def feed(self):
        print(f"{self.name} are eating {self.diet}!")
    


    def breed(self):
        
        ma, mi = self.offspring_range

        print(ma, mi)


    

    def __str__(self):
        return f"{self.species_id} {self.name} {self.diet} {self.population} {self.min_population_to_breed} {self.offspring_range}"
    
    def __repr__(self):
        return f"{self.species_id} {self.name} {self.diet} {self.population} {self.min_population_to_breed} {self.offspring_range}"




#------------------------
# 
#------------------------











# Example usage

# Create alien species
zorgon = AlienSpecies(1, "Zorgon", "Plasma Berries", population=10,
                      min_population_to_breed=5, offspring_range=(2, 5))

nebun = AlienSpecies(2, "Nebulon", "Cosmic Dust", population=3,
                     min_population_to_breed=4, offspring_range=(1, 3))



zorgon.feed()
#print(zorgon)
#print(nebun)





# Create habitats
# cryo_dome = Habitat("CryoDome", capacity=20)
# lava_swamp = Habitat("Lava Swamp", capacity=15)

# Add species to habitats
# cryo_dome.add_species(zorgon)
# lava_swamp.add_species(nebun)

# Create zoo
# zoo = Zoo()
# zoo.add_habitat(cryo_dome)
# zoo.add_habitat(lava_swamp)

# Simulate actions
# zorgon.feed()

# cryo_dome.breed()
# cryo_dome.breed()
# cryo_dome.breed()

# Should not be able to breed because of min_population_to_breed
# lava_swamp.breed()

# zoo.report()