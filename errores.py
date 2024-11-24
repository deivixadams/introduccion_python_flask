# Errores y Excepciones: Manejo de errores con try, except y depuración básica

# Función para manejar errores con try-except
def manejo_errores():
    print("=== Manejo de Errores ===")
    try:
        # Pedir un número al usuario
        numero = int(input("Ingresa un número: "))
        # Intentar dividir un número entre el ingresado
        resultado = 10 / numero
        print(f"El resultado de 10 dividido por {numero} es: {resultado}")
    except ValueError:
        # Capturar errores de conversión de datos
        print("Error: Debes ingresar un número válido.")
    except ZeroDivisionError:
        # Capturar el error de división por cero
        print("Error: No se puede dividir entre cero.")
    except Exception as e:
        # Capturar cualquier otro tipo de error
        print(f"Error inesperado: {e}")
    finally:
        # Bloque que se ejecuta siempre
        print("Finalizando el manejo de errores.")

# Función para depuración básica
def depuracion_basica():
    print("=== Depuración Básica ===")
    try:
        # Pedir una lista de números separados por comas
        entrada = input("Ingresa una lista de números separados por comas (ejemplo: 1,2,3): ")
        # Convertir la entrada en una lista de números
        numeros = [int(x) for x in entrada.split(",")]
        print("Lista ingresada:", numeros)
        
        # Calcular la suma y el promedio
        suma = sum(numeros)
        promedio = suma / len(numeros)
        print(f"Suma: {suma}, Promedio: {promedio}")
    except ValueError as e:
        # Mostrar el error exacto en caso de datos inválidos
        print(f"Error: Entrada inválida. Detalle: {e}")
    except Exception as e:
        # Capturar cualquier otro error
        print(f"Error inesperado: {e}")
    finally:
        print("Depuración finalizada.")

# Menú principal
def menu():
    while True:
        print("\n=== Menú Principal ===")
        print("1. Manejo de Errores")
        print("2. Depuración Básica")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            manejo_errores()
        elif opcion == "2":
            depuracion_basica()
        elif opcion == "3":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")

# Ejecutar el menú principal
menu()
