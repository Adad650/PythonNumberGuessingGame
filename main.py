# Adi's program that will be a number guessing game
import random

userAttempts = 0
hasUserGuessedCorrectly = False
print("Enter name")
userName = input()
print("Hi " + userName + " good to see you. What is the lowest number to guess ?")

minGuess = int(input())

print("and your highest number to guess is: ?")
maxGuess = int(input())

print("Ok great lets start")

secretNmber = random.randrange(minGuess, maxGuess)



print("Guess the number please")
while hasUserGuessedCorrectly == False:
    userGuessNumber = int(input())
    userAttempts = userAttempts + 1
    if userGuessNumber == secretNmber:
        hasUserGuessedCorrectly = True
        break
    if userGuessNumber > secretNmber:
        print("Too high try again")
    if userGuessNumber < secretNmber:
        print("Too low try again")

print("Good job you did it you did it in " + str(userAttempts) + " attempts. Press ^R to play again. ")



