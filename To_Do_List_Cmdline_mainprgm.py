import todo

def main():
    tasks = todo.load_tasks("tasks.txt") 
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
            todo.add_task(tasks, task)
        elif choice == '2':
            index = int(input("Enter the task number to update: ")) - 1
            new_task = input("Enter the new task: ")
            todo.update_task(tasks, index, new_task)
        elif choice == '3':
            index = int(input("Enter the task number to delete: ")) - 1
            todo.delete_task(tasks, index)
        elif choice == '4':
            todo.view_tasks(tasks)
        elif choice == '5':
            todo.save_tasks(tasks, "tasks.txt")
        elif choice == '6':
            todo.save_tasks(tasks, "tasks.txt") 
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
