from app.services.observer import Subject

class Task(Subject): # Herda de Subject para ser observado
    def __init__(self, title, description, priority="MEDIUM"):
        super().__init__()
        self.title = title
        self.description = description
        self.priority = priority
        self.status = "Pending"

    def complete_task(self):
        self.status = "Completed"
        # O Princípio Aberto/Fechado (OCP) é respeitado aqui via Observer
        self.notify(f"Tarefa '{self.title}' foi concluída!")