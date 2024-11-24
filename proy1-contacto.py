# Sistema de gestión de contactos con diccionarios

# Diccionario para almacenar los contactos
contactos = {}

# Función para agregar un contacto
def agregar_contacto():
    print("\n=== Agregar Contacto ===")
    nombre = input("Ingrese el nombre del contacto: ").strip()
    if nombre in contactos:
        print(f"El contacto '{nombre}' ya existe.")
    else:
        telefono = input("Ingrese el número de teléfono: ").strip()
        correo = input("Ingrese el correo electrónico: ").strip()
        contactos[nombre] = {"Teléfono": telefono, "Correo": correo}
        print(f"Contacto '{nombre}' agregado exitosamente.")

# Función para buscar un contacto
def buscar_contacto():
    print("\n=== Buscar Contacto ===")
    nombre = input("Ingrese el nombre del contacto a buscar: ").strip()
    if nombre in contactos:
        print(f"Información de '{nombre}':")
        print(f"Teléfono: {contactos[nombre]['Teléfono']}")
        print(f"Correo: {contactos[nombre]['Correo']}")
    else:
        print(f"El contacto '{nombre}' no existe.")

# Función para actualizar un contacto
def actualizar_contacto():
    print("\n=== Actualizar Contacto ===")
    nombre = input("Ingrese el nombre del contacto a actualizar: ").strip()
    if nombre in contactos:
        print(f"Información actual de '{nombre}':")
        print(f"Teléfono: {contactos[nombre]['Teléfono']}")
        print(f"Correo: {contactos[nombre]['Correo']}")
        
        telefono = input("Ingrese el nuevo número de teléfono (deje vacío para no cambiar): ").strip()
        correo = input("Ingrese el nuevo correo electrónico (deje vacío para no cambiar): ").strip()
        
        if telefono:
            contactos[nombre]['Teléfono'] = telefono
        if correo:
            contactos[nombre]['Correo'] = correo
        
        print(f"Contacto '{nombre}' actualizado exitosamente.")
    else:
        print(f"El contacto '{nombre}' no existe.")

# Función para eliminar un contacto
def eliminar_contacto():
    print("\n=== Eliminar Contacto ===")
    nombre = input("Ingrese el nombre del contacto a eliminar: ").strip()
    if nombre in contactos:
        del contactos[nombre]
        print(f"Contacto '{nombre}' eliminado exitosamente.")
    else:
        print(f"El contacto '{nombre}' no existe.")

# Función para listar todos los contactos
def listar_contactos():
    print("\n=== Lista de Contactos ===")
    if contactos:
        for nombre, info in contactos.items():
            print(f"Nombre: {nombre}")
            print(f"  Teléfono: {info['Teléfono']}")
            print(f"  Correo: {info['Correo']}")
    else:
        print("No hay contactos disponibles.")

# Menú principal
def menu():
    while True:
        print("\n=== Menú Principal ===")
        print("1. Agregar Contacto")
        print("2. Buscar Contacto")
        print("3. Actualizar Contacto")
        print("4. Eliminar Contacto")
        print("5. Listar Contactos")
        print("6. Salir")
        
        opcion = input("Elige una opción: ").strip()
        
        if opcion == "1":
            agregar_contacto()
        elif opcion == "2":
            buscar_contacto()
        elif opcion == "3":
            actualizar_contacto()
        elif opcion == "4":
            eliminar_contacto()
        elif opcion == "5":
            listar_contactos()
        elif opcion == "6":
            print("Saliendo del sistema de gestión de contactos. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")

# Ejecutar el sistema
menu()
