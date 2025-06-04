import random

def guess(x):
    """
    allows the user to guess a random number between 1 and x in a single round.

    args:
        x: the upper bound for the random number (the range is 1 to x).
    """
    random_number = random.randint(1, x) # computer picks a random number
    guess = 0 # initial value to enter the outer loop

    # main game loop: continues until the user guesses the number correctly
    while guess != random_number:
        # inner loop: handles getting and validating user input (integer within the range)
        while True:
            try:
                # prompt user for input within the defined range
                guess = int(input(f"guess a number between 1 and {x}: "))
                # check if the input is within the valid range (1 to x)
                if 1 <= guess <= x:
                    # if input is valid (integer within range), break the inner loop
                    break
                else:
                    # if input is outside the range, no explicit message, just loop again
                    pass # continue the inner loop implicitly

            except ValueError:
                # handle non-numeric input, no explicit message, just loop again
                pass # continue the inner loop implicitly

        # after inner loop, 'guess' is guaranteed to be a valid integer within the range

        # perform the too high/low check for the valid guess
        if guess < random_number:
            print("sorry, guess again. too low.")
        elif guess > random_number:
            print("sorry, guess again. too high.")
        # if guess == random_number, the outer while loop condition will be false, and the loop will terminate.

    # win message when the outer loop condition (guess != random_number) becomes false
    print(f"yay, congrats. you have guessed the number {random_number} correctly🎉")


# --- main function to run multiple rounds of the user guessing game ---
def main_user_guessing_game():
    """
    runs multiple rounds of the user guessing game until the user chooses to stop.
    """
    # initialize the variable to control playing again
    play_again = 'y'
    # define the upper bound for the number range
    upper_bound = 1000 # you can change this number if you want a different range

    # loop to run the game multiple times as long as play_again is 'y'
    while play_again == 'y':
        # call the guess() function to play a single round
        guess(upper_bound)

        # after a round is finished, ask the user if they want to play again
        # use an inner loop to validate the 'play again' input
        while True:
            play_again_input = input("\ndo you want to play again? (y/n): ").lower() # get yes/no input and convert to lowercase
            # validate if the input is 'y' or 'n'
            if play_again_input in ['y', 'n']:
                # if valid, update the control variable for the main loop
                play_again = play_again_input
                # exit the 'play again' input validation loop
                break
            else:
                # error message if 'play again' input is invalid
                print("invalid input. please enter 'y' or 'n'.")

    # message displayed when the main loop ends (user entered 'n')
    print("\nthanks for playing the user guessing game!")


# --- starting the entire program ---
# this is the only line outside of function definitions that runs initially.
# uncomment the game you want to play:
print("welcome to the user guesses the number game! 😁") # initial welcome message for this game
main_user_guessing_game() # start the main game loop for the user guessing game
