#Ejercicio de Flask  : Crea un API con Flask de que permita un CRUD (Create, Read, Update, Delete) de tareas. 
# - Cada `tarea` debe tener:
#     - `Identificador`
#     - `Título`
#     - `Descripción`
#     - `Estado` (Por Hacer, En Progreso o Completada)
# - El API debe tener endpoints para:
#     1. Obtener `tareas`.
#         1. Esta debe tener un query parameter **opcional** para filtrarlas por `Estado`.
#     2. Crear `tareas`.
#     3. Editar `tareas`.
#     4. Eliminar `tareas`.
# - Todos los datos deberán guardarse en un archivo JSON.
#     - Cada *endpoint* debe leer del archivo, y escribir en él (en caso de ser crear, editar o eliminar).
# - Además, debe de validar que:
#     1. No se puedan agregar `tareas` con identificadores ya existentes.
#     2. No se puedan agregar `tareas` sin nombre.
#     3. No se pueden agregar `tareas` sin descripción.
#     4. No se puedan agregar `tareas` sin estado.
#     5. No se puedan agregar `tareas` con un estado invalido.
import json
from flask import Flask, request, jsonify
import os 

app = Flask(__name__)
valid_states = ["To do","In progress", "Completed"]

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def get_path(file_name):
    return os.path.join(BASE_DIR,file_name)

TASKS_FILE = get_path("tasks.json")

#Functions to save and read the json file:
def read_tasks():
    try:
        with open( TASKS_FILE , "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open( TASKS_FILE , "w") as file:
        json.dump(tasks, file,indent=4)

@app.route("/tasks" , methods=["GET"])
def get_tasks():
    status = request.args.get("status")
    tasks = read_tasks()
    if status not in valid_states:
        return jsonify({"Error":"Invalid status"}),400
    tasks = [t for t in tasks if t["status"]==status]
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def create_tasks():
    new_task = request.json
    tasks = read_tasks()

    #Validations:
    if not new_task.get("id") or not new_task.get("name") or not new_task.get("description") or not new_task.get("status"):
        return jsonify({"Error":"Missing fields"}),400
    if new_task["status"] not in valid_states:
        return jsonify({"Error":"Not a valid status"}),400
    if any(t["id"] == new_task["id"] for t in tasks):
        return jsonify({"Error":"Duplicate ID"}),400

    tasks.append(new_task)
    save_tasks(tasks)
    return jsonify({"mensaje" : "Task created"}),200

@app.route("/tasks/<int:task_id>" , methods = ["PUT"])
def update_tasks(task_id):
    tasks = read_tasks()
    updated_task = request.json

    for task in tasks:
        if task["id"] == task_id:
            task.update(updated_task)
            save_tasks(tasks)
            return jsonify({"message":"Task updated"}), 200
        
    return jsonify({"message:":"Task not found"})

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_tasks(task_id):
    tasks = read_tasks()
    new_tasks = [t for t in tasks if t["id"] != task_id]

    if len(new_tasks) == len(tasks):
        return jsonify({"message": "Task not found"}),404
    
    save_tasks(new_tasks)
    return jsonify({"message":"Task deleted"}),200



if __name__ == "__main__" :
    app.run(host="localhost", port=8000 , debug=True)