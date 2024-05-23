# Trabajo Práctico 8

## Ejercicio 1 - Sets

Tú y tus socios comerciales operan una pequeña empresa de catering. Acaban de acordar organizar un evento para un club de cocina local que presenta platos "favoritos del club". El club no tiene experiencia en la organización de eventos grandes y necesita ayuda con la organización, compra, preparación y servicio. Han decidido escribir algunos pequeños scripts en Python para acelerar todo el proceso de planificación.

### 1.1. Limpiar los ingredientes repetidos del plato
Las recetas del evento se agregaron desde diversas fuentes y parece que los ingredientes tienen entradas duplicadas (o más) -- ¡no quieres terminar comprando elementos en exceso!
Antes de que pueda comenzar la compra y la cocina, la lista de ingredientes de cada plato necesita ser "limpiada".

Implementa la función `clean_ingredients` que tome el nombre de un plato y una lista de ingredientes.

Esta función debería devolver una tupla con el nombre del plato como primer elemento, seguido por el conjunto depurado de ingredientes.

```python
>>> clean_ingredients('Punjabi-Style Chole', ['onions', 'tomatoes', 'ginger paste', 'garlic paste', 'ginger paste', 'vegetable oil', 'bay leaves', 'cloves', 'cardamom', 'cilantro', 'peppercorns', 'cumin powder', 'chickpeas', 'coriander powder', 'red chili powder', 'ground turmeric', 'garam masala', 'chickpeas', 'ginger', 'cilantro'])

>>> ('Punjabi-Style Chole', {'garam masala', 'bay leaves', 'ground turmeric', 'ginger', 'garlic paste', 'peppercorns', 'ginger paste', 'red chili powder', 'cardamom', 'chickpeas', 'cumin powder', 'vegetable oil', 'tomatoes', 'coriander powder', 'onions', 'cilantro', 'cloves'})
```


### 1.2 Clasificar Cócteles y Mocktails
El evento incluirá tanto cócteles como "mocktails" - bebidas mezcladas sin alcohol.
Necesitas asegurarte de que las bebidas "mocktail" sean verdaderamente no alcohólicas y que los cócteles realmente incluyan alcohol.

Implementa la función `check_drinks` que tome el nombre de una bebida y una lista de ingredientes.
La función debería devolver el nombre de la bebida seguido de "Mocktail" si la bebida no tiene ingredientes alcohólicos, y el nombre de la bebida seguido de "Cocktail" si la bebida incluye alcohol.
Para los propósitos de este ejercicio, los cócteles solo incluirán alcoholes del set ALCOHOLS en sets_categories_data.py:

```python
>>> from sets_categories_data import ALCOHOLS 

>>> check_drinks('Honeydew Cucumber', ['honeydew', 'coconut water', 'mint leaves', 'lime juice', 'salt', 'english cucumber'])
...
'Honeydew Cucumber Mocktail'

>>> check_drinks('Shirley Tonic', ['cinnamon stick', 'scotch', 'whole cloves', 'ginger', 'pomegranate juice', 'sugar', 'club soda'])
...
'Shirley Tonic Cocktail'
```


## Ejercicio 2 - Diccionarios 

En este ejercicio, administrarás un sistema de inventario.

El inventario debe estar organizado por el nombre del artículo y debe llevar un seguimiento del número de artículos disponibles.

Tendrás que gestionar la adición de artículos a un inventario. Cada vez que un artículo aparezca en una lista dada, aumenta la cantidad del artículo en `1` en el inventario. Luego, tendrás que gestionar la eliminación de artículos de un inventario.

Para finalizar, tendrás que implementar una función que devuelva todos los pares clave-valor en un inventario como una lista de `tuplas`.

### 2.1. Crear un inventario basado en una lista

Implementa la función `create_inventory` que crea un "inventario" a partir de una lista de artículos. Debe devolver un `dict` que contenga cada nombre de artículo emparejado con su cantidad respectiva.

```python
>>> create_inventory(["coal", "wood", "wood", "diamond", "diamond", "diamond"])
{"coal":1, "wood":2, "diamond":3}
```

### 2.2. Añadir artículos a partir de una lista a un diccionario existente

Implementa la función `add_items` que agrega una lista de artículos a un inventario:

```python
>>> add_items({"coal":1}, ["wood", "iron", "coal", "wood"])
{"coal":2, "wood":2, "iron":1}
```

### 2.3. Decrementar artículos del inventario

Implementa la función `decrement_items` que toma una `lista` de artículos. La función debe restar uno de la cantidad disponible en el inventario por cada vez que un artículo aparezca en la `lista`:

```python
>>> decrement_items({"coal":3, "diamond":1, "iron":5}, ["diamond", "coal", "iron", "iron"])
{"coal":2, "diamond":0, "iron":3}
```
Las cantidades de los artículos en el inventario no deben caer por debajo de 0. Si la cantidad de veces que un artículo aparece en la lista excede la cantidad disponible, la cantidad listada para ese artículo debe permanecer en 0 y las solicitudes adicionales para eliminar cantidades deben ser ignoradas.

```python
>>> decrement_items({"coal":2, "wood":1, "diamond":2}, ["coal", "coal", "wood", "wood", "diamond"])
{"coal":0, "wood":0, "diamond":1}
```

### 2.4. Eliminar por completo un artículo del inventario

Implementa la función `remove_item` que elimina un artículo y su cantidad completamente de un inventario:

```python
>>> remove_item({"coal":2, "wood":1, "diamond":2}, "coal")
{"wood":1, "diamond":2}
```
Si el artículo no se encuentra en el inventario, la función debe devolver el inventario original sin cambios.
```python
>>> remove_item({"coal":2, "wood":1, "diamond":2}, "gold")
{"coal":2, "wood":1, "diamond":2}
```

### 2.5. Devolver el contenido del inventario

Implementa la función `list_inventory` que toma un inventario y devuelve una lista de tuplas `(artículo, cantidad)`. La lista solo debe incluir los artículos disponibles (con una cantidad mayor a cero):

```python
>>> list_inventory({"coal":7, "wood":11, "diamond":2, "iron":7, "silver":0})
[('coal', 7), ('diamond', 2), ('iron', 7), ('wood', 11)]
```