from app.services.observer import Observer

class User(Observer):
    def __init__(self, name):
        self.name = name
        self.notifications = []

    def update(self, message):
        print(f"EMAIL ENVIADO PARA {self.name}: {message}")
        self.notifications.append(message)