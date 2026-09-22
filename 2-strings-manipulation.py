"""
--------------------------- MANIPULACIÓN DE STRINGS ---------------------------
En este taller aprenderás cómo crear manipular cadenas de texto y cómo manejar entradas de datos del usuario.
"""

"""
--- Ejercicio 1 ---
Crea una variable llamada "hobbie". 
Asígnale como valor una string con uno de tus hobbies". 
Crea otra variable llamada "name"
Asígnale como valor una string con tu nombre". 
Crea otra variable llamada "teammate"
Asígnale como valor una string con el nombre de una compañera". 
Crea una variable llamada "teammate-hobbie". 
Asígnale como valor una string con unos de sus hobbies". 
"""
# Escribe tu código aquí
hobbie = "leer"
name = "Jonathan"
teammate = "María"
teammate_hobbie = "pintar"

"""
--- Ejercicio 2 Concatenación ---
Imprime por consola el siguiente mensaje concatenando las variales anteriormente declaradas:
"Soy [name] y en mis tiempos libres me gusta [hobbie]"
"""
# Escribe tu código aquí
print("Soy " + name + " y en mis tiempos libres me gusta " + hobbie)

"""
--- Ejercicio 3 f-strings ---
Imprime por consola el siguiente mensaje usando f-strings para unir las frases de las variales anteriormente declaradas:
"Ella es [teammate] y en sus tiempos libres le gusta [teammate-hobbie]"
"""
# Escribe tu código aquí
print(f"Ella es {teammate} y en sus tiempos libres le gusta {teammate_hobbie}")

"""
--- Ejercicio 4 separación por comas ---
Imprime por consola el siguiente mensaje usando separación por comas para unir las frases de las variales anteriormente declaradas:
"Ella se llama [teammate] y yo me llamo [name]"
"""
# Escribe tu código aquí
print("Ella se llama", teammate, "y yo me llamo", name)

"""
--- Ejercicio 5 separación con operador % ---
Imprime por consola el siguiente mensaje usando separación con el operador % para unir las frases de las variales anteriormente declaradas:
"Además de programar, nos gusta [hobbie] y [teammate-hobbie]"
"""
# Escribe tu código aquí
print("Además de programar, nos gusta %s y %s" % (hobbie, teammate_hobbie))

"""
--- Ejercicio 6 input data ---
Escribe dos variables que reciban por terminal un número cada una
"""
# Escribe tu código aquí
numero1 = input("Introduce el primer número: ")
numero2 = input("Introduce el segundo número: ")

"""
--- Ejercicio 7 ---
Imprime por consola el resultado de la suma de los dos número obtenidos anteriormente y 
en un comentario de línea escribe lo que sucede. ¡Recuerda que puedes usar type() para indagar mas!
"""
# Escribe tu código aquí
print(numero1 + numero2)
# Escribe tu análisis aquí
# Al usar input(), los datos introducidos se leen como cadenas de texto (tipo str) 
# y al sumarlos con '+', Python los concatena (une los textos) en lugar de hacer una suma matemática.

"""
--- Ejercicio 6 conversión de strings ---
Transforma los valores recibidos en el ejercicio 6 a números
Imprime por consola el resultado de la suma de los dos número obtenidos anteriormente
"""
# Escribe tu código aquí
numero1_int = int(numero1)
numero2_int = int(numero2)
print(numero1_int + numero2_int)
