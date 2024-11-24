import random

# Dibujos del ahorcado en formato ASCII
hangman_stages = [
    """
       ------
       |    |
            |
            |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
            |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
       |    |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|    |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
            |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
      /     |
            |
    =========
    """,
    """
       ------
       |    |
       O    |
      /|\\   |
      / \\   |
            |
    =========
    """
]

# Lista de palabras para el juego
palabras = ["python", "programacion", "ahorcado", "desarrollo", "inteligencia"]

# Seleccionar una palabra aleatoria
palabra_secreta = random.choice(palabras)
longitud = len(palabra_secreta)
palabra_actual = ["_"] * longitud
errores = 0
max_errores = len(hangman_stages) - 1

print("¡Bienvenido al juego del Ahorcado!")
print(hangman_stages[errores])
print("Palabra: " + " ".join(palabra_actual))

while errores < max_errores and "_" in palabra_actual:
    letra = input("Ingresa una letra: ").lower()
    if letra in palabra_secreta:
        print("¡Bien hecho! La letra está en la palabra.")
        for idx, char in enumerate(palabra_secreta):
            if char == letra:
                palabra_actual[idx] = letra
    else:
        print("Incorrecto. Esa letra no está en la palabra.")
        errores += 1
    
    # Mostrar el estado actual del ahorcado y la palabra
    print(hangman_stages[errores])
    print("Palabra: " + " ".join(palabra_actual))

# Verificar el resultado
if "_" not in palabra_actual:
    print("¡Felicidades! Adivinaste la palabra:", palabra_secreta)
else:
    print("¡Has perdido! La palabra era:", palabra_secreta)
