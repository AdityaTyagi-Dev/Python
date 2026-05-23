print("Welcome to Contact Book\n")

contacts = {}
def add_contact(name, phone, email):
    add = True
    if name in contacts:
        print(f"Contact with the name: {name} already exist")
        print("Entering yes will overwrite the new data")
        confirm = input("(yes/no): ")
        if confirm.lower() != "yes":
            add = False
    if add:
        contacts[name] = [phone, email]
        print("New contact added")
        print(f"Name: {name}")
        print(f"Phone: {phone}")
        print(f"Email: {email}\n")
    else:
        print("Contact addition canceled")


def input_name():
    while True:
        try:
            name = input("Enter the name: ")
            if not name or len(name) < 3:
                raise ValueError
            if not name.replace(" ","").isalpha():
                raise ValueError
            return name.capitalize()
        except ValueError:
            print("Invalid name\n")

def input_phone():
    while True:
        try:
            number = input("Enter phone number: ")
            phone = number
            if not number:
                raise ValueError
            if number[0] == "+":
                number = number[1:]
            if "+" in number:
                raise ValueError
            number = (number.replace(" ","")).replace("-","")
            if len(number) < 7 or len(number) > 15:
                raise ValueError
            if not number.isdigit():
                raise ValueError
            return phone
        except ValueError:
            print("Invalid phone number\n")
                
def input_email():
    while True:
        try:
            email = input("Enter email: ")
            s_mail = email.split('@')
            if not len(s_mail) == 2:
                raise ValueError
            if s_mail[1].find(".") == -1:
                raise ValueError
            if email[-1] == ".":
                raise ValueError
            for i in email:
                if i.isspace():
                    raise ValueError
            if "@." in email:
                raise ValueError
            return email.lower()
        except ValueError:
            print("Invalid email\n")

def view_contacts():
    if not contacts:
        print("No Contact!\n")
    else:
        print("| Name | Phone | Email |")
        for name, contact in contacts.items():
            print(f"| {name} | {contact[0]} | {contact[1]} |")
        print()

def search_contact(search):
    found = None
    for name, contact in contacts.items():
        if search.lower() in [name.lower(), contact[0], contact[1]]:
            found = name
    if not found:
        print(f"No contact found with the search: {search}\n")
        return False
    else:
        return found

def edit_contact(search):
    name = search_contact(search)
    if not name:
        return None
    else:
        while True:
            try:
                print("- Enter 1 to change name")
                print("- Enter 2 to change phone")
                print("- Enter 3 to change email\n")
                choice = int(input("Enter your choice: "))
                if choice not in [1, 2, 3]:
                    raise ValueError
                if choice == 1:
                    new_name = input_name()
                    edit = True
                    if new_name in contacts:
                        print(f"Contact with the name: {new_name} already exist")
                        print("Entering yes will overwrite the new data")
                        confirm = input("(yes/no): ")
                        if confirm.lower() != "yes":
                            edit = False
                    if edit:
                        data = [new_name, contacts[name][0], contacts[name][1]]
                    else:
                        print("Contact Editing Canceled")
                        return None
                elif choice == 2:
                    new_phone = input_phone()
                    data = [name, new_phone, contacts[name][1]]
                else:
                    new_email = input_email()
                    data = [name, contacts[name][0], new_email]
                del contacts[name]
                contacts[data[0]] = data[1:]
                return None
            except ValueError:
                print("Invalid choice\n")

def delete_contact(search):
    name = search_contact(search)
    if not name:
        return None
    else:
        print("Are you sure you want to delete this")
        print(f"Name: {name}")
        print(f"Phone: {contacts[name][0]}")
        print(f"Email: {contacts[name][1]}\n")
        confirm = input("(yes/no): ")
        if confirm.lower() == "yes":
            del contacts[name]
            print("Contact deleted\n")
        else:
            print("Deletion Canceled\n")


while True:
    print("- Enter 1 for 'ADDING CONTACT'")
    print("- Enter 2 for 'VIEWING ALL CONTACTS'")
    print("- Enter 3 for 'SEARCHING CONTACT'")
    print("- Enter 4 for 'EDITING CONTACT'")
    print("- Enter 5 for 'DELETING CONTACT'")
    print("- Enter 6 for 'EXIT'\n")
    try:
        choice = int(input("Enter your choice: "))
        if choice not in [1, 2, 3, 4, 5, 6]:
            raise ValueError
    except ValueError:
        print("Invalid choice\n")
        continue

    print()

    if choice == 1:
        name = input_name()
        phone = input_phone()
        email = input_email()
        add_contact(name, phone, email)

    elif choice == 2:
        view_contacts()
    
    elif choice == 3:
        if not contacts:
            print("No contact!\n")
        else:
            search_by = input("Enter name/phone/email to search contact: ")
            found_name = search_contact(search_by)
            if found_name:
                print(f"Name: {found_name}")
                print(f"Phone: {contacts[found_name][0]}")
                print(f"Email: {contacts[found_name][1]}\n")

    elif choice == 4:
        if not contacts:
            print("No contact!\n")
        else:
            search_by = input("Enter name/phone/email to search contact: ")
            edit_contact(search_by)

    elif choice == 5:
        if not contacts:
            print("No contact!\n")
        else:
            search_by = input("Enter name/phone/email to search contact: ")
            delete_contact(search_by)

    else:
        print("Thanks for using Contact Book")
        break