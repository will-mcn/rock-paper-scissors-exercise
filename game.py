# this is the "game.py" file
from random import random


print("Welcome to the game - Rock, Paper, Scissors, Shoot!")

print("-------------------")

# Ask for User Input 
user_choice = input("Please choose either 'rock', 'paper', or 'scissors': ")

print("Player has chosen:", user_choice)


# Validations
answer_list = ["rock", "paper", "scissors"]
user_choice = user_choice.lower()
if user_choice not in answer_list:
    print("invalid entry, please try again")
    quit()

print("-------------------")
    
# Computer Choice
computer_responses = ["rock", "paper", "scissors"]
import random
computer_choice = random.choice(computer_responses)
print("Computer has chosen:", computer_choice )

print("-------------------")

# Determine the Winner
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
print("Thanks for playing. Please play again!")





# Final Results