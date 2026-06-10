tasks = []

def add_task():
    name = input("Enter task name: ")
    
    if len(name) == 0:
        raise ValueError("Task name cannot be empty.")
    
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    priority = input("Enter priority (1-5): ")
    
    try:
        priority = int(priority)
        if priority < 1 or priority > 5:
            raise ValueError("Priority must be between 1 and 5.")
    except ValueError:
        raise ValueError("Priority must be a valid integer between 1 and 5.")
    
    task = {
        "name": name,
        "description": description,
        "due_date": due_date,
        "priority": priority,
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully!")


def mark_task_as_complete(index):
    if index < 0 or index >= len(tasks):
        raise IndexError("Task number out of range.")
    tasks[index]["completed"] = True
    print(f"Task '{tasks[index]['name']}' marked as complete!")


def view_pending_tasks():
    pending = [t for t in tasks if not t["completed"]]
    if not pending:
        print("No pending tasks.")
    else:
        for i, task in enumerate(pending, 1):
            print(f"{i}. {task['name']} | Due: {task['due_date']} | Priority: {task['priority']}")


def calculate_progress():
    if len(tasks) == 0:
        return 0.0
    completed = sum(1 for t in tasks if t["completed"])
    return (completed / len(tasks)) * 100
