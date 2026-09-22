"""
--------------------------- COLECCIONES ---------------------------
En este taller aprenderás a manipular coleccciones de datos: Listas, diccionarios, tuplas y sets.
"""

"""
 --- LISTAS ---
Las listas son ordenadas y mutables.
Pueden contener elementos duplicados.
Puedes modificar, añadir y eliminar elementos.
"""
"""
--- Ejercicio 1 Listas ---
Crea una variable "mascotas" que almacene una lista con los siguientes elementos: 'perro', 'gato', 'loro'
Imprime por consola el valor almacenado
Despues haz los pasos pedidos
"""
# Escribe tu código aquí
mascotas = ['perro', 'gato', 'loro']
print(mascotas)

# Escribe el código para saber la cantidad de elementos que tiene la lista, imprimir por consola
print(len(mascotas))

# Escribe el código para acceder al valor de la posición 2, imprimir por consola
print(mascotas[1])

# Escribe el código para agregar una elemento a la lista, imprimir por consola la lista
mascotas.append('pez')
print(mascotas)

# Escribe el código para modificar un elemento de la lista, imprimir por consola la lista
mascotas[0] = 'hámster'
print(mascotas)

# Escribe el código para eliminar un elemento de la lista, imprimir por consola la lista
mascotas.remove('gato')
print(mascotas)


"""
 --- TUPLAS ---
Las tuplas son ordenadas e inmutables.
Pueden contener elementos duplicados.
No puedes modificar, añadir o eliminar elementos después de la creación.
"""

"""
--- Ejercicio 2 Tuplas ---
Crea una variable "plantas" que almacene una tupla con los siguientes elementos: 'cactus', 'orquidea', 'rosas'
Imprime por consola el valor almacenado
Despues haz los pasos pedidos
"""
# Escribe tu código aquí
plantas = ('cactus', 'orquidea', 'rosas')
print(plantas)

# Escribe el código para saber la cantidad de elementos que tiene la tupla, imprimir por consola
print(len(plantas))

# Escribe el código para acceder al valor de la posición 2, imprimir por consola
print(plantas[1])

# Intentar modificar una tupla
# plantas[1] = 'hoja rota'  # Descomenta esta línea para ver qué sucede

# Escribe tu análisís acá acerca de qué sucede
# Si descomentamos la línea, salta un error ("TypeError").
# Las tuplas son inmutables, por lo tanto no podemos cambiar sus elementos una vez creadas.


"""
 --- SETS ---
Los sets son desordenados y mutables.
No pueden contener elementos duplicados.
Puedes añadir y eliminar elementos, pero no puedes modificar los elementos existentes.
"""

"""
--- Ejercicio 3 Sets ---
Crea una variable "nombres" que almacene un set con los siguientes elementos: 'María', 'Cris', 'Cris', 'Alex'
Imprime por la terminal dicha variable
Haz los pasos pedidos
"""
# Escribe el código aqui
nombres = {'María', 'Cris', 'Cris', 'Alex'}
print(nombres)

# Explica qué sucede cuándo imprimes el valor que almacena "nombres"
# El set descarta los duplicados automáticamente. 'Cris' solo aparece una vez. 
# Además, el orden de los elementos puede variar.

# Escribe el código para saber la cantidad de elementos que tiene el set, imprimir por consola
print(len(nombres))

# Escribe el código para acceder al valor de la posición 3, imprimir por consola
print(list(nombres)[2])

# Escribe el código para agregar una elemento al set, imprimir por consola el set
nombres.add('Juan')
print(nombres)

# Escribe el código para eliminar un elemento del set, imprimir por consola el set
nombres.remove('María')
print(nombres)

"""
 --- DICCIONARIOS ---
Los diccionarios son desordenados y mutables.
Contienen pares clave-valor.
Puedes añadir, modificar y eliminar pares clave-valor.
"""

"""
--- Ejercicio 4 Diccionarios ---
Crea un diccionario llamado "ciudad" con las claves 'nombre' y 'pais' y los valores 'Barcelona' y 'España' respectivamente.
Imprime el diccionario 
"""
ciudad = {'nombre': 'Barcelona', 'pais': 'España'}
print(ciudad)

# Escribe el código aqui para acceder y ver por consola el valor de 'nombre'
print(ciudad['nombre'])

# Escribe el código aqui para añadir un nuevo par clave-valor y ver por consola el valor de 'ciudad'
ciudad['poblacion'] = 1620000
print(ciudad)

# Escribe el código aqui para modificar el valor de un par clave-valor de 'ciudad' y verlo por consola
ciudad['nombre'] = 'Madrid'
print(ciudad)

# Escribe el código aqui para eliminar un par clave-valor de 'ciudad' y verlo por consola
del ciudad['pais']
print(ciudad)
