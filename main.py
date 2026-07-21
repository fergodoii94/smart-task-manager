import json
import os

class TaskManager:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, description):
        self.tasks.append({"description": description, "done": False})
        self.save_tasks()

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]['done'] = True
            self.save_tasks()

    def list_tasks(self):
        for i, task in enumerate(self.tasks):
            status = "✅" if task['done'] else "❌"
            print(f"{i}. {status} {task['description']}")

def main():
    manager = TaskManager()
    while True:
        print("\n--- SMART TASK MANAGER ---")
        print("1. Add Task | 2. List Tasks | 3. Complete Task | 4. Exit")
        choice = input("Choice: ")
        if choice == '1':
            manager.add_task(input("Task description: "))
        elif choice == '2':
            manager.list_tasks()
        elif choice == '3':
            manager.complete_task(int(input("Task index: ")))
        elif choice == '4':
            break

if __name__ == "__main__":
    main()
