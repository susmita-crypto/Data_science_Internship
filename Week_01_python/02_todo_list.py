tasks = []

print("Simple To-Do List")

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added successfully.")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")

            for number, task in enumerate(tasks, start=1):
                print(number, ".", task)

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            print("\nYour Tasks:")

            for number, task in enumerate(tasks, start=1):
                print(number, ".", task)

            task_number = int(input("Enter task number to remove: "))

            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print("Removed:", removed_task)
            else:
                print("Invalid task number.")

    elif choice == "4":
        print("To-do list closed.")
        break

    else:
        print("Invalid choice. Please try again.")