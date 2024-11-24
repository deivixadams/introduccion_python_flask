# Algoritmo para trabajar con tuplas

# Crear una tupla inicial
tupla = (10, 20, 30, 40, 50)

print("Tupla Original:")
print(tupla)
print("_" * 40)

# 1. Acceder a un elemento por índice
print("Elemento en la posición 2:")
print(tupla[2])
print("_" * 40)

# 2. Rebanado (Slicing)
print("Rebanado de la tupla (del índice 1 al 3):")
print(tupla[1:4])
print("_" * 40)

# 3. Longitud de la tupla
print("Longitud de la tupla:")
print(len(tupla))
print("_" * 40)

# 4. Concatenar dos tuplas
tupla_extra = (60, 70, 80)
nueva_tupla = tupla + tupla_extra
print("Tupla después de concatenar:")
print(nueva_tupla)
print("_" * 40)

# 5. Verificar la existencia de un elemento
print("¿Está el número 30 en la tupla?")
print(30 in tupla)
print("_" * 40)

# 6. Contar ocurrencias de un elemento
print("Ocurrencias del número 40 en la tupla:")
print(tupla.count(40))
print("_" * 40)

# 7. Índice de un elemento
print("Índice del número 50 en la tupla:")
print(tupla.index(50))
print("_" * 40)

# 8. Convertir la tupla en una lista
tupla_como_lista = list(tupla)
print("Tupla convertida a lista:")
print(tupla_como_lista)
print("_" * 40)

# 9. Iterar sobre la tupla
print("Elementos de la tupla:")
for elemento in tupla:
    print(elemento)
print("_" * 40)
