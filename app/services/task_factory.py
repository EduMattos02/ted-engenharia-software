from app.models.task import Task

class TaskFactory:
    @staticmethod
    def create_task(type, title, description):
        if type == "urgent":
            return Task(title, description, priority="HIGH")
        elif type == "routine":
            return Task(title, description, priority="LOW")
        else:
            return Task(title, description, priority="MEDIUM")