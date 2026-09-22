"""
--------------------------- VARIABLES / TIPOS DE DATOS ---------------------------
En este taller aprenderás cómo crear variables, trabajar con diferentes tipos de datos.
"""

"""
--- Ejercicio 1 Variables---
Crea una variable llamada "mensaje". 
Asígnale el valor "¡Hola, Mundo!". 
Imprime el valor de la variable en la consola.
"""
# Escribe tu código aquí
mensaje = "¡Hola, Mundo!"
print(mensaje)

"""
--- Ejercicio 2 Variables---
Invoca la variable anterior llamada "mensaje". 
Reasígnale el valor "Hello world!". 
Imprime el valor de la variable en la consola.
Escribe en un comentario de línea lo que sucede.
"""
# Escribe tu código aquí
mensaje = "Hello world!"
print(mensaje)

"""
--- Ejercicio 3 Tipos de datos---
Crea variables para cada uno de los siguientes tipos de datos y colecciones: string, int, float, 
bool, list, tuple, dicctionary and set. 
Imprime cada variable y el tipo de dato o colección que almacena en la consola.
"""
# Escribe tu código aquí
mi_string = "Soy un texto"
mi_int = 42
mi_float = 3.14
mi_bool = True
mi_lista = [1, 2, 3]
mi_tupla = (4, 5, 6)
mi_diccionario = {"clave": "valor"}
mi_set = {7, 8, 9}

print(mi_string, type(mi_string))
print(mi_int, type(mi_int))
print(mi_float, type(mi_float))
print(mi_bool, type(mi_bool))
print(mi_lista, type(mi_lista))
print(mi_tupla, type(mi_tupla))
print(mi_diccionario, type(mi_diccionario))
print(mi_set, type(mi_set))
