# Import functions from task_manager.task_utils package
from task_utils import add_task, mark_task_as_complete, view_pending_tasks, calculate_progress


# Define the main function
def main():
    while True:
        print("Task Management System")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_task()
        elif choice =="2":
            try:
                index = int(input("Enter the task number to mark complete: ")) - 1
                mark_task_as_complete(index)
            except ValueError:
                print("Please enter a valid number.")
            except IndexError as err:
                print(err)
        elif choice == "3":
            view_pending_tasks()
        elif choice == "4":
            progress = calculate_progress()
            print(f"Progress: {progress:.2f}%")
        elif choice == "5":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()