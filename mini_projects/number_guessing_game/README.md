# Number Guessing Game

A python mini project where the user guesses a randomly generated number within a limited number of attempts.

## Features
- 3 Difficulty levels (Easy, Medium, Hard)
- 10 attempts limit per game
- High/Low hints after each guess
- Reveals number on losing
- Input Validation
- Play again option

## Concepts Used
- Loops
- Random Module
- If-Else
- Exception Handling
- User Input

## How to Run
Run the Python file using:

```
python number_guessing_game.py
```

## Requirements
- Python 3.x

## Difficulty Levels

| Level | Range |
|-------|-------|
|  Easy |  1-50 |
| Medium| 1-100 |
|  Hard | 1-200 |

## Sample Output
```
Enter the difficulty of game
1 for easy (1 to 50)
2 for medium (1 to 100)
3 for hard (1 to 200)
Enter the level: 2
Guess the number [Attempt 1/10]: 50
You have guessed too high
Guess the number [Attempt 2/10]: 25
You have guessed too low
Guess the number [Attempt 3/10]: 37
Congratulations! You guessed right on attempt 3
```
