class Task:
    def __init__(self, task_id, name, description, due_date, completed=False):
        self.task_id = task_id
        self.name = name
        self.description = description
        self.due_date = due_date
        self.completed = completed

class ToDoList:
    def __init__(self):
        self.tasks = []
        self.task_id_counter = 1
    
    def add_task(self, name, description, due_date):
        new_task = Task(self.task_id_counter, name, description, due_date)
        self.tasks.append(new_task)
        self.task_id_counter += 1
    
    def view_tasks(self):
        for task in self.tasks:
            status = "Completed" if task.completed else "Not Completed"
            print(f"Task ID: {task.task_id}, Name: {task.name}, Description: {task.description}, Due Date: {task.due_date}, Status: {status}")
    
    def mark_task_complete(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                task.completed = True
                print(f"Task {task_id} marked as completed.")
                return
        print(f"Task {task_id} not found.")
    
    def delete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                print(f"Task {task_id} deleted.")
                return
        print(f"Task {task_id} not found.")

def main():
    todo_list = ToDoList()
    
    while True:
        print("\n===== To-Do List Menu =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter task name: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date: ")
            todo_list.add_task(name, description, due_date)
            print("Task added successfully!")
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            task_id = int(input("Enter task ID to mark as complete: "))
            todo_list.mark_task_complete(task_id)
        elif choice == "4":
            task_id = int(input("Enter task ID to delete: "))
            todo_list.delete_task(task_id)
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
