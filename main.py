# AIM: Task List Manager
# Coder: Ayaan Sayed
# Date: 19/01/26

print("--- Task List Manager ---")
tasks = ["Sleep", "Getup", "Brush"]
print(f"Original Tasks: {tasks}")

# Write your code here
# Initialize the original list of tasks
tasks = ['Sleep', 'Getup', 'Brush']

print("--- Task List Manager ---")
print(f"Original Tasks: {tasks}")

# 1. Add a new task
new_task = input("Enter a new task to add: ")
tasks.append(new_task)
print(f"Tasks after Adding: {tasks}")

# 2. Edit a task by index
try:
    edit_index = int(input("Enter the index of the task to edit: "))
    new_val = input("Enter the new task: ")
    tasks[edit_index] = new_val
    print(f"Tasks after Editing: {tasks}")
except IndexError:
    print("Invalid index provided for editing.")

# 3. Remove a task by index
try:
    remove_index = int(input("Enter the index of the task to remove: "))
    tasks.pop(remove_index)
    print(f"Tasks after Removing: {tasks}")
except IndexError:
    print("Invalid index provided for removal.")

# 4. Sort the tasks alphabetically
tasks.sort()
print(f"Tasks after Sorting: {tasks}")
