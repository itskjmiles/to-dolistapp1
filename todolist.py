# Define global variables to store tasks
tasks = []

# Display menu options
def display_menu():
    print("Welcome to the To-Do List App!")
    print("Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")

#  Add a task
def add_task():
    try:
        title = input("Enter the title of the task: ")
        tasks.append({"title": title, "status": "Incomplete"})
        print("Task added successfully!")
    except Exception as e:
        print(f"An error occurred while adding the task: {e}")

# View tasks
def view_tasks():
    try:
        if tasks:
            print("Tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task['title']} - {task['status']}")
        else:
            print("No tasks found.")
    except Exception as e:
        print(f"An error occurred while viewing tasks: {e}")

# Mark a task as complete
def mark_complete():
    try:
        view_tasks()
        task_index = int(input("Enter the index of the task to mark as complete: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks[task_index]["status"] = "Complete"
            print("Task marked as complete!")
        else:
            print("Invalid task index.")
    except Exception as e:
        print(f"An error occurred while marking the task as complete: {e}")

# Delete a task
def delete_task():
    try:
        view_tasks()
        task_index = int(input("Enter the index of the task to delete: ")) - 1
        if 0 <= task_index < len(tasks):
            del tasks[task_index]
            print("Task deleted successfully!")
        else:
            print("Invalid task index.")
    except Exception as e:
        print(f"An error occurred while deleting the task: {e}")

# Run the To-Do List Application
def main():
    try:
        while True:
            display_menu()
            choice = input("Enter your choice (1-5): ")
            if choice == "1":
                add_task()
            elif choice == "2":
                view_tasks()
            elif choice == "3":
                mark_complete()
            elif choice == "4":
                delete_task()
            elif choice == "5":
                print("Thank you for using the To-Do List App!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Exiting the To-Do List App.")

# Run the main function
if __name__ == "__main__":
    main()
