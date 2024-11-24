# Algoritmo para encontrar el número mayor en una lista

# Paso 1: Definir una lista de números
numeros = [34, 78, 12, 90, 65, 23]

# Paso 2: Inicializar una variable para almacenar el número mayor
mayor = numeros[0]  # Asumimos que el primer número es el mayor

# Paso 3: Recorrer la lista para comparar cada número
for numero in numeros:
    if numero > mayor:  # Si encontramos un número mayor
        mayor = numero  # Actualizamos la variable mayor

# Paso 4: Imprimir el número mayor
print("El número mayor en la lista es:", mayor)
