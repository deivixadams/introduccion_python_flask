# Algoritmo para manejo de archivos

# 1. Crear y escribir en un archivo
with open("archivo.txt", "w") as archivo:
    archivo.write("Línea 1: Hola, este es un archivo de texto.\n")
    archivo.write("Línea 2: Python facilita el manejo de archivos.\n")

print("Archivo creado y datos escritos.")
print("_" * 40)

# 2. Leer el contenido completo del archivo
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()

print("Contenido del archivo:")
print(contenido)
print("_" * 40)

# 3. Leer línea por línea
with open("archivo.txt", "r") as archivo:
    print("Leyendo línea por línea:")
    for linea in archivo:
        print(linea.strip())  # Eliminar saltos de línea al final
print("_" * 40)

# 4. Agregar contenido al archivo
with open("archivo.txt", "a") as archivo:
    archivo.write("Línea 3: Este contenido fue agregado después.\n")

print("Nuevo contenido agregado.")
print("_" * 40)

# 5. Leer y contar líneas
with open("archivo.txt", "r") as archivo:
    lineas = archivo.readlines()

print(f"El archivo tiene {len(lineas)} líneas.")
print("_" * 40)

# 6. Eliminar un archivo (opcional)
import os
os.remove("archivo.txt")
print("Archivo eliminado.")
print("_" * 40)
