"""
Dado un número x, redondéalo al entero más cercano utilizando únicamente el +operador y la int()función.

No utilice la función integrada round(). El motivo de esta restricción es entrenar su pensamiento de programación: debe deducir usted mismo la lógica del redondeo, en lugar de depender de una herramienta integrada.

Ejemplo 1

Aporte:

x: 3.7

Producción:

4

Ejemplo 2

Aporte:

x: 2.3

Producción:

2

Ejemplo 3

Aporte:

x: 5.5

Producción:

6

"""


x = float(input("Enter a number: "))

result = int(x + 0.5)

print(result)