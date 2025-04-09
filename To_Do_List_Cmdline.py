def add_task(tasks, task):
    tasks.append(task)
    print(f'Added task: "{task}"')

def update_task(tasks, index, new_task):
    if 0 <= index < len(tasks):
        old_task = tasks[index]
        tasks[index] = new_task
        print(f'Updated task: "{old_task}" to "{new_task}"')
    else:
        print("Invalid task index.")

def delete_task(tasks, index):
    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        print(f'Deleted task: "{removed_task}"')
    else:
        print("Invalid task index.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("Your tasks:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")

def save_tasks(tasks, filename):
    with open(filename, 'w') as f:
        for task in tasks:
            f.write(f"{task}\n")
    print("Tasks saved to file.")

def load_tasks(filename):
    try:
        with open(filename, 'r') as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print("No saved tasks found.")
        return []


def main():
    tasks = load_tasks("tasks.txt") 
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. View Tasks")
        print("5. Save Tasks")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ")
        
        if choice == '1':
            task = input("Enter the task: ")
            add_task(tasks, task)
        elif choice == '2':
            index = int(input("Enter the task number to update: ")) - 1
            new_task = input("Enter the new task: ")
            update_task(tasks, index, new_task)
        elif choice == '3':
            index = int(input("Enter the task number to delete: ")) - 1
            delete_task(tasks, index)
        elif choice == '4':
            view_tasks(tasks)
        elif choice == '5':
            save_tasks(tasks, "tasks.txt")
        elif choice == '6':
            save_tasks(tasks, "tasks.txt") 
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
