# this is the "game.py" file
from random import random

import os 
player_name = os.getenv("PLAYER_NAME", default="Player One")
    
print("-------------------")

print(f"Welcome {player_name} to the game - Rock, Paper, Scissors, Shoot!")

print("-------------------")

# Ask for User Input 

user_choice = input("Please choose either 'rock', 'paper', or 'scissors': ")

print("You chose:", user_choice)


# Validations
answer_list = ["rock", "paper", "scissors"]
user_choice = user_choice.lower()
if user_choice not in answer_list:
    print("invalid entry, please try again")
    quit()

    
# Computer Choice
# https://docs.python.org/3/library/random.html
# https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/modules/random.m

computer_responses = ["rock", "paper", "scissors"]
import random
computer_choice = random.choice(computer_responses)
print("Computer chose:", computer_choice )

print("-------------------")

# Determine the Winner
# Winner determination by using a nested if statement
if user_choice == computer_choice: 
    print(f"Both players selected {user_choice}. Its a tie!")
elif user_choice == "rock":
    if computer_choice == "paper":
        print("Paper covers rock. Computer wins!")
    else: 
        print("Rock crushes scissors. User wins!")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("Paper covers rock. User wins!")
    else:
        print("Scissors cut paper. Computer wins!")
elif user_choice == "scissors":
    if computer_choice == "rock":
        print("Rock crushes scissors. Computer wins!")
    else:
        print("Scissors cut paper. User wins!")


# Final Message
print("Thank you for playing. Please play another round soon!")
