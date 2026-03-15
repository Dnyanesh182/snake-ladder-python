import random

NO_PLAY = 0
LADDER = 1
SNAKE = 2

player_position = 0
dice_roll_count = 0

while player_position < 100:

    dice = random.randint(1,6)
    option = random.randint(0,2)

    dice_roll_count += 1

    if option == LADDER:
        if player_position + dice <= 100:
            player_position += dice
        print("Ladder")

    elif option == SNAKE:
        player_position -= dice
        if player_position < 0:
            player_position = 0
        print("Snake")

    else:
        print("No Play")

    print("Dice:", dice)
    print("Player Position:", player_position)

print("Player reached 100")
print("Total Dice Rolls:", dice_roll_count)