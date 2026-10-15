import json
import os
from datetime import datetime
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TASKS_FILE = os.path.join(BASE_DIR, "tasks.json")
def load_task():
    try: 
        with open(TASKS_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        with open(TASKS_FILE, "w", encoding="utf-8") as file:
            json.dump([], file, indent=4)
        return []
    except json.JSONDecodeError:
        print("Warning!: The tasks.json file is corrupted!")
        while True:
            corrupted_json_choice = input("Would you like to: 1 Create a new clean file or 2 Exit the program ?: ")
            if corrupted_json_choice == "1":
                timestamp = datetime.now().strftime("%d%m%Y_%H%M%S")
                backup_name = f"tasks_corrupted_{timestamp}.json"
                backup_file_path = os.path.join(BASE_DIR, backup_name)
                os.rename(TASKS_FILE, backup_file_path)
                print(f"Corrupted file safely preserved as: {backup_file_path}")
                print("Creating a new clean tasks.json file")
                with open(TASKS_FILE, "w", encoding="utf-8") as file:
                    json.dump([], file, indent=4)
                return []
            elif corrupted_json_choice == "2":
                print("Exiting. Goodbye!")
                exit()
            else:
                print("Invalid choice. Please type 1 or 2.")
def show_tasks(tasks):
    for number, task in enumerate(tasks, start=1):
        if task["completed"] == True:
            print(number, "[X]", task["name"])
        else:
            print(number, "[ ]", task["name"])
def add_task(tasks):
    new_task = input("What text to add?: ")
    if not new_task:
        print("Invalid entry: cannot be empty.")
        return False
    new_task_data = {
        "name": new_task,
        "completed": False
    }
    tasks.append(new_task_data)
    print("Task added sucessfully.")
    return True
def save_task(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)
def complete_task(tasks):
    show_tasks(tasks)
    try:
        task_number = int(input("Choose what to change: "))
    except ValueError:
        print("Invalid number")
        return False
    if 1 <= task_number <= len(tasks):
        selected_task = tasks[task_number - 1]
        try:
            new_status = int(input("1 for true, 2 for false: "))
        except ValueError:
            print("Invalid entry: cannot be text.")
            return False
        if new_status == 1:
            if selected_task["completed"] == True:
                print("Task is already completed. No changes made.")
                return False
            selected_task["completed"] = True
            print("Task change to completed.")
            return True
        elif new_status == 2:
            if selected_task["completed"] == False:
                print("Task is already marked as not completed. No changes made.")
                return False
            selected_task["completed"] = False
            print("Task changed to not completed.")
            return True
        else:
             print("Invalid statement.")
             return False
    else:
        print("Invalid task number.")
        return False
def delete_task(tasks):
    show_tasks(tasks)
    try:
        delete_number = int(input("Choose what to delete: "))
    except ValueError:
        print("Invalid number.")
        return False
    if 1 <= delete_number <= len(tasks):
        tasks.pop(delete_number - 1)
        print("Task deleted sucessfully.")
        return True
    else:
        print("Invalid task number.")
        return False
def rename_task(tasks):
    show_tasks(tasks)
    try:
        task_number = int(input("Choose what to rename: "))
    except ValueError:
        print("Invalid number.")
        return False
    if 1 <= task_number <= len(tasks):
        rename_task_text = input("New name?: ")
        if not rename_task_text:
            print("Invalid entry: Name cannot be empty.")
            return False
        if tasks[task_number - 1]["name"] == rename_task_text:
            print("Cannot rename to the same name!")
            return False
        else:    
            tasks[task_number - 1]["name"] = rename_task_text
            print("Task renamed sucessfully")
            return True
    else:
        print("Invalid task number.")
        return False
def search_task(tasks):
    search_task_input = input("What do you want to find?: ").strip()
    if not search_task_input:
        print("Invalid entry: Name cannot be empty or only spaces.")
        return
    filtered_tasks = []
    for number, task in enumerate(tasks, start=1):
        if search_task_input.lower() in task["name"].lower():
            filtered_tasks.append((number, task))
    if filtered_tasks:
        print(f"\nFound {len(filtered_tasks)} matching task(s):")
        for original_number, task in filtered_tasks:
            if task["completed"] == True:
                print(original_number, "[X]", task["name"])
            else:
                print(original_number, "[ ]", task["name"])
    else:
        print(f"No tasks found matching '{search_task_input}'.")
