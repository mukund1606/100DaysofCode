# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

logo = """
   _____                       _______ _            _   _                 _               
  / ____|                     |__   __| |          | \\ | |               | |              
 | |  __ _   _  ___  ___ ___     | |  | |__   ___  |  \\| |_   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ \\/ __/ __|    | |  | '_ \\ / _ \\ | . ` | | | | '_ ` _ \\| '_ \\ / _ \\ '__|
 | |__| | |_| |  __/\\__ \\__ \\    | |  | | | |  __/ | |\\  | |_| | | | | | | |_) |  __/ |   
  \\_____|\\__,_|\\___||___/___/    |_|  |_| |_|\\___| |_| \\_|\\__,_|_| |_| |_|_.__/ \\___|_|   
"""


def clear():
    print("\033c", end="")


import random

number = random.randint(1, 100)

while True:
    clear()
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        lives = 10
    elif difficulty == "hard":
        lives = 5
    else:
        continue
    while lives > 0:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == number:
            print(f"You got it! The answer was {number}.")
            break
        elif guess > number:
            print("Too high.")
            lives -= 1
        else:
            print("Too low.")
            lives -= 1
    if lives == 0:
        print("You've run out of guesses, you lose.")
        print(f"The correct answer was {number}.")
    play_again = input("Do you want to play again? Type 'y' or 'n': ")
    if play_again == "n":
        print("Goodbye!")
        break
