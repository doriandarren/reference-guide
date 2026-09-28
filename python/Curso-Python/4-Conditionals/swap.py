"""
Intercambio

Dado un valor string, crea una nueva cadena donde se intercambien el primer y el último carácter. Hazlo en una sola línea de código (como máximo dos líneas si cuentas la declaración de la variable de cadena).

Puedes asumir que la longitud mínima de la cadena es 2.

Ejemplo 1

Aporte:

string: Python

Producción:

nythoP

Ejemplo 2

Aporte:

string: hello

Producción:

oellh

"""


#string = input('Enter a string: ')
string = 'hello'
print(string[-1] + string[1:-1] + string[0])