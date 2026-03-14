# SAP



## Variables: 

```sh

DATA texto   TYPE string.
DATA numero  TYPE i.
DATA fecha   TYPE d.
DATA hora    TYPE t.
DATA importe TYPE p LENGTH 8 DECIMALS 2.


# Crear: 
DATA nombre TYPE string.



# Usar:
out->write( message ).
out->write( |Nombre: { nombre }| ).

```