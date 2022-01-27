# this is the "game.py" file
from random import random


print("Welcome to the game - Rock, Paper, Scissors, Shoot!")

print("-------------------")

# Ask for User Input 
user_choice = input("rock, paper, or scissors? ")

print("Player has chosen:", user_choice)


# Validations
answer_list = ["rock", "paper", "scissors"]
user_choice = user_choice.lower()
if user_choice not in answer_list:
    print("invalid entry, please try again") and quit()
    
# Computer Choice
computer_responses = ["rock", "paper", "scissors"]
import random
computer_choice = random.choice(computer_responses)
print("Computer has chosen:", computer_choice )


# Determine the Winner
if user_choice == answer_list[1] and computer_choice == answer_list[1]: 
    print("Rock vs Rock. The game is a tie!")
elif user_choice == answer_list[1] and computer_choice == answer_list[2]:
    print("Paper beats Rock. Computer wins!")
elif



# Final Results