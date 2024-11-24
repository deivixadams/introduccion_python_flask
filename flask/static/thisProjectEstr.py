# Crear un archivo ASCII para describir la estructura básica de un proyecto Flask
estructura_flask = """\
proyecto_flask/
├── app.py              # Archivo principal de la aplicación
├── templates/          # Carpeta para almacenar plantillas HTML
│   ├── index.html      # Página principal con la lista de tareas
│   ├── agregar.html    # Página para agregar nuevas tareas
│   ├── editar.html     # Página para editar una tarea existente
├── static/             # Archivos estáticos
│   └── styles.css      # Archivo de estilos (opcional)
├── tareas.db           # Base de datos SQLite

"""

# Guardar la estructura en un archivo .txt
file_path = "/mnt/data/estructura_flask.txt"
with open(file_path, "w") as file:
    file.write(estructura_flask)

file_path
