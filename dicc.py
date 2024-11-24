# Algoritmo para trabajar con diccionarios

# Crear un diccionario inicial
estudiantes = {
    "Ana": 85,
    "Carlos": 90,
    "Luis": 78,
    "María": 92,
    "Sofía": 88
}

print("Diccionario de Estudiantes (Original):")
print(estudiantes)
print("_" * 40)

# 1. Agregar un nuevo estudiante
estudiantes["Roberto"] = 80
print("Después de agregar a Roberto:")
print(estudiantes)
print("_" * 40)

# 2. Eliminar un estudiante
del estudiantes["Luis"]
print("Después de eliminar a Luis:")
print(estudiantes)
print("_" * 40)

# 3. Actualizar la calificación de un estudiante
estudiantes["Ana"] = 95
print("Después de actualizar la calificación de Ana:")
print(estudiantes)
print("_" * 40)

# 4. Buscar un estudiante por nombre
nombre = "María"
if nombre in estudiantes:
    print(f"Calificación de {nombre}: {estudiantes[nombre]}")
else:
    print(f"{nombre} no está en el diccionario.")
print("_" * 40)

# 5. Listar todos los estudiantes con sus calificaciones
print("Lista de todos los estudiantes y sus calificaciones:")
for estudiante, calificacion in estudiantes.items():
    print(f"{estudiante}: {calificacion}")
print("_" * 40)

# 6. Calcular el promedio de las calificaciones
promedio = sum(estudiantes.values()) / len(estudiantes)
print(f"Promedio de las calificaciones: {promedio:.2f}")
print("_" * 40)
