from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///task.db'
app.config['SQLALCAMY_TRACK_MODIFICATIONS'] = False
db= SQLAlchemy(app)

class Task(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(20),nullable=False)
    description=db.Column(db.String(200))
    due_date=db.Column(db.DateTime)
    status=db.Column(db.String(20),default='Incomplete')

    def validate_status(self, status):
        valid_statuses = ["Incomplete", "In Progress", "Completed"]
        if status not in valid_statuses:
            raise ValueError("Invalid status value")


# Create a new task
@app.route('/tasks', methods=['POST'])
def create_task():
    new_task = {
        'title': request.json.get('title', ''),
        'description': request.json.get('description', ''),
        'due_date': request.json.get('due_date', ''),
        'status': request.json.get('status', 'Incomplete')
    }

    if not new_task['title']:
        return jsonify({'error': 'Title is required'}), 400

    try:
        due_date = datetime.strptime(new_task['due_date'], '%Y-%m-%d')
    except ValueError:
        return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD'}), 400
    
    
    
    task = Task(
        title=new_task['title'],
        description=new_task['description'],
        due_date=due_date,
        status=new_task['status']
    )

    try:
        task.validate_status(task.status)
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

    db.session.add(task)
    db.session.commit()

    return jsonify({
        'id': task.id,
        'title': task.title,
        'description': task.description,
        'due_date': task.due_date.strftime('%Y-%m-%d'),
        'status': task.status
    }), 201


# Retrieve a single task by its ID
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = Task.query.get(task_id)

    if task:
        return jsonify({
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'due_date': task.due_date,
            'status': task.status
        })
    else:
        return jsonify({'error': 'Task not found'}), 404


# Update an existing task
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Task.query.get(task_id)

    if not task:
        return jsonify({'error': 'Task not found'}), 404

    task.title = request.json.get('title', task.title)
    task.description = request.json.get('description', task.description)
    task.due_date = request.json.get('due_date', task.due_date)
    task.status = request.json.get('status', task.status)

    db.session.commit()

    return jsonify({
        'id': task.id,
        'title': task.title,
        'description': task.description,
        'due_date': task.due_date,
        'status': task.status
    })


# Delete a task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get(task_id)

    if not task:
        return jsonify({'error': 'Task not found'}), 404

    db.session.delete(task)
    db.session.commit()

    return jsonify({'deleted'}), 204

# List all tasks with pagination
@app.route('/tasks', methods=['GET'])
def list_tasks():
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 5))

    tasks = Task.query.paginate(page=page, per_page=per_page)

    if not tasks.items:
        return jsonify({'error': 'No tasks found'}), 404

    task_list = []
    for task in tasks.items:
        task_data = {
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'due_date': task.due_date.strftime('%Y-%m-%d'),
            'status': task.status
        }
        task_list.append(task_data)

    return jsonify({
        'tasks': task_list,
        'total_tasks': tasks.total,
        'current_page': tasks.page,
        'per_page': tasks.per_page,
        'has_next': tasks.has_next,
        'has_prev': tasks.has_prev
    })

if __name__ == '__main__':
    app.run()
