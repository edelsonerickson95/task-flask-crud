from flask import Flask, request, jsonify
from models.task import Task

app = Flask(__name__)

tasks = []
task_id_control = 1


# CREATE
@app.route("/tasks", methods=["POST"])
def create_task():
    global task_id_control
    data = request.get_json()
    new_task = Task(
        id=task_id_control,
        title=data.get("title"),
        description=data.get("description", ""),
    )
    task_id_control += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"message": "Nova tarefa creada com sucesso", "id":new_task.id})


@app.route("/tasks", methods=["GET"])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]
    output = {"tasks": task_list, "total_task": len(task_list)}

    return jsonify(output)


# READ
@app.route("/tasks/<int:id>", methods=["GET"])
def get_task(id):
    # task = None
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())

    return jsonify({"message": "Não foi possíve, encontar a atividade"}), 404


@app.route("/user/<int:user_id>")
def show_user(user_id):
    print(user_id)
    print(type(user_id))
    return "%s" % user_id


# Update
@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break

    if task == None:
        return jsonify({"message": "Não foi possíve, encontar a atividade"}), 404

    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    task.completed = data['completed']
    print(task)
    return jsonify({"message": "Tarefa atualizada com sucesso"})


# DELETE
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = None
    for t in tasks:
        if t in tasks:
            if t.id == id:
                task = t
                break

    if not task:
        return jsonify({"message": "Não foi possível encontar a atividade"}), 404

    tasks.remove(task)
    return jsonify({"message": "Tarefa deletada com sucesso"})


if __name__ == "__main__":
    app.run(debug=True)
