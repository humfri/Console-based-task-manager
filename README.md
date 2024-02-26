# Task Manager

A simple command-line task manager written in Python. The task manager allows you to add tasks, set task start time, task duration, mark them as complete, and view the list of tasks. Additionally, it provides task reminders through system notifications using the `plyer` library.

## Features

- **Add Task**: Enter a task description, start time (HH:MM format), and task duration in hours. The task will be added to the list with start and end times.

- **Show Tasks**: View the list of tasks and completion status.

- **Mark Task as Complete**: Mark a task as complete by specifying its index in the list of tasks.

- **Task Reminders**: Receive system notifications for added tasks with details about the task, start time, and end time.


## Usage

Choose an option from the menu by entering the corresponding number.
- For adding a task, provide the task description, start time, and duration when prompted.
- View tasks, mark them as complete, or exit the Task Manager.
  
## tasks.json File
The tasks are stored in a JSON file named tasks.json. This file will contain an array of tasks, each represented as a JSON object with fields such as description, complete, created_at, start_time, and end_time. You can aswell view and edit this file to manage your tasks manually.

## Dependencies
- plyer - A Python library for accessing features commonly found on various platforms.
  
## Contributing
Contributions are welcome! If you have suggestions, improvements, or find any issues, feel free to open an issue or create a pull request.

## License
This project is licensed under the MIT License
