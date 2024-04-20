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
