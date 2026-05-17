# Guida solo SAP



## Variables: 

```sh

DATA texto   TYPE string.
DATA numero  TYPE i.
DATA fecha   TYPE d.
DATA hora    TYPE t.
DATA importe TYPE p LENGTH 8 DECIMALS 2.


# Crear: 
DATA nombre TYPE string.
DATA nombre TYPE string VALUE 'Dorian'.

# inferencia de tipo
DATA(nombre) = 'Dorian'.
DATA(edad) = 25.


DATA: nombre TYPE string,
      apellido TYPE string,
      edad     TYPE i,
      salario  TYPE p LENGTH 8 DECIMALS 2.

```


## Constantes:

```sh

CONSTANTS pi TYPE p LENGTH 8 DECIMALS 2 VALUE 3.1416.

```


# Imprimir en pantalla:

```sh

# Imprimir en pantalla:
out->write( message ).
out->write( |Nombre: { nombre }| ).

```




# Project

```sh






```