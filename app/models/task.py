from app.services.observer import Subject

class Task(Subject):
    def __init__(self, title, description, priority="MEDIUM"):
        super().__init__()
        self.title = title
        self.description = description
        self.priority = priority
        self.status = "Pending"

    def complete_task(self):
        self.status = "Completed"
        self.notify(f"Tarefa '{self.title}' foi concluída!")