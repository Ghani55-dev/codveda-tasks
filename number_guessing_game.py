# Import the random module to generate random numbers
import random

# Function to play the number guessing game
def number_guessing_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    max_attempts = 7  # Set the maximum number of allowed attempts
    attempts = 0  # Initialize attempt counter

    print("🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Loop until the user runs out of attempts or guesses the number
    while attempts < max_attempts:
        try:
            # Prompt the user to input a guess and convert it to an integer
            guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts}: Enter your guess: "))
        except ValueError:
            # Handle non-integer input
            print("⚠️ Please enter a valid number.")
            continue  # Skip to the next loop iteration

        attempts += 1  # Increment attempt counter

        # Provide feedback on the guess
        if guess < number_to_guess:
            print("📉 Too low!")  # Guess is lower than the target number
        elif guess > number_to_guess:
            print("📈 Too high!")  # Guess is higher than the target number
        else:
            # Guess is correct
            print(f"🎉 Correct! You guessed the number in {attempts} attempts.")
            break  # Exit the loop if the guess is correct
    else:
        # This block runs if the loop completes without a correct guess
        print(f"\n❌ Sorry, you've run out of attempts. The number was {number_to_guess}.")

# If this script is run directly (not imported), start the game
if __name__ == "__main__":
    number_guessing_game()
