"""
ToDo App

This module implements a command-line to-do list application 
for efficient task organization.

Author: Asibeh Tenager
Date: 01/07/2023

Usage:
- Run the script to start the ToDo app.
- Follow the on-screen instructions to manage your to-do lists and tasks.

Actions:
     add - Add a new task to the ToDo list
     delete  - Delete a task from the ToDo list
     list   - List all tasks in the ToDo list
"""
tasks = []


def add_task():
    """
    Add a new task to the to-do list.
    """
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully.")


def view_tasks():
    """
    View the tasks in the to-do list.
    """
    if len(tasks) == 0:
        print("no tasks.")
    else:
        print('List of tasks:')
        for i, task in enumerate(tasks):
            print(f'{i+1}. {task}')


def delete_task():
    """
    Delete a task from the to-do list.
    """
    if len(tasks) == 0:
        print('no tasks to delete.')
    else:
        print('Tasks:')
        for i, task in enumerate(tasks):
            print(f'{i+1}. {task}')
        choice = int(input('Enter the task number to delete:'))

        if 0 < choice <= len(tasks):
            del tasks[choice-1]
            print('Task deleted successfully.')
        else:
            print('Invalid task number.')


def main():
    """
    Run the command-line to-do list application.
    """
    while True:
        print('\n===== To-Do-List Application =====')
        print("1. Add task")
        print('2. view task')
        print('3. Delete task')
        print('4. Quit')

        choice = int(input("Enter your choice:"))
        if choice == 1:
            add_task()
        elif choice == 2:
            view_tasks()
        elif choice == 3:
            delete_task()
        elif choice == 4:
            print("Thank you for using the To-Do-List Application.")
            break
        else:
            print('Invalid choice. Please try again.')


if __name__ == "__main__":
    main()
