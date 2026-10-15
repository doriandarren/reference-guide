# Notas:

Tuple: (1) ->>>> ERROR




# 

```sh

## Recorrer Filas:

for row in sudoku:
        if set(row) != numbers:
            return False


## Recorrer columnas:

for j in range(9):
    for i in range(9):
        square.append(sudoku[i][j])

```


zip





# Listas:

```sh 

lista = ["Ana", "Bob"]


# Acceder
lista[0]


# Añadir:
lista.append("Pepe")
lista.insert(0, "Eva")

# Eliminar
lista.remove("Ana")     # Por Valor
lista.pop(0)            # Por Indice
del lista[0]            # Por indice

# Recorrer
for x in lista:
    print(x)


# Buscar

"Ana" in lista          # True o False

```



# dic

```sh

dic = {"name": "Ana", "age": 20}


# Acceder
dic["name"]
dic.get("name", "Defaul")


# Añadir:
dic["city"] = "Barcelona"
dic["age"] = 28


# Eliminar
del dic["age"]
dic.pop("name")


# Recorrer

for key, value in dic.items():
    print(key, value)



# Buscar
"name" in dic       # True o False

```



# tupla

```sh
tupla = ("Ana", "Bob", "Luis")
vacia = ()
una = ("Ana",)


# Acceder
tupla[0]                # Ana
tupla[-1]               # Luis


# Eliminar
# No permite append() ni insert()
del tupla               # Elimina la variable completa


# Recorrer
for x in tupla:
    print(x)



# Buscar
"Ana" in tupla
tupla.index("Bob")
tupla.count("Ana")


```








