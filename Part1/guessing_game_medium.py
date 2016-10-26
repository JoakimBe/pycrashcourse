##########################################################################################################
#
# Guessing Game
# Level: Medium
#
# Requirements.
#
# - (E) The game will randomize a number between 1 and 10, and then let the player guess the random number.
# - (E) Gather an input from the player. The input will be the guessed number or quit command to end the game.
# - (E) Use a conditional statement to check if the guessed number equals the current random number.
# - (E) The game should randomize a new number everytime the user guesses.
# - (E) Print information to the player if the guess is right or wrong.
#
# - (M) Main game must run within a conditional loop ( while ) that runs in definite
# - (M) Must contain a way to exit the game ( end while loop ).
#       Use a higher number then the random range as an exit integer.
#
# - (M) The code that let's the user exit the game must be in a separate function.
#
#
##########################################################################################################

import random

runProcess = True


# If the user enters the number 100, set the return False to exit the game.
def exit_process(user_input):
    if user_input == 100:
        print("\nExiting game, Thanks for playing!")
        return False
    else:
        return True

print("\nGuess a number between 1 and 10.\nWrite '100' to exit the game.\n\n")

# Run the game as long as runProcess equals True
while runProcess:

    # Randomize a number between 1 and 10 and return that number to the randomNumber variable.
    randomNumber = random.randint(1, 10)

    # Ask the user to enter a number
    userInput = int(input("Enter a number:"))

    # Run the exit_process function with the userInput and the input-parameter.
    # We need to check if the user wants to exit the game by entering 100.
    runProcess = exit_process(userInput)

    # If the runProcess is True we will continue the game.
    if runProcess:

        # Check if the user guessed the correct number
        if randomNumber == userInput:
            message = "Correct! You guessed {guessedNumber} and the number is {randomNumber}\n"
        else:
            message = "Fail! You guessed {guessedNumber} but the number is {randomNumber}\n"

        print(message.format(randomNumber=randomNumber, guessedNumber=userInput))



