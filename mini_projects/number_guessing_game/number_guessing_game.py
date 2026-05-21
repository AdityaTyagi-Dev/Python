import random

print("Welcome to Number Guessing Game\n")

while True:
    try:
        print("Enter the difficulty of game\n1 for easy (1 to 50)\n2 for medium (1 to 100)\n3 for hard (1 to 200)")
        lvl = int(input("Enter the level: "))
        if lvl == 1:
            num = random.randint(1,50)
        elif lvl == 2:
            num = random.randint(1,100)
        elif lvl == 3:
            num = random.randint(1,200)
        else:
            raise ValueError
    except ValueError:
        print("You have entered invalid input")
        continue
    print()
    count = 0
    while True:
        try:
            entNum = int(input(f"Guess the number [Attempt {count+1}/10]: "))
            count += 1
            if entNum > num:
                print("You have guessed too high\n")
            elif entNum < num:
                print("You have guessed too low\n")
            else:
                print(f"Congratulations! you guessed right on attempt {count}\n")
                break
            if count == 10:
                print(f"Better luck next time! The number was {num}.\n")
                break
        except ValueError:
            print("You have entered incorrect input\n")
    print("Enter 'exit' to quit the game, hit enter to continue the game")
    choice = input("Enter your choice: ")
    if choice.lower() == 'exit':
        break

print("\nThanks for playing Number Guessing Game")