import random
import math

def startGame():
    lower = int(input("Insert lower digit:"))
    upper = int(input("insert upper digit:"))
    numberWithinRange = random.randint(lower,upper)
    userGuess = 0

    while (userGuess != numberWithinRange):
        userGuess = int(input("Your guess is: ")) 
        if userGuess < numberWithinRange:
            print("Too Low")
        elif userGuess > numberWithinRange:
            print("Too High")
        elif userGuess == numberWithinRange:
            print("You got it right")
            break
        