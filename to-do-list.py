import os

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def __str__(self):

        return f"{'[✔]' if self.completed else '[ ]'} {self.description}"
    def mark_completed(self):
        self.completed = True


class ToDoList:
    def __init__(self, filename="tasks.txt"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        """ Load tasks from file into the list. """
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    task_desc, completed = line.strip().split(" || ")
                    task = Task(task_desc)
                    if completed == 'True':
                        task.mark_completed()
                    self.tasks.append(task)

    def save_tasks(self):
        """ Save the current tasks to a file. """
        with open(self.filename, 'w') as file:
            for task in self.tasks:
                file.write(f"{task.description} || {task.completed}\n")

    def add_task(self, description):
        """ Add a new task to the to-do list. """
        task = Task(description)
        self.tasks.append(task)
        self.save_tasks()

    def delete_task(self, index):
        """ Delete a task by index. """
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_tasks()
            print("Task deleted successfully.")
        else:
            print("Invalid task number.")

    def view_tasks(self):
        """ Display all tasks. """
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            print("\nTo-Do List:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")
        print()  # Newline for better formatting

    def mark_task_completed(self, index):
        """ Mark a task as completed. """
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
            self.save_tasks()
            print("Task marked as completed.")
        else:
            print("Invalid task number.")


def show_menu():
    """ Display the main menu to the user. """
    print("To-Do List")
    print("1. View tasks")
    print("2. Add a new task")
    print("3. Delete a task")
    print("4. Mark task as completed")
    print("5. Exit")
    print()


def main():
    to_do_list = ToDoList()

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            to_do_list.view_tasks()

        elif choice == '2':
            task_desc = input("Enter task description: ")
            to_do_list.add_task(task_desc)
            print("Task added successfully.")

        elif choice == '3':
            to_do_list.view_tasks()
            try:
                task_number = int(input("Enter task number to delete: ")) - 1
                to_do_list.delete_task(task_number)
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == '4':
            to_do_list.view_tasks()
            try:
                task_number = int(input("Enter task number to mark as completed: ")) - 1
                to_do_list.mark_task_completed(task_number)
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == '5':
            print("Exiting the program...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()