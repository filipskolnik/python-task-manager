import json
from functions import *
tasks = load_task()
option = ""
while option != "7":
    print("=== TASK MANAGER ===")
    print("1. Add text")
    print("2. Show tasks")
    print("3. Find tasks")
    print("4. Complete task")
    print("5. Rename task")
    print("6. Delete task")
    print("7. Exit")
    print()
    option = input("Choose an option: ")    
    if option == "1":
        if add_task(tasks):
            save_task(tasks)
    elif option == "2":
        if len(tasks) == 0:
            print("No tasks.")
        else:
            show_tasks(tasks)
    elif option == "3":
        search_task(tasks)
    elif option == "4":
        if len(tasks) > 0:
            if complete_task(tasks):
                save_task(tasks)
        else:
            print("No tasks.")
    elif option == "5":
        if len(tasks) > 0:
            if rename_task(tasks):
                save_task(tasks)
        else:
            print("No tasks.")
    elif option == "6":
        if len(tasks) > 0:
            if delete_task(tasks):
                save_task(tasks)
        else:
            print("Nothing to delete!")
    elif option == "7":
        exit()
    else:
        print("Invalid option.")