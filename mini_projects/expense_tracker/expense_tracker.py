import csv
import datetime

try:
    with open("expense_tracker.csv", "r") as file:
        r = csv.reader(file)
        if not r:
            raise FileNotFoundError
        count = []
        for i in r:
            count.append(i)
        if count[0] != ["Date", "Expense", "Category"]:
            raise FileNotFoundError
except FileNotFoundError:
    with open("expense_tracker.csv", "w", newline="") as file:
        w = csv.writer(file)
        w.writerow(["Date", "Expense", "Category"])

def input_expense():
    while True:
        try:
            money = int(input("Enter the amount: "))
            if money < 1:
                raise ValueError
            print()
            return money
        except ValueError:
            print("Invalid Amount\n")

def input_category():
    while True:
        try:
            print("Pick the category")
            print("-Enter 1 for 'FOOD'")
            print("-Enter 2 for 'TRAVEL'")
            print("-Enter 3 for 'SHOPPING'")
            print("-Enter 4 for 'OTHERS'\n")
            category = int(input("Enter the category: "))
            if category not in [1, 2, 3, 4]:
                raise ValueError
            print()
            if category == 1:
                return 'FOOD'
            elif category == 2:
                return 'TRAVEL'
            elif category == 3:
                return 'SHOPPING'
            else:
                return 'OTHERS'
        except ValueError:
            print("Invalid input\n")

def add(expense, category):
    date = datetime.datetime.now().strftime("%d/%m/%Y")
    data = [date, expense, category]
    with open("expense_tracker.csv", "a", newline="") as file:
        w = csv.writer(file)
        data = [date, expense, category]
        w.writerow(data)
    print(f"Data added successfully: {data}")

def view_all():
    with open("expense_tracker.csv", "r") as file:
        r = csv.reader(file)
        count = []
        for i in r:
            count.append(i)
    if len(count) == 1:
        print("No Data\n")
        return
    for i in count:
        print(i)
    print()

def view_by_category(category):
    with open("expense_tracker.csv", "r") as file:
        r = csv.reader(file)
        l = []
        for i in r:
            if i[2] == category:
                l.append(i)
    if len(l) == 0:
        print("No Data\n")
        return
    print(["Date", "Expense", "Category"])
    for i in l:
        print(i)
    print()

def all_spending():
    total = 0
    with open("expense_tracker.csv", "r") as file:
        r = csv.reader(file)
        count = []
        for i in r:
            count.append(i)
    for i in range(1, len(count)):
        total += int(count[i][1])
    return total
    
def summary():
    with open("expense_tracker.csv", "r") as file:
        r = csv.reader(file)
        count = []
        for i in r:
            count.append(i)
    for i in ["FOOD", "TRAVEL", "SHOPPING", "OTHERS"]:
        total = 0
        for j in range(1, len(count)):
            if count[j][2] == i:
                total += int(count[j][1])
        print(f"Category: {i}")
        print(f"Expense: {total}")
        print()
    print()

print("Welcome to Expense Tracker\n")
while True:
    try:
        print("- Enter 1 for 'ADDING EXPENSE'")
        print("- Enter 2 for 'VIEWING ALL EXPENSES'")
        print("- Enter 3 for 'VIEWING ALL EXPENSES (FILTER BY CATEGORY)'")
        print("- Enter 4 for 'ALL SPENDINGS'")
        print("- Enter 5 for 'SUMMARY'")
        print("- Enter 6 for 'EXIT'")
        choice = int(input("Enter your choice: "))
        if choice not in [1, 2, 3, 4, 5, 6]:
            raise ValueError
        print()
    except ValueError:
        print("Invalid input\n")
        continue
    if choice == 1:
        expense = input_expense()
        category = input_category()
        add(expense, category)

    elif choice == 2:
        view_all()

    elif choice == 3:
        category = input_category()
        view_by_category(category)

    elif choice == 4:
        print(all_spending())
        print()

    elif choice == 5:
        summary()

    else:
        print("Thanks for using the expense tracker.")
        break