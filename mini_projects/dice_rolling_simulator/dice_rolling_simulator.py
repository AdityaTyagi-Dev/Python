import random
import statistics

print("Welcome to Dice Rolling Simulator\n")
def num_of_dice():
    while True:
        try:
            num = int(input("Enter the number of dice: "))
            if num < 1:
                raise ValueError
            print()
            return num
        except ValueError:
            print("Invalid number of dice\n")

def num_of_turns():
    while True:
        try:
            num = int(input("Enter the number of turns: "))
            if num < 1:
                raise ValueError
            return num
        except ValueError:
            print("Invalid number of turns")
        finally:
            print()

def turn(dice, num):
    all_turn = []
    for i in range(num):
        per_turn = []
        for j in range(dice):
            per_turn.append(random.randint(1, 6))
        print(f"Roll {i + 1}: {per_turn} -> Sum: {sum(per_turn)}")
        all_turn.append(per_turn)
    return all_turn

def stat(result, num):
    data = []
    for i in result:
        for j in i:
            data.append(j)
    print()
    print(f"Total Rolls: {num}")
    print(f"All Values: {data}")
    print("--- Statistics ---")
    print(f"Mean: {round(statistics.mean(data), 2)}")
    print(f"Median: {statistics.median(data)}")
    print(f"Mode: {calculate_mode(data)}")
    print(f"Highest: {max(data)}")
    print(f"Lowest: {min(data)}\n")

def calculate_mode(data):
    max_count = max(data.count(i) for i in data)
    if max_count == 1:
        return "No mode"
    modes = list(set(i for i in data if data.count(i) == max_count))
    return modes

while True:
    dice = num_of_dice()
    turns = num_of_turns()
    stat(turn(dice, turns), turns)
    print("Enter yes to try again")
    choose = input("(yes/no): ")
    if choose.lower() == 'yes':
        continue
    print("Thanks for using the Dice Rolling Simulator")
    break