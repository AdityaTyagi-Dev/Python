# Contact Book

A Python project that allows users to manage their contacts through a simple menu-driven interface. Data is saved permanently using JSON file storage.

## Features
- Add contacts with name, phone and email
- View all contacts
- Search contact by name, phone or email
- Edit specific fields of a contact
- Delete contact with confirmation
- Duplicate contact check with override
- Input validation (international phone numbers, email format)
- Data persists after program closes

## Concepts Used
- Dictionaries
- Lists
- Functions
- If-Else
- Loops
- Exception Handling
- File Handling (JSON)
- String Methods
- json module

## How to Run
Run the Python file using:
```
python contact_book.py
```

## Requirements
- Python 3.x

## Menu Options

| Option | Action |
|--------|--------|
|    1   | Add Contact |
|    2   | View All Contacts |
|    3   | Search Contact |
|    4   | Edit Contact |
|    5   | Delete Contact |
|    6   | Exit |

## Sample Output
```
Enter the name: John
Enter phone number: +91 9876543210
Enter email: john@gmail.com
New contact added
Name: John
Phone: +91 9876543210
Email: john@gmail.com
```