class Student:  # defining a class

    school = "ABC School"
    def __init__(self, name, age):  # making a constructor
        self.name = name
        self.age = age

    def introduce(self):  # making a method
        print(f"My name is {self.name}")

s1 = Student("Rahul", 17)  # creating objects
s2 = Student("Anita", 18)

s1.school = "XYZ School"

s1.introduce()
s2.introduce()