# Crear un archivo ASCII para describir la estructura básica de un proyecto Flask
estructura_flask = """\
proyecto_flask/
├── app/                    # Carpeta principal de la aplicación
│   ├── __init__.py         # Archivo para inicializar la aplicación Flask
│   ├── routes.py           # Define las rutas (endpoints) de la aplicación
│   ├── models.py           # (Opcional) Define los modelos de datos si usas una base de datos
│   ├── forms.py            # (Opcional) Define formularios para la aplicación
│   └── templates/          # Carpeta para almacenar plantillas HTML
│       └── index.html      # Archivo HTML para la página principal
│   └── static/             # Carpeta para archivos estáticos (CSS, JS, imágenes)
│       ├── css/            # Archivos CSS
│       │   └── styles.css  # Hoja de estilos principal
│       ├── js/             # Archivos JavaScript
│       │   └── scripts.js  # Scripts personalizados
│       └── images/         # Imágenes utilizadas en la aplicación
├── venv/                   # Entorno virtual de Python (creado con `python -m venv venv`)
├── config.py               # Configuración de la aplicación (base de datos, claves secretas, etc.)
├── requirements.txt        # Lista de dependencias del proyecto
├── run.py                  # Archivo principal para ejecutar la aplicación
└── README.md               # Documentación del proyecto
"""

# Guardar la estructura en un archivo .txt
file_path = "/mnt/data/estructura_flask.txt"
with open(file_path, "w") as file:
    file.write(estructura_flask)

file_path
