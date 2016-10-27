##########################################################################################################
#
# Guessing Game
# Level: Easy
#
# Requirements.
#
# - The game will randomize a number between 1 and 10, and then let the player guess the random number.
# - Gather an input from the player. The input will be the guessed number or quit command to end the game.
# - Use a conditional statement to check if the guessed number equals the current random number.
# - The game should randomize a new number everytime the user guesses.
# - Print information to the player if the guess is right or wrong.
#
##########################################################################################################

import random

print("\nGuess a number between 1 and 10.\nWrite 'Quit' to exit the game.\n\n")

# Randomize a number between 1 and 10 and return that number to the randomNumber variable.
randomNumber = random.randint(1, 10)

# Ask the user to enter a number
userInput = input("Enter a number:")

# If the runProcess is True we will continue the game.
if randomNumber == int(userInput):
    message = "Correct! You guessed {guessedNumber} and the number is {randomNumber}\n"
else:
    message = "Fail! You guessed {guessedNumber} but the number is {randomNumber}\n"

print(message.format(randomNumber=randomNumber, guessedNumber=userInput))
