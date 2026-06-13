# Student Marks Tracker

A Python mini project that allows users to manage student records and calculate statistics. Data is saved permanently using JSON file storage.

## Features
- Add students with marks (1-8 subjects per student)
- View all students and their marks
- Calculate stats for a student
- Find topper
- Delete student with confirmation
- Duplicate student check with override
- Input validation
- Data persists after program closes

## Concepts Used
- Dictionaries
- Lists
- Functions
- If-Else
- Loops
- Exception Handling
- File Handling (JSON)
- json module

## How to Run
```
python student_marks_tracker.py
```

## Requirements
- Python 3.x

## Menu Options

| Option | Action |
|--------|--------|
|    1   | Add Student |
|    2   | View All Students |
|    3   | Calculate Stats |
|    4   | Find Topper |
|    5   | Delete Student |
|    6   | Exit |

## Grading System
Grading system same as Grade Calculator

## Sample Output
```
Enter your choice: 1
Enter the student name: John
Enter the number of subjects: 3
Enter marks of subject 1/3: 85
Enter marks of subject 2/3: 90
Enter marks of subject 3/3: 78
New Student Added
Student: John
Marks: [85, 90, 78]
```