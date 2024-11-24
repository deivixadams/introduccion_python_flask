# Algoritmo que combina y muestra diferentes listas

# 1. Lista de Números Enteros
numeros = [1, 2, 3, 4, 5]
print("Lista de Números Enteros:")
print(numeros)
print("_" * 40)  # Línea separadora

# 2. Lista de Cadenas de Texto
nombres = ["Ana", "Carlos", "Luis", "María", "Sofía"]
print("Lista de Cadenas de Texto:")
print(nombres)
print("_" * 40)  # Línea separadora

# 3. Lista Mixta
mixta = [42, "Hola", True, 3.14, None]
print("Lista Mixta:")
print(mixta)
print("_" * 40)  # Línea separadora

# 4. Lista de Listas (Anidada)
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Lista de Listas (Matriz):")
for fila in matriz:
    print(fila)
print("_" * 40)  # Línea separadora

# 5. Lista Vacía (y agregar elementos dinámicamente)
vacia = []
vacia.append("Elemento 1")
vacia.append("Elemento 2")
print("Lista Vacía (con elementos añadidos):")
print(vacia)
print("_" * 40)  # Línea separadora
