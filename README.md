# rock-paper-scissors-exercise
RPS Exercise from OPIM 243

# Rock Paper Scissors Game

## Prerequisites
+ Anaconda 3.7+
+ Python 3.7+

## Setup & Virtual Environment
Clone and download the repository (https://github.com/will-mcn/rock-paper-scissors-exercise) onto your local computer.

On your terminal and the command line, navigate to the newly downloaded repository: 

```
cd ~/Desktop/rock-paper-scissors-exercise
```
Once in the repository, create and activate a project-specific virtual environment:
```
conda create -n RPS-game-env python=3.8
conda activate RPS-game-env
```

## Playing the Game

To start the game:

```
PLAYER_NAME="PLAYER_NAME" python game.py
```

This sequence passes an environment variable, PLAYER_NAME, so that you may customize your desired name throughout the program. If not customized as in the above, you will simply be 'Player One'. This also initiates the start of the game.

You will be prompted to select between 'rock', 'paper', or 'scissors' and type the input into the command line. Any capitalization or format of the words (i.e., rock, ROCK, Rock) will work as a valid input. Anything outside of these options will cause the game to quit, and the start sequence will need to be repeated. 

### Winner Determination

As a refresher, the following relationships dicate a win, loss, or tie in rock paper scissors: 
1. rock crushes scissors
2. scissors cuts paper
3. paper covers rock 
4. rock and rock, scissors and scissors, paper and paper all result in a tie

With the player's input, the computer will make a random corresponding selection and the outcome of the game (win, loss, or tie) will be displayed. 
