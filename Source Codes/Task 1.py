# Define a dictionary to store tasks
tasks = {}

def add_task(task_description):
    task_id = len(tasks) + 1
    tasks[task_id] = {"description": task_description, "completed": False}
    print(f"Task {task_id} added.")
def update_task(task_id, new_description):
    if task_id in tasks:
        tasks[task_id]["description"] = new_description
        print(f"Task {task_id} updated.")
    else:
        print(f"Task {task_id} not found.")
def complete_task(task_id):
    if task_id in tasks:
        tasks[task_id]["completed"] = True
        print(f"Task {task_id} marked as completed.")
    else:
        print(f"Task {task_id} not found.")
def delete_task(task_id):
    if task_id in tasks:
        del tasks[task_id]
        print(f"Task {task_id} deleted.")
    else:
        print(f"Task {task_id} not found.")
def list_tasks():
    print("To-Do List:")
    for task_id, task in tasks.items():
        status = "Completed" if task["completed"] else "Not Completed"
        print(f"Task {task_id}: {task['description']} ({status})")
if __name__ == "__main__":
    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. List Tasks")
        print("6. Quit")

        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == "1":
            task_description = input("Enter task description: ")
            add_task(task_description)
        elif choice == "2":
            task_id = int(input("Enter task ID to update: "))
            new_description = input("Enter new task description: ")
            update_task(task_id, new_description)
        elif choice == "3":
            task_id = int(input("Enter task ID to mark as completed: "))
            complete_task(task_id)
        elif choice == "4":
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)
        elif choice == "5":
            list_tasks()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")
     
