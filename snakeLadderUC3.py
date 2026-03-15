import random

# Constants
NO_PLAY = 0
LADDER = 1
SNAKE = 2

# Initialize player position
player_position = 0

# Roll dice
dice = random.randint(1, 6)

# Determine game option
option = random.randint(0, 2)

if option == NO_PLAY:
    print("No Play")
elif option == LADDER:
    print("Ladder")
elif option == SNAKE:
    print("Snake")

print("Dice Rolled:", dice)