import unittest
from app.services.task_factory import TaskFactory
from app.models.user import User # Assumindo que você crie uma classe User simples

class TestTaskSystem(unittest.TestCase):
    def test_factory_creation(self):
        task = TaskFactory.create_task("urgent", "Corrigir Bug", "Erro crítico")
        self.assertEqual(task.priority, "HIGH")

    def test_observer_notification(self):
        task = TaskFactory.create_task("routine", "Doc", "Escrever doc")
        user = User("Eduardo") # User deve herdar de Observer
        task.attach(user)
        
        # Captura a saída ou verifica estado (simplificado para exemplo)
        task.complete_task()
        self.assertEqual(task.status, "Completed")

if __name__ == '__main__':
    unittest.main()