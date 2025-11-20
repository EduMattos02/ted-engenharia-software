from app.services.observer import Observer

class User(Observer):
    def __init__(self, name):
        self.name = name
        self.notifications = []

    def update(self, message):
        # Em um sistema real, isso enviaria um email.
        # Aqui, guardamos numa lista para mostrar na tela.
        print(f"EMAIL ENVIADO PARA {self.name}: {message}")
        self.notifications.append(message)