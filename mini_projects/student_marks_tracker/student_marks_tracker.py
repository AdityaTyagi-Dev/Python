import json

print("Welcome to Student Marks Tracker\n")

try:
    with open("student_marks_tracker.json","r") as file:
        data = json.load(file)
except (json.JSONDecodeError, FileNotFoundError):
    with open("student_marks_tracker.json","w") as file:
        json.dump({}, file)

def grade(percent):
    if percent >= 90:
        return 'A+'
    elif percent >= 80:
        return 'A'
    elif percent >= 70:
        return 'B'
    elif percent >= 60:
        return 'C'
    elif percent >= 50:
        return 'D'
    elif percent >= 40:
        return 'P'
    else:
        return 'F'
    
def input_name():
    while True:
        try:
            name = input("Enter the student name: ")
            if not name or len(name) < 3:
                raise ValueError
            if not name.replace(" ","").isalpha():
                raise ValueError
            name = name.capitalize()
            return name
        except ValueError:
            print("Incorrect name\n")

def input_sub():
    while True:
        try:
            num_of_sub = int(input("Enter the number of subjects: "))
            if (num_of_sub < 1) or (num_of_sub > 8):
                raise ValueError
            print()
            return num_of_sub
        except ValueError:
            print("Incorrect number of subjects\n")

def input_marks(num):
    count = 0
    mark = []
    while count < num:
        try:
            m = int(input(f"Enter marks of subject {count + 1}/{num}: "))
            if (m > 100) or (m < 0):
                raise ValueError
            count +=1
            mark.append(m)
            print()
        except ValueError:
            print("Incorrect number of marks\n")
    return mark

def add():
    name = input_name()
    marks = input_marks(input_sub())
    confirm_add = True
    try:
        with open("student_marks_tracker.json","r") as file:
            data = json.load(file)
        if name in data:
            print(f"Student {name} is already entered !!")
            print("Entering yes will override the data, otherwise addition will be cancelled")
            confirm = input("(yes/no): ")
            if confirm.lower() == "yes":
                confirm_add = True
            else:
                confirm_add = False
        if confirm_add:
            data[name] = marks
            print("New Student Added")
            print(f"Student: {name}")
            print(f"Marks: {data[name]}\n")
            with open("student_marks_tracker.json", "w") as file2:
                json.dump(data, file2, indent = 4)

        else:
            print("Addition of data canceled\n")
    except:
        with open("student_marks_tracker.json","w") as file:
            data = {name : marks}
            json.dump(data, file, indent=4)
            

def view():
    try:
        with open("student_marks_tracker.json","r") as file:
            data = json.load(file)
            if not data:
                raise ValueError
        print("| Name | Marks |")
        for name in data:
            print(f"| {name} | {data[name]}")
    except ValueError:
        print("No Student!!")
    finally:
        print()

def stat():
    try:
        with open("student_marks_tracker.json","r") as file:
            data = json.load(file)
            if not data:
                raise ValueError
        while True:
            try:
                name = input_name()
                name = name.capitalize()
                if name not in data:
                    raise ValueError
                break
            except ValueError:
                print("Incorrect name\n")
        print(f"Name: {name}")
        print(f"Marks: {data[name]}")
        sum_of_marks = sum(data[name])
        percentage = round(sum_of_marks / len(data[name]), 2)
        print(f"Percentage: {percentage}%")
        print(f"Grade: {grade(percentage)}")
        print(f"Highest: {max(data[name])}")
        print(f"Lowest: {min(data[name])}")
    except ValueError:
        print("No Student!!")
    finally:
        print()

def topper():
    try:
        with open("student_marks_tracker.json","r") as file:
            data = json.load(file)
            if not data:
                raise ValueError   
        top_name = next(iter(data))
        highest = round(sum(data[top_name]) / len(data[top_name]), 2)
        for name, marks in data.items():
            percentage = round(sum(marks) / len(marks), 2)
            if percentage > highest:
                highest = percentage
                top_name = name
        print("Topper Details:")
        print(f"Name: {top_name}")
        print(f"Marks: {data[top_name]}")
        print(f"Percentage: {highest}")
        print(f"Grade: {grade(highest)}")
    except ValueError:
        print("No Student!!")
    finally:
        print()

def delete():
    try:
        with open("student_marks_tracker.json","r") as file:
            data = json.load(file)
            if not data:
                raise ValueError
        print("| Name | Marks |")
        for name, marks in data.items():
            print(f"| {name} | {marks} |")
        print()
        while True:
            try:
                name = input("Enter the name of student to be deleted: ")
                if name.capitalize() not in data:
                    raise ValueError
                name = name.capitalize()
                print("Are you sure you want to delete this entry:")
                print(f"| {name} | {data[name]} |")
                print()
                confirm = input("(yes/no): ")
                if confirm.lower() == 'yes':
                    deleted = True
                    break
                else:
                    deleted = False
                    break
            except ValueError:
                print("Incorrect input\n")
        if deleted:
            del data[name]
            with open("student_marks_tracker.json","w") as file:
                json.dump(data, file, indent = 4)
            print("Deleted successfully")
        else:
            print("Deletion canceled")
    except ValueError:
        print("No Student!!")
    finally:
        print()

while True:
    print("- Enter 1 for 'ADD STUDENT'")
    print("- Enter 2 for 'VIEW ALL STUDENTS'")
    print("- Enter 3 for 'CALCULATE STATS FOR A STUDENT'")
    print("- Enter 4 for 'FIND TOPPER'")
    print("- Enter 5 for 'DELETE A STUDENT'")
    print("- Enter 6 for 'EXIT'")

    try:
        choice = int(input("Enter your choice: "))
        if choice not in [1,2,3,4,5,6]:
            raise ValueError
        print()
    except ValueError:
        print("You have entered invalid input\n")
        continue

    if choice == 1:
        add()

    elif choice == 2:
        view()

    elif choice == 3:
        stat()

    elif choice == 4:
        topper()

    elif choice == 5:
        delete()
        
    else:
        print("Thanks for using Student Marks Tracker")
        break