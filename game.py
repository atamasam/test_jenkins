import random

def guess_number():
    number_to_guess = random.randint(1, 10)
    print("Welcome to the Guess-the-Number Game!")
    print("I'm thinking of a number between 1 and 10.")

    for _ in range(3):  # The player has 3 attempts
        try:
            guess = int(input("Take a guess: "))
            if guess == number_to_guess:
                print("Congratulations! You guessed the number!")
                return True
            elif guess < number_to_guess:
                print("Too low!")
            else:
                print("Too high!")
        except ValueError:
            print("Please enter a valid number!")
    print(f"Sorry, the number was {number_to_guess}. Better luck next time!")
    return False

if __name__ == "__main__":
    guess_number()