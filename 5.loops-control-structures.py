"""
--------------------------- CICLOS Y ESTRUCTURAS DE CONTROL ---------------------------
En este taller aprenderás usar los métodos más típicos para dirigir el flujo de ejecuón y la lógica de un algoritmo
"""

"""
--- Ejercicio 1 condicionales  ---
Escribe un programa que pida al usuario una letra y luego imprima un mensaje indicando si es una vocal o una consonante.
"""
# Escribe tu código aquí
letra = input("Introduce una letra: ").lower()
if letra in ['a', 'e', 'i', 'o', 'u']:
    print("Es una vocal")
else:
    print("Es una consonante")


"""
--- Ejercicio 2  condicionales anidados  ---
Escribe un programa que pida al usuario una nota (entre 0 y 100) y determine si 
es una calificación de "A", "B", "C", "D" o "F".
"""
# Escribe tu código aquí
nota = int(input("Introduce una nota (0-100): "))
if nota >= 90:
    print("A")
elif nota >= 80:
    print("B")
elif nota >= 70:
    print("C")
elif nota >= 60:
    print("D")
else:
    print("F")

"""
--- Ejercicio 3  bucle while  ---
Escribe un programa que pida al usuario un número entero positivo y 
luego imprima la cuenta regresiva desde ese número hasta 1.
"""
# Escribe tu código aquí
numero = int(input("Introduce un número entero positivo: "))
while numero > 0:
    print(numero)
    numero -= 1

"""
--- Ejercicio 4  bucle for  ---
Escribe un programa que imprima todos los caracteres de una cadena de texto ingresada por el usuario.
"""
# Escribe tu código aquí
cadena = input("Introduce un texto: ")
for caracter in cadena:
    print(caracter)

"""
--- Ejercicio 5  bucle for con range ---
Escribe un programa que imprima la tabla de multiplicar del 5 (del 1 al 10).
"""
# Escribe tu código aquí
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

"""
--- Ejercicio 6  bucle for con listas ---
Escribe un programa que pida al usuario 5 palabras, las guarde en una lista y 
luego en una nueva lista guarde todas las palabras en mayúsculas.
"""
# Escribe tu código aquí
palabras = []
for i in range(5):
    palabra = input(f"Introduce la palabra {i+1}: ")
    palabras.append(palabra)

palabras_mayusculas = []
for palabra in palabras:
    palabras_mayusculas.append(palabra.upper())

print("Mayúsculas:", palabras_mayusculas)


"""
--- Ejercicio 7  break and continue ---
Escribe un programa que le pida al usuario una mascota y 
si es un perro, que imprima en la consola "Tengo un perro", 
si es un gato, que imprima en la consola "Tengo un gato", 
si es un pájaro, que imprima en la consola "Tengo un pájaro" y 
si no es ninguno de los 3 que imprima "No tengo una mascota convencional"
"""
# Escribe tu código aquí
while True:
    mascota = input("Introduce una mascota: ").lower()
    
    if mascota == "perro":
        print("Tengo un perro")
        break
    elif mascota == "gato":
        print("Tengo un gato")
        break
    elif mascota == "pájaro" or mascota == "pajaro":
        print("Tengo un pájaro")
        break
    else:
        print("No tengo una mascota convencional.")
        continue
