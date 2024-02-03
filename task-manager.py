import json
from datetime import datetime, timedelta
import plyer

def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=2)

def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task['description']} - {'Complete' if task['complete'] else 'Incomplete'}")

def add_task(tasks, description):
    task_time = input("Enter task start time (HH:MM format): ")
    task_duration = float(input("Enter task duration in hours: "))

    try:
        # Parse the input time string to a datetime object
        start_time = datetime.strptime(task_time, "%H:%M")
    except ValueError:
        print("Invalid time format. Please use HH:MM format.")
        return

    # Capture the current date and time
    current_datetime = datetime.now()

    # Calculate end time based on start
    end_time = start_time + timedelta(hours=task_duration)

    task = {
        'description': description,
        'complete': False,
        'created_at': current_datetime.strftime("%Y-%m-%d %H:%M:%S"),  # Save the current date and time
        'start_time': start_time.strftime("%H:%M"),  # Save the start time as a string
        'end_time': end_time.strftime("%H:%M")  # Save the end time as a string
    }

    tasks.append(task)

    # Plyer notification
    reminder_message = f"Task added: {description} starting at {current_datetime.strftime('%Y-%m-%d %H:%M:%S')} and ending at {end_time.strftime('%H:%M')} on {current_datetime.strftime('%Y-%m-%d')}"
    plyer.notification.notify(title='Task Reminder', message=reminder_message, timeout=10, toast=True)

    print(f"Task added: {description} starting at {current_datetime.strftime('%Y-%m-%d %H:%M:%S')} and ending at {end_time.strftime('%H:%M')} on {current_datetime.strftime('%Y-%m-%d')}")

def mark_complete(tasks, index):
    if 1 <= index <= len(tasks):
        tasks[index - 1]['complete'] = True
        print(f"Task marked as complete: {tasks[index - 1]['description']}")
    else:
        print("Invalid task index.")

def main():
    tasks = load_tasks()

    while True:
        print("\nTask Manager Menu:")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Mark Task as Complete")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            description = input("Enter task description: ")
            add_task(tasks, description)
        elif choice == '3':
            index = int(input("Enter task index to mark as complete: "))
            mark_complete(tasks, index)
        elif choice == '4':
            save_tasks(tasks)
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
