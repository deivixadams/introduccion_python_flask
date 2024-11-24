import random  # Importar la biblioteca para generar números aleatorios

# Generar un número aleatorio entre 1 y 10
numero_secreto = random.randint(1, 10)

# Instrucciones del juego
print("¡Bienvenido al juego de adivinar el número!")
print("He pensado un número entre 1 y 10. ¿Puedes adivinar cuál es?")

# Solicitar al usuario que adivine
adivinanza = int(input("Ingresa tu número: "))

# Comprobar si la adivinanza es correcta
if adivinanza == numero_secreto:
    print("¡Felicidades! Adivinaste el número.")
else:
    print(f"Lo siento, el número correcto era {numero_secreto}. ¡Intenta de nuevo!")
