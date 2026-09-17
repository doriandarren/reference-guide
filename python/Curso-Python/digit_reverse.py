"""
Permita que el usuario ingrese un número integerde cualquier cantidad de dígitos e imprima el número con sus dígitos invertidos. Antes de imprimir, almacene el resultado en una variable que debe ser de tipo int.

Ejemplo 1

Entrada del usuario:

1234

Producción:

4321

Ejemplo 2

Entrada del usuario:

7001

Producción:

1007

Ejemplo 3

Entrada del usuario:

10

Producción:

1

"""






integer = input('Enter an integer: ')
integer_reversed = int(integer[::-1])
print(integer_reversed)