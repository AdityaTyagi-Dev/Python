import datetime

print("Welcome to To Do List\n")
with open("to_do_list.txt", "a") as file:
    pass

def input_task():
    while True:
        print("- Enter 1 for 'ADDING TASKS'")
        print("- Enter 2 for 'VIEWING TASKS'")
        print("- Enter 3 for 'DELETING TASKS'")
        print("- Enter 4 for 'EXITING THE PROGRAM'")

        try:
            choice = int(input("Enter your choice: "))
            if choice not in [1, 2, 3, 4]:
                raise ValueError
            print()
            return choice

        except ValueError:
            print("You have entered invalid input\n")

def add_task():
    while True:
        try:
            task = input("Enter the task to be added: ")
            if not task:
                raise ValueError
            date = datetime.datetime.now().strftime("<<%d/%m/%y, %H:%M>>")
            task = date + ' ' + task + '\n'
            with open("to_do_list.txt", "a") as file:
                file.write(task)
            print(f"New task added: {task}")
            break
        except ValueError:
            print("Invalid task!\n")

def view_task():
    with open("to_do_list.txt", "r") as file:
        tasks = file.readlines()
        if len(tasks) == 0:
            print("You have no tasks!")
        else:
            for task in tasks:
                print(task.replace("\n", ""))
        print()

def delete_task():
    with open("to_do_list.txt", "r") as file:
        tasks = file.readlines()
        if len(tasks) == 0:
            print("You have no tasks!\n")
        else:
            while True:
                try:
                    print("These are the tasks you are currently having:")
                    for i in range(len(tasks)):
                        print(f"{i + 1}. {tasks[i].replace("\n", "")}")
                    print()
                    n = int(input("Enter the serial number of task to be deleted: "))
                    if n > len(tasks) or n < 1:
                        raise ValueError
                    confirm = input(f"Are you sure you want to delete {tasks[n - 1].replace("\n", "")[19:]} ? (yes/no): ")
                    if confirm.lower() == 'yes':
                        deleted = True
                        break
                    else:
                        deleted = False
                        break
                except ValueError:
                    print("You have entered invalid input\n")
            if deleted:
                print(f"Task is deleted: {tasks[n - 1].replace("\n", "")[19:]}")
                tasks.pop(n - 1)
                with open("to_do_list.txt","w") as file2:
                    file2.writelines(tasks)
            else:
                print("Task Deletion Canceled")
            print()

            

while True:
    choice = input_task()
    if choice == 1:
        add_task()
    elif choice == 2:
        view_task()
    elif choice == 3:
        delete_task()
    else:
        print("Thanks for using To Do List")
        break