# Fundamentos Python

## Notas

```sh

- __init__ es el constructor de la clase
- def = function se crea una función
- self = this refrencia a la clase - cuando se instancia (Instancia)
- cls = this referencia a la clase - cuando no se instancia (Estatico)


```

## Crear entorno virtual

```sh

## Crear
python3 -m venv .venv

## Activar
source .venv/bin/activate

## Actualizar
pip install --upgrade pip

##  Si no funcionan  VSCode:
( Cmd + Shift + P ) -> luego "Python: Select Interpreter" elegir ".venv/bin/python"


## Instalar paquetes

pip install requests        ## Conexion API
pip install schedule


```

## Listas / List - Arrays

```sh
list_numbers = [1, 2, 3, 4, 5]
list_letters = ['a', 'b', 'c']
list_mix = [2, 'z', True, [1, 2, 3], 5.5]
```

## Dictionaries - Objetos

```sh
user = {
    "name": "Richard",
    "age": 29,
    "email": "ricardo@gmail.com",
    "active": True,
    (19.12, -98.32): "Cancún Mexico"
}

user["name"] = "RAul"
user["age"] = 27
user["country"] = "México"

print(user)
print(user[(19.12, -98.32)])

# Values, items, keys
print(user.items())
print(user.values())
print(user.keys())


```

## Tuples

Son buenas para valores que inmutables. Ejemplos: dias de la semana

```sh
my_tuple = (1, 2, 3, 4, "Hola", True, False, 2, "hi", 3)

print(my_tuple.count(3))
#print(my_tuple.count("Hola"))

print(my_tuple.index(2))

## my_tuple[1] = 20 ## No se pueden mutar

```

## Sets

Su principal caracteristicas es que no permite duplicados

```sh
my_set = {1, 2, 3, 4, 5, 6, 7, 8, 5, 4, 3, 2, 2, 3}
print(my_set)

usernames = {"ricardo", "milena", "ferxo", "milena", "ferxo"}
print(usernames)

```

## For

```sh

for(int i=0; i<10;i++) es igual ---> for i in range(10):


for a in (5, 7, 11, 13):
    pass



for index, n in enumerate(list(range(70, 80))):
    print(index, n)

```

## While

```sh
counter = 1
while counter <= 5:
    print(f"Number: {counter}")
    counter += 1
else:
    print("Terminamos")




```

## Clase - Objeto

```sh
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        return f"{self.name} está trabajando duro."


person1 = Persona("Pepe", 29) ## Instanciando una clase

```