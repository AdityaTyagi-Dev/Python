print("Welcome to Grade Calculator\n\n")

while True:
    try:
        numOfSub = int(input("Enter the number of subjects: "))
        marks = []
        if numOfSub < 1:
            raise ValueError
        i = 0
        while i < numOfSub:
            try:
                mark = int(input(f"Enter marks of subject {i+1}: "))
                if mark > 100 or mark < 0:
                    raise ValueError
                marks.append(mark)
                i += 1
            except ValueError:
                print("You have entered incorrect marks, please try again\n")
                continue
        
        sumOfMarks = sum(marks)
        percentage = round(sumOfMarks / numOfSub, 2)
        if percentage >= 90:
            print(f"Percentage: {percentage}\nGrade: A+\n")
        elif percentage >= 80:
            print(f"Percentage: {percentage}\nGrade: A\n")
        elif percentage >= 70:
            print(f"Percentage: {percentage}\nGrade: B\n")
        elif percentage >= 60:
            print(f"Percentage: {percentage}\nGrade: C\n")
        elif percentage >= 50:
            print(f"Percentage: {percentage}\nGrade: D\n")
        elif percentage >= 40:
            print(f"Percentage: {percentage}\nGrade: P\n")
        else:
            print(f"Percentage: {percentage}\nGrade: F\n")
        

        print("Enter 'exit' to quit the program, hit enter for checking more grades")
        choice = input("Enter your choice: ")
        if choice.lower() == 'exit':
            break
    except ValueError:
        print("You have entered incorrect number of Subjects, please try again\n")

print("Thanks for using Grade Calculator")