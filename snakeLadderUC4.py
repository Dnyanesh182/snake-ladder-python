import random

# Constants
NO_PLAY = 0
LADDER = 1
SNAKE = 2

player_position = 0

# Roll dice
dice = random.randint(1,6)

# Game option
option = random.randint(0,2)

if option == LADDER:
    player_position += dice
    print("Ladder! Player moves forward.")

elif option == NO_PLAY:
    print("No Play. Player stays at same position.")

else:
    print("Snake encountered.")

print("Dice Rolled:", dice)
print("Player Position:", player_position)