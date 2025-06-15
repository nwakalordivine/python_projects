# let computer guess a random number between 1 and 100
import random
from utilis import logo

EASY_MODE_TRIAL = 10
HARD_MODE_TRIAL = 5


def generate_number():
    """Generates a random number between 1 - 100 """
    computer_choice = random.randint(1, 100)
    return computer_choice


def status(user, computer_generated_number):
    """Compares user's guess to the correct number and prints hint feedback."""
    if user > computer_generated_number:
        print("Too high.\nGuess again.")
    elif user < computer_generated_number:
        print("Too low.\nGuess again.")


def operation(trials, computer_generated_number):
    """Informs the player of how many trials a player has and lets player guess again if they guessed wrong"""
    print(f"You have {trials + 1} attempts remaining to guess the number.")
    user_guessed = int(input("Make a guess: "))
    if trials != 0:
        status(user_guessed, computer_generated_number)
    else:
        return user_guessed
    return user_guessed


def play_game(trials):
    """The player has 10 or 5 trials in this function, this functions sorts if trials draw down to 0 player lose
    but if they guess right and trial != 0 player wins"""
    computer_generated_number = generate_number()
    print(f"You have {trials+1} attempts remaining to guess the number")
    user_guessed = int(input("Make a guess: "))
    status(user_guessed, computer_generated_number)

    while user_guessed != computer_generated_number and trials != 0:
        trials -= 1
        user_guessed = operation(trials, computer_generated_number)

    if user_guessed == computer_generated_number and trials != 0:
        return f"You got it! The answer was {computer_generated_number}"
    if trials == 0:
        return "You've run out of guesses. Refresh the page to run again."


def game_start():
    """This function takes player to their desired difficulty level (hard or easy)"""
    print(logo)
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    difficulty_choice = input("Choose a difficulty. Type 'easy' or 'hard': ").strip().lower()
    if difficulty_choice == "easy":
        print(play_game(EASY_MODE_TRIAL-1))
    elif difficulty_choice == "hard":
        print(play_game(HARD_MODE_TRIAL-1))
    else:
        print("Invalid entry")


game_start()
