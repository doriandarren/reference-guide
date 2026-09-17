"""
Que el usuario introduzca dos cadenas stringsy compruebe si son anagramas entre sí. Un anagrama se forma reordenando todas las letras de otra cadena, utilizando cada letra exactamente una vez. Ignore las mayúsculas y minúsculas, por lo que 'A' es lo mismo que 'a'. Los espacios también deben ignorarse.

Infórmate (investiga un poco) sobre las sorted()funciones integradas de Python y piensa en cómo utilizarlas para este ejercicio.

Ejemplo 1

Aporte:

string1: New York Times
string2: monkeys write

Producción:

True

Ejemplo 2

Aporte:

string1: Coronavirus
string2: carnivorous

Producción:

True

Ejemplo 3

Aporte:

string1: Python
string2: Pytho

Producción:

False
"""





#string1 = input('Enter a first string: ')
#string2 = input('Enter a second string: ')

#string1 = 'New York Times'
#string2 =  'monkeys write'

#string1 = 'Coronavirus'
#string2 = 'carnivorous'


string1 = 'Python'
string2 = 'Pytho'


string1_sorted = sorted(
    string1.lower().replace(' ', '')
)

string2_sorted = sorted(
    string2.lower().replace(' ', '')
)



print(string1_sorted == string2_sorted)