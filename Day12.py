import random
import os

logo = """ $$$$$$\                                          $$\                                                                       
$$  __$$\                                         \__|                                                                      
$$ /  \__|$$\   $$\  $$$$$$\   $$$$$$$\  $$$$$$$\ $$\ $$$$$$$\   $$$$$$\         $$$$$$\   $$$$$$\  $$$$$$\$$$$\   $$$$$$\  
$$ |$$$$\ $$ |  $$ |$$  __$$\ $$  _____|$$  _____|$$ |$$  __$$\ $$  __$$\       $$  __$$\  \____$$\ $$  _$$  _$$\ $$  __$$\ 
$$ |\_$$ |$$ |  $$ |$$$$$$$$ |\$$$$$$\  \$$$$$$\  $$ |$$ |  $$ |$$ /  $$ |      $$ /  $$ | $$$$$$$ |$$ / $$ / $$ |$$$$$$$$ |
$$ |  $$ |$$ |  $$ |$$   ____| \____$$\  \____$$\ $$ |$$ |  $$ |$$ |  $$ |      $$ |  $$ |$$  __$$ |$$ | $$ | $$ |$$   ____|
\$$$$$$  |\$$$$$$  |\$$$$$$$\ $$$$$$$  |$$$$$$$  |$$ |$$ |  $$ |\$$$$$$$ |      \$$$$$$$ |\$$$$$$$ |$$ | $$ | $$ |\$$$$$$$\ 
 \______/  \______/  \_______|\_______/ \_______/ \__|\__|  \__| \____$$ |       \____$$ | \_______|\__| \__| \__| \_______|
                                                                $$\   $$ |      $$\   $$ |                                  
                                                                \$$$$$$  |      \$$$$$$  |                                  
                                                                 \______/        \______/                                   """
def rules(number, guess):
    if guess == number:
        print(f"You got it! The answer was {number}.")
    elif guess < number:
        print("Too low.")
    else:
        print("Too high")

def stillPlaying():
    play = input("Do you want to play the guessing game? Type 'y' or 'n': ").lower()
    if play == 'y':
        os.system('cls')
        guessingGame()

def guessingGame():
    print(logo)
    number = random.randint(1, 100)

    print("I'm thinking of a number between 1 and 100")

    difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    values = {"easy": 10, "hard": 5}

    for i in range(values[difficulty_level]):
        print(f"You have {values[difficulty_level]} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        rules(number, guess)
        if guess == number:
            stillPlaying()
            break
        values[difficulty_level] = values[difficulty_level] - 1
        if values[difficulty_level] == 0:
            print("You've run out of guesses, you lose.")
            stillPlaying()
        else:
            print("Guess again.")
        


stillPlaying()


