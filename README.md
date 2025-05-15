# Codveda Internship - Level 1 Tasks

## ✅ Task 1: Simple Calculator

This Python program performs basic arithmetic operations: addition, subtraction, multiplication, and division.

### Features
- Handles user input
- Catches division by zero errors
- Uses Python functions for modular code

### How to Run
```bash
python simple_calculator.py

# codveda-tasks
Sample output
Enter first number: 10  
Enter second number: 5  
Enter operation (+ - * /): *  
Result: 50.0


#----------------------------------------------------------------------------------------------------------------------
---

## ✅ Task 2: Number Guessing Game

This Python program generates a random number between 1 and 100. The user has a limited number of attempts to guess the number, with hints provided after each guess.

### Features
- Random number generation using `random.randint()`
- User feedback on each guess: "Too high", "Too low", or "Correct!"
- Maximum number of attempts
- Input validation using `try/except`

### How to Run

```bash
python number_guessing_game.py

Sample output:
🎯 Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.

Attempt 1/7: Enter your guess: 50  
📈 Too high!

Attempt 2/7: Enter your guess: 30  
📉 Too low!

Attempt 3/7: Enter your guess: 42  
🎉 Correct! You guessed the number in 3 attempts.
