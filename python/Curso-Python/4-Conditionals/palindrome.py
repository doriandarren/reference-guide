"""
Permitir al usuario ingresar una letra stringy comprobar si es un palíndromo
(es decir, que se lee igual de adelante hacia atrás que de atrás hacia adelante).

Ejemplo 1

Entrada del usuario:

racecar

Producción:

True

Ejemplo 2

Entrada del usuario:

hello

Producción:

False

Ejemplo 3

Entrada del usuario:

madam

Producción:

True
"""



string = input('Enter a string: ')

reversed_string = string[::-1]

print(string == reversed_string)