# Sistema de Gestão de Tarefas Colaborativas

Este projeto foi desenvolvido para a disciplina de Engenharia de Software, aplicando arquitetura **MVC**, princípios **SOLID** e Padrões de Projeto (**Design Patterns**).

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python 3.10
- **Framework Web:** Flask
- **Testes:** Unittest / Pytest
- **CI/CD:** GitHub Actions

## 📐 Arquitetura e Padrões de Projeto

O sistema utiliza uma abordagem modular. Abaixo, o diagrama de classes UML demonstrando a aplicação dos padrões **Factory Method** e **Observer**:

```mermaid
classDiagram
    %% Padrão Observer
    class Subject {
        +attach(observer)
        +notify(message)
    }
    class Observer {
        +update(message)
    }
    class User {
        +name: str
        +update(message)
    }
    class Task {
        +title: str
        +status: str
        +complete_task()
    }

    %% Padrão Factory
    class TaskFactory {
        +create_task(type, title, desc)
    }

    %% Relacionamentos
    Observer <|-- User : Implementa
    Subject <|-- Task : Herda
    Subject --> Observer : Notifica
    TaskFactory ..> Task : Cria