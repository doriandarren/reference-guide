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





```sh 

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

```



```sh 

numbers = [10, 20, 30, 40, 50]

del numbers[0]       # Elimina el primer elemento.
del numbers[-1]      # Elimina el último elemento.
del numbers[1:3]     # Elimina los elementos de los índices 1 y 2.

```