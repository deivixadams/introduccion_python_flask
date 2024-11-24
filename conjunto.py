# Algoritmo para trabajar con conjuntos

# Crear dos conjuntos iniciales
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {4, 5, 6, 7, 8}

print("Conjuntos Originales:")
print(f"Conjunto A: {conjunto_a}")
print(f"Conjunto B: {conjunto_b}")
print("_" * 40)

# 1. Unión de los conjuntos
union = conjunto_a | conjunto_b
print("Unión de A y B:")
print(union)
print("_" * 40)

# 2. Intersección de los conjuntos
interseccion = conjunto_a & conjunto_b
print("Intersección de A y B:")
print(interseccion)
print("_" * 40)

# 3. Diferencia de los conjuntos
diferencia = conjunto_a - conjunto_b
print("Diferencia (A - B):")
print(diferencia)
print("_" * 40)

# 4. Diferencia simétrica de los conjuntos
diferencia_simetrica = conjunto_a ^ conjunto_b
print("Diferencia Simétrica (A ^ B):")
print(diferencia_simetrica)
print("_" * 40)

# 5. Agregar un elemento a un conjunto
conjunto_a.add(10)
print("Conjunto A después de agregar 10:")
print(conjunto_a)
print("_" * 40)

# 6. Eliminar un elemento de un conjunto
conjunto_b.discard(7)
print("Conjunto B después de eliminar 7:")
print(conjunto_b)
print("_" * 40)

# 7. Verificar si un conjunto es subconjunto de otro
es_subconjunto = {4, 5}.issubset(conjunto_a)
print("¿{4, 5} es subconjunto de A?")
print(es_subconjunto)
print("_" * 40)

# 8. Verificar si los conjuntos son disjuntos
son_disjuntos = conjunto_a.isdisjoint(conjunto_b)
print("¿A y B son disjuntos?")
print(son_disjuntos)
print("_" * 40)
