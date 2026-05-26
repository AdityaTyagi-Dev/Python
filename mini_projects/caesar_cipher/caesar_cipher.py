print("Welcome to Caesar Cipher\n")

def input_key():
    while True:
        try:
            key = int(input("Enter the key: "))
            return key
        except ValueError:
            print("Invalid input\n")

def encrypt(text, key):
    encrypted_message = ""
    for i in text:
        if i.isupper():
            ch = chr((ord(i) - 65 + key) % 26 + 65)
            encrypted_message += ch
        elif i.islower():
            ch = chr((ord(i) - 97 + key) % 26 + 97)
            encrypted_message += ch
        else:
            encrypted_message += i

    return encrypted_message

while True:
    print("- Enter 1 to 'ENCRYPT A MESSAGE'")
    print("- Enter 2 to 'DECRYPT A MESSAGE'")
    print("- Enter 3 to 'EXIT'")
    try:
        choice = int(input("Enter your choice: "))
        if choice not in [1, 2, 3]:
            raise ValueError
        print()
    except ValueError:
        print("Invalid Input\n")
        continue

    if choice == 1:
        message = input("Enter the message: ")
        key = input_key()
        encrypted_message = encrypt(message, key)
        print("Encrypted message:")
        print(encrypted_message)
        print()

    elif choice == 2:
        message = input("Enter the encrypted message: ")
        key = input_key()
        decrypted_message = encrypt(message, -key)
        print("Decrypted message:")
        print(decrypted_message)
        print()

    else:
        break

print("Thanks for using Caesar Cipher")