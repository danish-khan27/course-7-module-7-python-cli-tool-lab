class Task:
    def __init__(self, title: str):
        self.title = title
        self.completed = False

    def complete(self):
        self.completed = True
        print(f"✅ Task '{self.title}' completed.")


class User:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, task: "Task"):
        self.tasks.append(task)
        print(f"📌 Task '{task.title}' added to {self.name}.")

    def get_task_by_title(self, title: str):
        for t in self.tasks:
            if t.title == title:
                return t
        return None
