# Proyecto-final Curso Python, CODERHOUSE (comision 34650)

## *Presentación de proyecto*

 Base el proyecto en mi local favorito de hamburguesas "FIVE GUYS". El concepto de la tienda es vender hamburguesas premiun del tipo caseras y el cliente le puede agregar todos los toppings que quiera sin costo adicional. 
 
 La tienda se especializa en hamburguesas y solo ofrece un menu alternativo, hot dogs.Tambien venden papas fritas, postres y bebidas. El menu esta estandarizado, es decir, es fijo y siempre es el mismo en todos los diferentes locales y franquicias de la marca.

Realice los modelos productos (products), locales (location) y clientes (costumer). Luego tambien la aplicaciones usuarios (users).

La idea es que segun el nivel del usuario se vaya modificando los diferentes  accesos y funcionalidades.

Para un usuario sin logerse o un usuario basico del tipo cliente, solo estaran disponibles las visualizaciones generales de la marca, la del menu, la de los distintos puntos de venta y la posibilidade de registrarse.

Para un usuario intermedio del tipo 'staff' agregamos la posibilidad de visualizar el listado de clientes con sus datos personales como asi tambien la posibilidad de actualizar, agregar y borrar los mismos.

Para un usuario del mas alto nivel del tipo 'superuser' agregamos la posibilidad de sumar opcines al menu de comidas (aunque esta tienda como dije tiene  menu fijo), como asi tambien la posibilidad de agregar/actualizar/borrar locales o franquicias al listado de locales.

### Cómo ejecutar el proyecto
- Instalar Python
- Clonar el proyecto con ``` git clone github.com/JFGILI/Proyecto-final.git```
- Crear entorno virtual con `Pipenv` or `virtualenv` and activate it.
- Instalar los requerimientos
```
    pip install -r requirements.txt
```
- Arrastrar carpeta a Visual estudio code
- Ubicarse con cd y ls en la raiz (donde esta el manage.py)
- Ejecutar las migraciones
```
    $python manage.py makemigrations
    $python manage.py migrate
```
- Ejecutar el proyecto
```
    python manage.py runserver

# Desarrollador del proyecto:
## BackEnd
### | [Juan Francisco GILI TOMLIENOVICH ](https://www.linkedin.com/in/juan-francisco-gili-tomlienovich-30494b23a) | 
 [<img src=](https://github.com/JFGILI) 


