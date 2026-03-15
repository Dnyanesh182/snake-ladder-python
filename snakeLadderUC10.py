import random

NO_PLAY = 0
LADDER = 1
SNAKE = 2

player1_position = 0
player2_position = 0

dice_roll_count = 0
current_player = 1

while player1_position < 100 and player2_position < 100:

    dice = random.randint(1,6)
    option = random.randint(0,2)

    dice_roll_count += 1

    if current_player == 1:

        if option == LADDER:
            if player1_position + dice <= 100:
                player1_position += dice

        elif option == SNAKE:
            player1_position -= dice
            if player1_position < 0:
                player1_position = 0

        print("Player 1 Position:", player1_position)

        current_player = 2

    else:

        if option == LADDER:
            if player2_position + dice <= 100:
                player2_position += dice

        elif option == SNAKE:
            player2_position -= dice
            if player2_position < 0:
                player2_position = 0

        print("Player 2 Position:", player2_position)

        current_player = 1


if player1_position == 100:
    print("Player 1 Wins!")
else:
    print("Player 2 Wins!")

print("Total Dice Rolls:", dice_roll_count)