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
