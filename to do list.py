tasks = []

def show_tasks():
    print("\nYour To-Do List:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added!")

def remove_task():
    show_tasks()
    task_num = int(input("Enter the number of the task to remove: "))
    tasks.pop(task_num - 1)
    print("Task removed!")

while True:
    print("Options: " 
    "1. Add Task " 
    "2. Remove Task " 
    "3. Show Tasks " 
    "4. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        add_task()
    elif choice == '2':
        remove_task()
    elif choice == '3':
        show_tasks()
    elif choice == '4':
        break
    else:
        print("Invalid choice.")