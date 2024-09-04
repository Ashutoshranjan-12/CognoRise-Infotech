import random

def get_user_choice():
    """
    Prompts the user to enter their choice and validates it.
    """
    choice = input("Enter your choice (rock, paper, scissors): ").lower()
    while choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please try again.")
        choice = input("Enter your choice (rock, paper, scissors): ").lower()
    return choice

def get_computer_choice():
    """
    Randomly selects the computer's choice from available options.
    """
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    """
    Determines the winner of the game based on user and computer choices.
    """
    if user_choice == computer_choice:
        return "It's a Tie😅"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You Win😊"
    else:
        return "You Lose😔"

def play_game():
    """
    Runs the game loop, allowing the user to play multiple rounds.
    """
    print("Welcome to Rock, Paper, Scissors! Let's play!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"User choice: {user_choice}")
        print(f"Computer choice: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

play_game()
