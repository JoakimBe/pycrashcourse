##########################################################################################################
#
# Guessing Game
# Level: Hard
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
# - (H) Sanitize user input to only allow numbers. Exception handling or regex are two valid options.
# - (H) Create an informative row that includes player statistics( separate function ).
#       Code must be in a separate function.
#       * Total number of times played
#       * Total number of failed guesses
#       * Total number of correct guesses
#
# - (H) Make the player data persistent by saving to a local file.
#       Try to load the old statistics each time the game is started.
#       If no old statistics exist, load default values.
#
#
##########################################################################################################

import random
import os
import json

runProcess = True


# We try to open the file game_data.json. If the files does not exist, not old game data
# is available and we return the default values which is {'total': 0, 'correct': 0, 'failed': 0}.
def load_player_statistics():

    if os.path.exists('game_data.json'):

        with open('game_data.json') as data_file:
            data = json.load(data_file)

        return data

    else:
        return {'total': 0, 'correct': 0, 'failed': 0}


# A cross-platform clear terminal function
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


# Write player statistics to game_data.json.
def save_player_statistics(json_data):
    with open('game_data.json', 'w') as outfile:
        json.dump(json_data, outfile, sort_keys=True, indent=4, ensure_ascii=False)


# If the user enters the number 100, set the return False to exit the game.
def exit_process(user_input):
    if user_input == 100:
        print("\nExiting game, Thanks for playing!")
        return False
    else:
        return True

# Load old game data. If no old data exists, load default.
gameData = load_player_statistics()


# Display game info and statistics
def show_info(game_data):
    statistics = """---------------------------------------
| Total: {total} | Correct: {correct} | Failed: {failed} |
---------------------------------------"""

    print(statistics.format(total=game_data['total'], correct=game_data['correct'], failed=game_data['failed']))
    print("\nGuess a number between 1 and 10.\nWrite '100' to exit the game.\n\n")


# Clear terminal once before the game starts
clear_terminal()

# Display game info and statistics once before the game starts
show_info(gameData)

# Run the game as long as runProcess equals True
while runProcess:

    # Randomize a number between 1 and 10 and return that number to the randomNumber variable.
    randomNumber = random.randint(1, 10)

    # Exception handling is used to "try" to convert the user input to a number.
    try:

        # Ask the user to enter a number
        userInput = int(input("Enter a number:"))

        # Run the exit_process function with the userInput and the input-parameter.
        # We need to check if the user wants to exit the game by entering 100.
        runProcess = exit_process(userInput)

        # If the runProcess is True we will continue the game.
        if runProcess:

            # Increase the total number of attempts by one each time the use tries to guess a new number.
            gameData['total'] += 1

            # Check if the user guessed the correct number
            if randomNumber == userInput:

                # Increase the total number of correct answers by one.
                gameData['correct'] += 1
                message = "Correct! You guessed {guessedNumber} and the number is {randomNumber}\n"

            else:

                # Increase the total number of failed answers by one.
                gameData['failed'] += 1
                message = "Fail! You guessed {guessedNumber} but the number is {randomNumber}\n"

            # Clear the terminal, show new info/stats and save stats after each guess.
            clear_terminal()
            show_info(gameData)
            save_player_statistics(gameData)
            print(message.format(randomNumber=randomNumber, guessedNumber=userInput))

    # If the user enters something else then a number the "try" will fail and cast a ValueError exception.
    # In this case we print an error to the user and let the game continue.
    except ValueError:
        print("Invalid input. Only numbers is allowed! Please try again.\n")
        pass



