class Task:
    def __init__(self, title: str):
        # store title and mark incomplete by default
        self.title = title
        self.completed = False

    def complete(self):
        # mark complete and confirm
        self.completed = True
        print(f"✅ Task '{self.title}' completed.")


class User:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, task: Task):
        self.tasks.append(task)
        print(f"📌 Task '{task.title}' added to {self.name}.")

    # convenience helper (used by CLI)
    def get_task_by_title(self, title: str):
        for t in self.tasks:
            if t.title == title:
                return t
        return None