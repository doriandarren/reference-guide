# Notas Listas


```sh

students = ["Alice", "Bob", "Charlie"]


students.append("David")       # Añade un elemento al final.
students.insert(1, "John")      # Inserta un elemento en el índice 1.
students.extend(["Ana", "Tom"]) # Añade varios elementos al final.

students.remove("Bob")         # Elimina la primera aparición de "Bob".
students.pop()                 # Elimina y retorna el último elemento.
students.pop(1)                # Elimina y retorna el elemento del índice 1.
students.clear()               # Elimina todos los elementos.

students.index("Charlie")      # Retorna el índice de "Charlie".
students.count("Alice")        # Retorna cuántas veces aparece "Alice".

students.sort()                # Ordena la lista ascendentemente.
students.sort(reverse=True)    # Ordena la lista descendentemente.
students.reverse()             # Invierte el orden de los elementos.
students.copy()                # Retorna una copia superficial de la lista.


```





```sh
numbers = [5, 2, 8, 1, 3]

len(numbers)           # Retorna la cantidad de elementos -> 5
max(numbers)           # Retorna el valor máximo -> 8
min(numbers)           # Retorna el valor mínimo -> 1
sum(numbers)           # Retorna la suma -> 19

sorted(numbers)        # Retorna una nueva lista ordenada -> [1, 2, 3, 5, 8]
sorted(numbers, reverse=True)  # Orden descendente -> [8, 5, 3, 2, 1]

list(range(1, 6))      # Crea una lista -> [1, 2, 3, 4, 5]
list("Hello")          # Convierte un string -> ['H', 'e', 'l', 'l', 'o']

```



```sh 

students = ["Alice", "Bob", "Charlie", "David"]

students[0]       # Primer elemento -> "Alice"
students[1]       # Segundo elemento -> "Bob"
students[-1]      # Último elemento -> "David"
students[-2]      # Penúltimo elemento -> "Charlie"

students[1] = "John"  # Modifica "Bob" por "John".

```


# Slicing

```sh

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# SINTAXIS: lista[inicio:fin:paso]
# El índice fin NO está incluido.

numbers[0]                    # Primer elemento -> 0
numbers[-1]                   # Último elemento -> 9
numbers[-2]                   # Penúltimo elemento -> 8

numbers[2:5]                  # [2, 3, 4]
numbers[:5]                   # [0, 1, 2, 3, 4]
numbers[5:]                   # [5, 6, 7, 8, 9]
numbers[:]                    # Copia superficial de la lista.

numbers[-3:]                  # [7, 8, 9] -> Últimos 3.
numbers[:-3]                  # [0, 1, 2, 3, 4, 5, 6]
numbers[-5:-2]                # [5, 6, 7]

numbers[::2]                  # [0, 2, 4, 6, 8]
numbers[1::2]                 # [1, 3, 5, 7, 9]
numbers[::3]                  # [0, 3, 6, 9]

numbers[::-1]                 # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
numbers[::-2]                 # [9, 7, 5, 3, 1]
numbers[5:1:-1]               # [5, 4, 3, 2]

numbers[:len(numbers)//2]     # Primera mitad -> [0, 1, 2, 3, 4]
numbers[len(numbers)//2:]     # Segunda mitad -> [5, 6, 7, 8, 9]

numbers[2:8:2]                # [2, 4, 6]
numbers[8:2:-2]               # [8, 6, 4]



numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

numbers[2:5]      # Elementos del índice 2 al 4 -> [2, 3, 4]
numbers[:5]       # Primeros 5 elementos -> [0, 1, 2, 3, 4]
numbers[5:]       # Desde el índice 5 hasta el final.
numbers[-3:]      # Últimos 3 elementos -> [7, 8, 9]

numbers[::2]      # Elementos en índices pares -> [0, 2, 4, 6, 8]
numbers[1::2]     # Elementos en índices impares -> [1, 3, 5, 7, 9]
numbers[::-1]     # Retorna la lista invertida.
numbers[::3]      # Selecciona un elemento cada 3 posiciones.

numbers[:len(numbers)//2]  # Primera mitad.
numbers[len(numbers)//2:]  # Segunda mitad.



numbers = [10, 20, 30, 40, 50]

del numbers[0]       # Elimina el primer elemento.
del numbers[-1]      # Elimina el último elemento.
del numbers[1:3]     # Elimina los elementos de los índices 1 y 2.

```




# Tuplas (tuple)


```sh

numbers = (10, 20, 30, 20, 40)

numbers.count(20)              # Cuenta apariciones -> 2
numbers.index(30)              # Retorna el índice -> 2

len(numbers)                   # Cantidad de elementos -> 5
max(numbers)                   # Máximo -> 40
min(numbers)                   # Mínimo -> 10
sum(numbers)                   # Suma -> 120

numbers[0]                     # Primer elemento -> 10
numbers[-1]                    # Último elemento -> 40
numbers[1:3]                   # (20, 30)
numbers[::-1]                  # Invierte la tupla.

list(numbers)                  # Convierte a lista.
tuple([1, 2, 3])               # Convierte lista a tupla.



person = ("Alice", 25, "Barcelona")

name, age, city = person       # Desempaqueta la tupla.

a, b = (10, 20)                # a=10, b=20
a, b = b, a                   # Intercambia valores.

single = (5,)                  # Tupla de un elemento.

```



#  Sets (set)


```sh
numbers = {1, 2, 3, 4}

numbers.add(5)                 # Añade un elemento.
numbers.update([6, 7])         # Añade varios elementos.

numbers.remove(2)              # Elimina; error si no existe.
numbers.discard(2)             # Elimina; sin error si no existe.
numbers.pop()                  # Elimina un elemento arbitrario.
numbers.clear()                # Vacía el set.
numbers.copy()                 # Copia superficial.


A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

A.union(B)                     # {1, 2, 3, 4, 5, 6}
A | B                          # Unión.

A.intersection(B)              # {3, 4}
A & B                          # Intersección.

A.difference(B)                # {1, 2}
A - B                          # Elementos de A que no están en B.

B.difference(A)                # {5, 6}
B - A                          # Elementos de B que no están en A.

A.symmetric_difference(B)      # {1, 2, 5, 6}
A ^ B                          # Elementos no comunes.



numbers = [1, 2, 2, 3, 3, 4]

set(numbers)                   # {1, 2, 3, 4}
list(set(numbers))             # Elimina duplicados; orden no garantizado.
sorted(set(numbers))           # [1, 2, 3, 4]

set()                          # Crea un set vacío.
{}                             # Crea un diccionario vacío.

```



# Diccionarios (dict)


```sh 

student = {
    "name": "Alice",
    "age": 25,
    "grade": 9
}

student.keys()                 # Retorna vista de claves.
student.values()               # Retorna vista de valores.
student.items()                # Retorna vista de pares (clave, valor).

student.get("name")            # "Alice"
student.get("city")            # None si no existe.
student.get("city", "Unknown")  # Valor por defecto.

student.update({"age": 26})    # Actualiza o añade.
student.pop("age")             # Elimina clave y retorna valor.
student.popitem()              # Elimina último par insertado.
student.setdefault("city", "BCN") # Añade si no existe.

student.copy()                 # Copia superficial.
student.clear()                # Vacía el diccionario.



dic = {"Alice": 90, "Bob": 85}

dic["Alice"]                   # 90
dic["Charlie"] = 78            # Añade un elemento.
dic["Alice"] = 95              # Modifica un valor.

del dic["Bob"]                 # Elimina clave y valor.

"Alice" in dic                 # True
"David" not in dic             # True

len(dic)                       # Cantidad de claves.

dic = {"Alice": 90, "Bob": 85}

for key in dic:                # Recorre claves.
    print(key)

for value in dic.values():     # Recorre valores.
    print(value)

for key, value in dic.items(): # Recorre claves y valores.
    print(key, value)

```


# Strings (str)


```sh
text = "Hello Python"

text.lower()                   # "hello python"
text.upper()                   # "HELLO PYTHON"
text.capitalize()              # "Hello python"
text.title()                   # "Hello Python"
text.swapcase()                # "hELLO pYTHON"

text.strip()                   # Elimina espacios de extremos.
text.lstrip()                  # Elimina espacios izquierda.
text.rstrip()                  # Elimina espacios derecha.

text.replace("Python", "World") # Sustituye texto.
text.split()                   # ['Hello', 'Python']
text.split("o")                # Divide usando "o".
"-".join(["A", "B", "C"])        # "A-B-C"

text.find("Python")            # Índice -> 6
text.find("Java")              # -1 si no existe.
text.index("Python")           # Índice -> 6; error si no existe.
text.count("l")                # 2

text.startswith("Hello")       # True
text.endswith("Python")        # True


text = "Python"

text[0]                        # "P"
text[-1]                       # "n"
text[:3]                       # "Pyt"
text[3:]                       # "hon"
text[::-1]                     # "nohtyP"

len(text)                      # 6

"Py" in text                   # True
"Java" not in text             # True

```



# Funciones integradas (built-ins)


```sh
names = ["Alice", "Bob", "Charlie"]

for i, name in enumerate(names):
    print(i, name)             # Índice y elemento.

for i, name in enumerate(names, start=1):
    print(i, name)             # Empieza índice en 1.




numbers = [5, 2, 8, 1]

len(numbers)                   # Cantidad -> 4
max(numbers)                   # Máximo -> 8
min(numbers)                   # Mínimo -> 1
sum(numbers)                   # Suma -> 16
sorted(numbers)                # Ordena -> [1, 2, 5, 8]

abs(-10)                       # Valor absoluto -> 10
round(3.14159, 2)              # 3.14
pow(2, 3)                     # 8
divmod(10, 3)                  # (3, 1) cociente y resto.

int("25")                      # 25
float("3.5")                   # 3.5
str(25)                        # "25"
bool(1)                        # True

type(numbers)                  # <class 'list'>
isinstance(numbers, list)      # True


```



## enumerate()


```sh

names = ["Alice", "Bob", "Charlie"]

for i, name in enumerate(names):
    print(i, name)             # Índice y elemento.

for i, name in enumerate(names, start=1):
    print(i, name)             # Empieza índice en 1.

```


## zip()

```sh

names = ["Alice", "Bob"]
grades = [90, 85]

list(zip(names, grades))
# [('Alice', 90), ('Bob', 85)]

dict(zip(names, grades))
# {'Alice': 90, 'Bob': 85}

```


## Bucles:

```sh

numbers = [10, 20, 30]

for number in numbers:
    print(number)              # Recorre elementos.

for i in range(len(numbers)):
    print(numbers[i])          # Recorre por índices.

for i, number in enumerate(numbers):
    print(i, number)           # Índice y elemento.

```


# Agrupar listas

```sh
data = [("A", 1), ("A", 2), ("B", 3)]

dic = {}

for key, value in data:
    if key not in dic:
        dic[key] = []

    dic[key].append(value)

# {'A': [1, 2], 'B': [3]}
```


# Agrupar en diccionarios anidados

```sh

grades = [
    ("Math", "John", 88),
    ("Math", "Jane", 92)
]

dic = {}

for course, student, grade in grades:
    if course not in dic:
        dic[course] = {}

    dic[course][student] = grade

# {'Math': {'John': 88, 'Jane': 92}}

```

# Obtener números pares e impares

```sh
numbers = [1, 2, 3, 4, 5]

even = {n for n in numbers if n % 2 == 0}
odd = {n for n in numbers if n % 2 != 0}

# even = {2, 4}
# odd = {1, 3, 5}
```


# Encontrar pares que suman un número

```sh

numbers = [1, 2, 3, 4, 5]
target = 6

pairs = set()

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):

        if numbers[i] + numbers[j] == target:
            pair = tuple(sorted((numbers[i], numbers[j])))
            pairs.add(pair)

# {(1, 5), (2, 4)}

```



# Obtener elementos faltantes

```sh
n = 5
numbers = [0, 2, 4]

missing = sorted(set(range(n + 1)) - set(numbers))

# [1, 3, 5]

```


# Obtener números pares e impares


```sh

numbers = [1, 2, 3, 4, 5]

even = {n for n in numbers if n % 2 == 0}
odd = {n for n in numbers if n % 2 != 0}

# even = {2, 4}
# odd = {1, 3, 5}

```


# Agrupar en diccionarios anidados

```sh

grades = [
    ("Math", "John", 88),
    ("Math", "Jane", 92)
]

dic = {}

for course, student, grade in grades:
    if course not in dic:
        dic[course] = {}

    dic[course][student] = grade

# {'Math': {'John': 88, 'Jane': 92}}

```