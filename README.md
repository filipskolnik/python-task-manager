# Python Task Manager

A simple command-line task manager written in Python. It lets you organize tasks and saves changes to a local JSON file.

## Features

- Add new tasks.
- List tasks with their completion status.
- Search for tasks by full or partial name (case-insensitive).
- Mark tasks as completed or not completed.
- Rename existing tasks.
- Delete tasks.
- Automatically save changes to `tasks.json`.
- Handle invalid menu selections and task numbers.
- Detect invalid JSON and offer to preserve the original file as a timestamped backup before creating a new one.

## Requirements

- Python 3
- No third-party packages required (standard library only)

## Getting started

1. Clone or download this repository.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python main.py
   ```

   On Windows, you can also use `py main.py` if Python is installed through the Python launcher.

4. Follow the on-screen menu.

## Menu

```text
=== TASK MANAGER ===
1. Add text
2. Show tasks
3. Find tasks
4. Complete task
5. Rename task
6. Delete task
7. Exit
```

The **Complete task** option can mark a task as either completed or not completed.

## Data storage

Task data is stored in `tasks.json` in the same folder as the Python source files. The file is created automatically if it does not exist. Changes are saved after successful additions, status updates, renames, and deletions.

Example data:

```json
[
    {
        "name": "Learn Python",
        "completed": false
    },
    {
        "name": "Finish my project",
        "completed": true
    }
]
```

If `tasks.json` contains invalid JSON, the application prompts you to either exit without changing it or create a new empty file. If you choose to create a new file, the original is renamed to a timestamped `tasks_corrupted_*.json` backup.

Personal task data and corrupted-file backups are excluded from Git using `.gitignore`.

## Project structure

```text
task-manager/
├── main.py          # Menu and application flow
├── functions.py     # Task operations and JSON storage
├── .gitignore       # Files excluded from Git
└── README.md        # Project documentation
```

`tasks.json` is generated when the app runs, so it is not included in the repository.

## About

This is a learning project built to practice Python fundamentals, functions, lists, dictionaries, file operations, error handling, and Git.
