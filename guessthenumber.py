
import random
import os

# Function to clear the console screen depending on the operating system
def clear_console():
    # If the OS is Windows, use 'cls' to clear the console
    if os.name == "nt": 
        _ = os.system('cls')
    # For Unix-based systems (like macOS or Linux), use 'clear'
    else: 
        _ = os.system('clear')


# Main function to start the "Guess the Number" game
def start_game():

    # Randomly generate a number between 1 and 100 for the player to guess
    system_guess = random.randint(1, 100)
    # Uncomment this line to print the number for testing/debugging purposes
    # print(system_guess)

    # Initial game instructions for the player
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Variable to track whether the game is still running
    game_status = True

    # Function to determine the number of attempts based on user-selected difficulty level
    def get_attempts(user_difficulty_level):
        # Easy difficulty gives the player 10 attempts
        if user_difficulty_level == "easy":
            return 10
        # Hard difficulty gives the player 5 attempts
        elif user_difficulty_level == "hard":
            return 5
        # Default to 5 attempts if an invalid difficulty is provided
        else:
            return 5
        
    # Function to check if the player wants to continue the game or quit
    def check_play_again(status):
        # If the player chooses 'y' (yes), restart the game by clearing the console and calling the main function again
        if status == "y":
            clear_console()
            start_game()
        # If the player chooses 'n' (no), print a goodbye message and exit the game
        else:
            print("Okay, see you some other time.")
    
    # Ask the player to choose a difficulty level
    difficulty_level = input("Choose a difficulty level. Type 'easy' or 'hard': ")

    # Get the number of attempts based on the chosen difficulty level
    number_of_attempts = get_attempts(difficulty_level)

    # Main game loop that continues until the game is over
    while game_status:
        # Check if the player still has attempts left
        if number_of_attempts > 0:
            # Inform the player how many attempts they have remaining
            print(f"You have {number_of_attempts} attempts remaining to guess the number.")
            # Get the player's guess as an integer
            user_guess = int(input("Make a guess: "))
            
            # Check if the player's guess is correct
            if user_guess == system_guess:
                # If correct, set the game status to False to end the loop and congratulate the player
                game_status = False
                print(f"You won! The number is indeed {system_guess}.")
                
                # Ask if the player wants to play again
                play_again = input("Do you want to play again? Type y for yes or n for no. ")
                
                # Call the function to determine if the game should continue
                check_play_again(play_again)

            # If the guess is incorrect, decrement the number of attempts and give feedback
            else:
                number_of_attempts -= 1
                # Let the player know if their guess was too high
                if user_guess > system_guess:
                    print("Guess is high.")
                # Let the player know if their guess was too low
                else:
                    print("Guess is low.")
        
        # If the player has run out of attempts, end the game
        else:
            game_status = False
            print("You've run out of guesses, you lose!")
            # Ask if the player wants to play again
            play_again = input("Do you want to play again? Type y for yes or n for no. ")
            
            # Call the function to determine if the game should continue
            check_play_again(play_again)
        

# Call the main function to start the game
start_game()
