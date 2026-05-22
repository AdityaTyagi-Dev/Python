print("Welcome to To Do List\n")

tasks = []
while True:
    print("- Enter 1 for 'ADDING TASK'")
    print("- Enter 2 for 'VIEWING TASKS'")
    print("- Enter 3 for 'DELETING TASK'")
    print("- Enter 4 for 'EXITING THE PROGRAM'\n")

    try:
        choice = int(input("Enter your choice: "))
        if choice > 4 or choice < 1:
            raise ValueError
        print()
        
    except ValueError:
        print("You have entered invalid input\n")
        continue

    if choice == 1:
        task = input("Enter the task to be added: ")
        tasks.append(task)
        print(f"New task added: {task}\n")

    elif choice == 2:
        if len(tasks) == 0:
            print("You have no tasks!")
        else:
            print(f"You have {len(tasks)} task(s):")
            for task in tasks:
                print(f"- {task}")
        print()

    elif choice == 3:
        if len(tasks) == 0:
            print("You have no tasks!")
        else:
            while True:
                try:
                    print("These are the tasks you are currently having:")
                    for i in range(len(tasks)):
                        print(f"{i+1}. {tasks[i]}")
                    print()
                    n = int(input("Enter the serial number of task to be deleted: "))
                    if n > len(tasks) or n < 1:
                        raise ValueError
                    confirm = input(f"Are you sure you want to delete '{tasks[n-1]}'? (yes/no): ")
                    if confirm.lower() == 'yes':
                        deleted = True
                        break
                    else:
                        deleted = False
                        break

                except ValueError:
                    print("You have entered invalid input\n")
                    continue
            if deleted:
                print(f"Task is deleted: {tasks[n-1]}")
                tasks.pop(n - 1)
            else:
                print("Task Deletion Canceled")
        print()

    else:
        print("Thanks for using To Do List")
        break