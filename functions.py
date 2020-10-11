import random
import math
import sys

def startGame():

    lower = 1
    upper = 0

    selectedDifficulty = input("Select a difficulty [easy, medium, hard]")

    if selectedDifficulty == "easy":
        upper = 5
    elif selectedDifficulty == "medium":
        upper = 15
    elif selectedDifficulty == "hard":
        upper = 30
    else:
        sys.exit("I couldn't understand that!")

    numberWithinRange = random.randint(lower,upper)
    userGuess = 0

    while (userGuess != numberWithinRange):
        print("You selected the", selectedDifficulty, "Guess a number between", lower, "and", upper)
        userGuess = int(input("Your guess is: ")) 
        if userGuess < numberWithinRange:
            print("Too Low")
        elif userGuess > numberWithinRange:
            print("Too High")
        elif userGuess == numberWithinRange:
            print("You got it right")
            break
        