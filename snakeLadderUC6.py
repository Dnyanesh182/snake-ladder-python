import random

# Constants
NO_PLAY = 0
LADDER = 1
SNAKE = 2

player_position = 0

# Roll dice
dice = random.randint(1,6)

# Determine option
option = random.randint(0,2)

if option == LADDER:
    player_position += dice
    print("Ladder! Player moves forward.")

elif option == SNAKE:
    player_position -= dice
    if player_position < 0:
        player_position = 0
    print("Snake! Player moves backward.")

else:
    print("No Play.")

print("Dice Rolled:", dice)
print("Player Position:", player_position)