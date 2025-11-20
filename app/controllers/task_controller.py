from flask import Blueprint, render_template, request, redirect, url_for
from app.services.task_factory import TaskFactory
from app.models.user import User

task_bp = Blueprint('task_bp', __name__)

# Simulação de Banco de Dados em Memória
tasks_db = []
# Simulação de Usuário Logado (Eduardo)
current_user = User("Eduardo")

@task_bp.route('/')
def index():
    # Passamos as tarefas e as notificações do usuário para a View
    return render_template('index.html', tasks=tasks_db, notifications=current_user.notifications)

@task_bp.route('/add', methods=['POST'])
def add_task():
    title = request.form.get('title')
    description = request.form.get('description')
    task_type = request.form.get('type') # urgent, routine, etc.

    # PADRÃO FACTORY: Cria a tarefa sem saber a classe exata
    new_task = TaskFactory.create_task(task_type, title, description)
    
    # PADRÃO OBSERVER: O usuário atual passa a observar essa tarefa
    new_task.attach(current_user)
    
    tasks_db.append(new_task)
    return redirect(url_for('task_bp.index'))

@task_bp.route('/complete/<int:task_id>')
def complete_task(task_id):
    if 0 <= task_id < len(tasks_db):
        task = tasks_db[task_id]
        # Isso dispara o método .notify(), que avisa o current_user
        task.complete_task()
        
    return redirect(url_for('task_bp.index'))