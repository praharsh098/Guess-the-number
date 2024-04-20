# Guess-the-number
Develop a number-guessing game. It uses Binary search approach.. 

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
Example: If the computer randomly selects 42, the user might guess 25, then 37, and finally 42.
