from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Función para conectar con la base de datos
def conectar_db():
    return sqlite3.connect("tareas.db")

# Crear la tabla si no existe
def inicializar_db():
    with conectar_db() as conexion:
        cursor = conexion.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tareas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                estado TEXT NOT NULL
            )
        """)
        conexion.commit()

inicializar_db()

# Ruta principal: Muestra las tareas
@app.route("/")
def index():
    with conectar_db() as conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM tareas")
        tareas = cursor.fetchall()
    return render_template("index.html", tareas=tareas)

# Ruta para agregar una nueva tarea
@app.route("/agregar", methods=["GET", "POST"])
def agregar():
    if request.method == "POST":
        nombre_tarea = request.form.get("nombre")
        estado_tarea = request.form.get("estado")
        with conectar_db() as conexion:
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO tareas (nombre, estado) VALUES (?, ?)", (nombre_tarea, estado_tarea))
            conexion.commit()
        return redirect(url_for("index"))
    return render_template("agregar.html")

# Ruta para eliminar una tarea
@app.route("/eliminar/<int:id>")
def eliminar(id):
    with conectar_db() as conexion:
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM tareas WHERE id = ?", (id,))
        conexion.commit()
    return redirect(url_for("index"))

# Ruta para editar una tarea
@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    if request.method == "POST":
        nuevo_nombre = request.form.get("nombre")
        nuevo_estado = request.form.get("estado")
        with conectar_db() as conexion:
            cursor = conexion.cursor()
            cursor.execute("UPDATE tareas SET nombre = ?, estado = ? WHERE id = ?", (nuevo_nombre, nuevo_estado, id))
            conexion.commit()
        return redirect(url_for("index"))
    with conectar_db() as conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM tareas WHERE id = ?", (id,))
        tarea = cursor.fetchone()
    return render_template("editar.html", tarea=tarea)

if __name__ == "__main__":
    app.run(debug=True)
