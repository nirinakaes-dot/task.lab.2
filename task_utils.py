from datetime import datetime

# Import validation functions
from validation import validate_due_date,validate_task_description


# Define tasks list
tasks = []

# Implement add_task function
def add_task(title, description, due_date):
    if title is None:
        title = input('Enter the title of your task')
    if description is None:    
        description = input('Enter the description of your task')
    if due_date is None:    
        due_date = input('Enter the due date')
    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False,
        "created_at": datetime.now().isoformat()
    }
    tasks.append(task)
    print("Task added successfully!")
    return task

# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    if index <0 or index >= len(tasks) :
        raise IndexError('Task index out of range')
    tasks[index] ['Completed']
    print("Task marked as complete!")
    return tasks[index]
    
# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    pending = [task for task in tasks]
    if not pending:
        print('No pending tasks')
    else:
        for idx, task in enumerate(pending, start=1):
            print(f"{idx}. {task['title']} - due {task['due_date']}")
    return pending

# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    if not tasks:
        return 0
    completed_count = sum(1 for task in tasks if task.get('completed', False))
     
    return (completed_count /len(tasks))