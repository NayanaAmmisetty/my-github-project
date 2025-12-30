tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added successfully")

def view_tasks():
    for i, task in enumerate(tasks, 1):
        print(i, task)
print("debug")
