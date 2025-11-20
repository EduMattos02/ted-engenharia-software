from flask import Blueprint, render_template, request, redirect, url_for
from app.services.task_factory import TaskFactory
from app.models.user import User

task_bp = Blueprint('task_bp', __name__)

tasks_db = []
current_user = User("Eduardo")

@task_bp.route('/')
def index():
    return render_template('index.html', tasks=tasks_db, notifications=current_user.notifications)

@task_bp.route('/add', methods=['POST'])
def add_task():
    title = request.form.get('title')
    description = request.form.get('description')
    task_type = request.form.get('type')

    new_task = TaskFactory.create_task(task_type, title, description)
    
    new_task.attach(current_user)
    
    tasks_db.append(new_task)
    return redirect(url_for('task_bp.index'))

@task_bp.route('/complete/<int:task_id>')
def complete_task(task_id):
    if 0 <= task_id < len(tasks_db):
        task = tasks_db[task_id]
        task.complete_task()
        
    return redirect(url_for('task_bp.index'))