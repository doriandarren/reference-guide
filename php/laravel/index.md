# Configuración Plesk

```sh

- Crear subdominio en Ionos
- Crear subdominio en plesk
- Configurar certificados SSL en plesk
- Clonar y configurar el git
- Agregar Webhook Plesk -> GitHub
- Añadir base de datos en plesk

- Conectar via ssh:
composer install
cp .env.example .env
php artisan key:generate
php artisan config:clear
php artisan migrate
php artisan migrate:fresh --seed

```

## Para debugar en PHP:

```sh
## Se puede hacer: (Inspeccionar variables)
<?php var_dump($tasks) ?>
```

## LARAVEL class

```sh

dd($variable_a_debugar);                ## Para debugar variables


## Crear una instancia de una clase:
$obj = new DB();
$obj->llamadaMetodo();

## Llamada método statico
DB::llamadaMetodo();


```

# Larave Eloquent - ORM

```sh

->get();                                ## Retorna un array
->first();                              ## Retorna un objeto


```

## Comandos artisan:

```sh

php artisan make:migration              ## Para crear migración
php artisan migrate                     ## Para ejecutar la migración
php artisan migrate:fresh               ## Para ejecutar la migración y borra los registros de la DB
php artisan migrate:fresh --seed        ## Para ejecutar la migración y borra los registros de la DB


php artisan make:model                  # Crea modelo
php artisan make:controller             # Crea Controller
php artisan make:request                # Crea Form Request


php artisan make:notifications-table    # Crea la tabla de notifications (no la migra a la DB, luego se hace el "migrate")

php artisan make:notification           # Crea una clase Notification (IdeaPublished)



php artisan config:clear                # Borra configuracion del .env si se modifica


php artisan queue:work                  # Colas de trabajos
php artisan make:job                    # Crea Colas de trabajos



```

## LCRUD

```sh

index           -> Muestra la lista de registros (Todos, filtro, etc)
show            -> Muentra UN dato
create          -> Muetra la vista (Formulario para creación)
store           -> Guarda datos del create (Unido con create)
edit            -> Muestra la vista (Formulario para editar)
update          -> Actuliza los datos de edit (Unido con edit)
destory         -> Elimina UN dato (Unido con index)

```

# Pest

```sh
./vendor/bin/pest tests/Browser/AuthTest.php


./vendor/bin/pest tests/Unit/IdeaTest.php
```
