# Clases, objetos, métodos, herencia y polimorfismo con un menú interactivo

# Clase base (superclase)
class Persona:
    # Constructor de la clase Persona
    def __init__(self, nombre, edad):
        # Atributos de la clase
        self.nombre = nombre
        self.edad = edad

    # Método para mostrar información de la Persona
    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"

# Clase derivada (subclase)
class Estudiante(Persona):
    # Constructor de la subclase Estudiante
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)  # Llamar al constructor de la superclase
        self.grado = grado  # Atributo adicional de Estudiante

    # Método polimórfico que sobrescribe el de la clase base
    def mostrar_informacion(self):
        return f"Estudiante: {self.nombre}, Edad: {self.edad}, Grado: {self.grado}"

# Clase derivada adicional para demostrar polimorfismo
class Profesor(Persona):
    # Constructor de la subclase Profesor
    def __init__(self, nombre, edad, asignatura):
        super().__init__(nombre, edad)  # Llamar al constructor de la superclase
        self.asignatura = asignatura  # Atributo adicional de Profesor

    # Método polimórfico que sobrescribe el de la clase base
    def mostrar_informacion(self):
        return f"Profesor: {self.nombre}, Edad: {self.edad}, Asignatura: {self.asignatura}"

# Función para mostrar el uso de clases, objetos y métodos
def opcion_clases_y_objetos():
    print("=== Clases, Objetos y Métodos ===")
    # Crear un objeto de la clase Persona
    persona = Persona("Ana", 30)
    # Llamar al método de la clase base y mostrar la información
    print("Objeto creado: ", persona.mostrar_informacion())

# Función para mostrar el uso de herencia
def opcion_herencia():
    print("=== Herencia ===")
    # Crear un objeto de la clase Estudiante (heredada de Persona)
    estudiante = Estudiante("Luis", 16, "10º Grado")
    # Mostrar la información utilizando el método sobrescrito
    print("Objeto Estudiante (heredado de Persona):", estudiante.mostrar_informacion())

# Función para mostrar el uso de polimorfismo
def opcion_polimorfismo():
    print("=== Polimorfismo ===")
    # Crear objetos de diferentes clases
    persona = Persona("Carlos", 45)
    estudiante = Estudiante("Lucía", 17, "11º Grado")
    profesor = Profesor("María", 40, "Matemáticas")

    # Almacenar los objetos en una lista para demostrar polimorfismo
    personas = [persona, estudiante, profesor]
    print("Demostración del polimorfismo (mostrar_informacion):")
    for p in personas:  # Cada objeto llama a su propia versión de mostrar_informacion
        print(p.mostrar_informacion())

# Función principal del menú
def menu():
    while True:
        print("\n=== Menú Principal ===")
        print("1. Clases, Objetos y Métodos")
        print("2. Herencia")
        print("3. Polimorfismo")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        # Llamar a las funciones correspondientes según la opción elegida
        if opcion == "1":
            opcion_clases_y_objetos()
        elif opcion == "2":
            opcion_herencia()
        elif opcion == "3":
            opcion_polimorfismo()
        elif opcion == "4":
            print("Saliendo del programa. ¡Hasta luego!")
            break  # Salir del bucle y terminar el programa
        else:
            print("Opción no válida. Intenta nuevamente.")

# Ejecutar el menú principal
menu()
