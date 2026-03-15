import random

NO_PLAY = 0
LADDER = 1
SNAKE = 2

player_position = 0

while player_position < 100:

    dice = random.randint(1,6)
    option = random.randint(0,2)

    if option == LADDER:
        if player_position + dice <= 100:
            player_position += dice
        print("Ladder! Move Forward")

    elif option == SNAKE:
        player_position -= dice
        if player_position < 0:
            player_position = 0
        print("Snake! Move Backward")

    else:
        print("No Play")

    print("Dice:", dice)
    print("Player Position:", player_position)

print("Player reached position 100. Game Won!")