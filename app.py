from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
import json
import uuid

app = Flask(__name__)
CORS(app)

DATA_FILE = 'tasks.json'

def load_tasks():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_tasks(tasks):
    with open(DATA_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

@app.route("/")
def home():
    return "Task Manager API is running!"

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    print("Received:", data)

    tasks = load_tasks()

    new_task = {
        "id": str(uuid.uuid4()),
        "title": data.get("title"),
        "description": data.get("description", ""),
        "completed": False,
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat()
    }

    tasks.append(new_task)
    save_tasks(tasks)
    return jsonify(new_task), 201

@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = load_tasks()
    return jsonify(tasks), 200

@app.route("/tasks/<task_id>", methods=["PUT"])
def update_task(task_id):
    tasks = load_tasks()
    data = request.get_json()
    updated = False

    for task in tasks:
        if task["id"] == task_id:
            task["title"] = data.get("title", task["title"])
            task["description"] = data.get("description", task["description"])
            task["completed"] = data.get("completed", task["completed"])
            task["updated_at"] = datetime.now().isoformat()
            updated = True
            break

    if updated:
        save_tasks(tasks)
        return jsonify({"message": "Task updated successfully!"}), 200
    else:
        return jsonify({"error": "Task not found"}), 404

@app.route("/tasks/<task_id>", methods=["DELETE"])
def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [task for task in tasks if task["id"] != task_id]

    if len(tasks) == len(new_tasks):
        return jsonify({"error": "Task not found"}), 404

    save_tasks(new_tasks)
    return jsonify({"message": "Task deleted successfully!"}), 200

@app.route("/tasks", methods=["DELETE"])
def delete_all_tasks():
    tasks = load_tasks()
    if not tasks:
        return jsonify({"error": "No tasks"}), 404

    save_tasks([])
    return jsonify({"message": "All tasks deleted successfully!"}), 200

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)