"""Binary Search Approach:
The user selects a range (lets say from A to B, where A and B are integers).
The computer randomly selects an integer within that range.
The user starts guessing numbers.
After each guess, the computer provides feedback (e.g., “Try Again! You guessed too high” or “Try Again! You guessed too small”).
The user continues guessing, narrowing down the range intelligently.
The game ends when the user correctly guesses the number.
The goal is to minimize the number of guesses.
Example: If the range is 1 to 100, the user might guess 50, then 25, then 37, and so on, until they find the correct number (e.g., 42) 1.
Random Number Approach:
The computer generates a random number between 1 and 99 using the randint() function from the random module.
The user inputs their guessed number.
A while loop is used to implement the program logic.
The user keeps guessing until they get the correct number.
Example: If the computer randomly selects 42, the user might guess 25, then 37, and finally 42 """

import random

def main():
    print("Welcome to the Number Guessing Game!")
    print("I've selected a random number between 1 and 99.")
    print("Try to guess it!")

    # Generate a random number between 1 and 99
    secret_number = random.randint(1, 99)

    attempts = 0
    while True:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            if user_guess == secret_number:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
                break
            elif user_guess < secret_number:
                print("Try again! Your guess is too low.")
            else:
                print("Try again! Your guess is too high.")
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    main()