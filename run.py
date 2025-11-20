from flask import Flask
from app.controllers.task_controller import task_bp

app = Flask(__name__, template_folder='app/templates')

app.register_blueprint(task_bp)

if __name__ == "__main__":
    print("Sistema de Tarefas Iniciado...")
    print("Acesse: http://127.0.0.1:5000")
    app.run(debug=True)