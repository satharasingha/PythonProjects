# Start of the To-Do List Program

# Create an empty list to store all tasks
todo_list = []

# Display a welcome message and menu options for the user
print("Welcome to the To-Do List")

# Use a while loop so the menu keeps showing until the user chooses to exit
while True:
    choose = input("What do you want to do? Add Task (1), View Tasks (2), Remove Task (3), Exit (4): ")

    # If the user chooses "Add Task"
    if choose == "1":
        task = input("Enter the task: ")
        todo_list.append(task)
        print("Task added successfully!")

    # If the user chooses "View Tasks"
    elif choose == "2":
        if not todo_list:
            print("No tasks found.")
        else:
            print("Your Tasks:")
            for index, task in enumerate(todo_list, start=1):
                print(f"{index}. {task}")

    # If the user chooses "Remove Task"
    elif choose == "3":
        if not todo_list:
            print("No tasks to remove.")
        else:
            task_num = int(input("Enter the task number to remove: "))
            if 0 < task_num <= len(todo_list):
                removed = todo_list.pop(task_num - 1)
                print(f"Removed task: {removed}")
            else:
                print("Invalid task number!")

    # If the user chooses "Exit"
    elif choose == "4":
        print("Thank you for using the To-Do List!")
        break

    # Handle invalid input
    else:
        print("Invalid input, please try again.")
