# AIM: Task List Manager
# Coder: Ayaan Sayed
# Date: 19/01/26

print("--- Task List Manager ---")
tasks = ["Sleep", "Getup", "Brush"]
print(f"Original Tasks: {tasks}")

# Write your code here

tasks = []

def display_tasks():
    if not tasks:
        print("Task list is empty.")
    else:
        print("Task List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter the task to add: ").strip()
    tasks.append(task)
    print(f"Task '{task}' added successfully.")

def remove_task():
    display_tasks()
    try:
        task_index = int(input("Enter the task number to remove: ")) - 1
        removed_task = tasks.pop(task_index)
        print(f"Task '{removed_task}' removed successfully.")
    except (IndexError, ValueError):
        print("Invalid task number.")

def update_task():
    display_tasks()
    try:
        task_index = int(input("Enter the task number to update: ")) - 1
        new_task = input("Enter the updated task: ").strip()
        tasks[task_index] = new_task
        print(f"Task updated successfully to '{new_task}'.")
    except (IndexError, ValueError):
        print("Invalid task number.")

def sort_tasks():
    tasks.sort()
    print("Tasks sorted successfully.")

while True:
    print("\nTask List Manager")
    print("1. Display Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Update Task")
    print("5. Sort Tasks")
    print("6. Exit")
    
    choice = input("Enter your choice: ").strip()
    
    if choice == "1":
        display_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        update_task()
    elif choice == "5":
        sort_tasks()
    elif choice == "6":
        print("Exiting Task List Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
      
