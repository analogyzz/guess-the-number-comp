import random

def computer_guess(x):
    """
    allows the computer to guess a number chosen by the user between 1 and x.
    the computer uses a strategy to narrow down the possible range based on user feedback.

    args:
        x: the upper bound for the user's chosen number (the range is 1 to x).
    """
    low = 1 # lower bound for the computer's guess
    high = x # upper bound for the computer's guess
    feedback = '' # feedback from the user ('h', 'l', 'c' for high, low, correct)

    # main game loop: continues until the user says 'c' (correct)
    while feedback != 'c':
        # check if the guessing range is still valid (low is less than or equal to high)
        if low <= high : # check if the current range [low, high] is valid for guessing
            # computer makes a guess (attempting a binary search approach by picking randomly within the valid range)
            if low != high:
                # pick a random number within the current valid range
                guess = random.randint(low, high)
            else:
                # if low equals high, that's the only possible number left to guess
                guess = low # could also be high because low equals high

            # inner loop to get valid feedback from the user
            while True:
                # prompt user for feedback on the computer's guess
                feedback = input(f'is {guess} too high (h), too low (l), or correct (c)?').lower()
                # validate feedback: check if it's 'h', 'l', or 'c'
                if feedback in ['h', 'l', 'c']:
                    break # exit the validation loop if feedback is valid
                else:
                    # error message for invalid feedback
                    print("please input h / l / c.")

            # adjust the guessing range based on user feedback
            if feedback == 'h':
                # if the guess was too high, the correct number must be less than the current guess
                high = guess - 1
            elif feedback == 'l':
                # if the guess was too low, the correct number must be greater than the current guess
                low = guess + 1

            # check for condition of no whole numbers between low and high (indicates inconsistent user feedback)
            # this check is done after adjusting low/high based on the feedback
            if high == low - 1:
                print(f"there are no whole numbers between {low - 1} and {low}. please ensure your feedback is correct.")
                # the loop continues to the next iteration, but the invalid range might cause issues or require a way to break/reset

            # the commented out check below is logically redundant if high == low - 1 handles the direct consequence
            # if low > high after adjusting, it means the user gave contradictory feedback
            # elif low > high:
            # print(f"Please choose a number between 1 and {x}.")
            # # no break here either, so it will return to the beginning of the while loop


        else:
            # this condition is met if low > high before a guess is made (implies previous inconsistent feedback led to an invalid range)
            print(f"please choose a number between 1 and {x}.")
            # break the main loop because the range is no longer valid for guessing
            break # or you could also reset low and high if desired

    # win message
    # check if the loop ended because the user said 'c'
    if feedback == 'c':
        print(f'yeay! the computer guessed your number, {guess}, correctly!')
    # add an else block here if you want to handle the case where the loop broke due to inconsistent feedback


# --- main function to run multiple rounds of the computer guessing game ---
def main_computer_guessing_game():
    """
    runs multiple rounds of the computer guessing game until the user chooses to stop.
    """
    # initialize the variable to control playing again
    play_again = 'y'
    # define the upper bound for the number range
    upper_bound = 1000 # you can change this number if you want a different range

    # loop to run the game multiple times as long as play_again is 'y'
    while play_again == 'y':
        # call the computer_guess() function to play a single round
        computer_guess(upper_bound)

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
    print("\nthanks for playing the computer guessing game!")


# --- starting the entire program ---
# this is the only line outside of function definitions that runs initially.
# uncomment the game you want to play:
print("welcome to the computer guesses the number game! 😁") # initial welcome message for this game
main_computer_guessing_game() # start the main game loop for the computer guessing game