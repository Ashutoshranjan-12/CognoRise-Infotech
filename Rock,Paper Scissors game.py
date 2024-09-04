# ROCK, PAPER, SCISSORS GAME

import random

def get_user_choice():
    choice=input("Enter your choice (rock, paper, scissors): ").lower()
    while choice not in ["rock","Paper","scissors"]:
        print("Invalid choice! please Try again later")
        choice=input("Enter your choice (rock, paper, scissors): ").lower()
    return choice

def get_computer_choice():
    choices=["rock","paper","scissors"]
    return random.choice(choices)

def determine_winner(user_choice,computer_choice):
    if user_choice==computer_choice:
        return "It's a Tie😅"
    elif(user_choice=="rock" and computer_choice=="scissors")or \
        (user_choice=="scissors" and computer_choice=="paper")or \
        (user_choice=="paper" and computer_choice=="rock"):

        return "You Win😊"
    else:
        return "You loose😔"

def play_game():
    while True:
        user_choice=get_user_choice()
        computer_choice=get_computer_choice()
        print(f"User choice: {user_choice}")
        print(f"computer choice:{computer_choice}")

        result = determine_winner(user_choice,computer_choice)
        print(result)

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break
play_game()