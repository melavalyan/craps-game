import random


def roll_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    print(f"The sum of dice is {dice1} + {dice2} = {total}")
    return total


def play_game():
    roll = roll_dice()
    print("First roll:", roll)

    if roll in [7, 11]:
        print("You win!")
        return
    elif roll in [2, 3, 12]:
        print("Casino wins!")
        return
    else:
        goal = roll
        print("Now your goal number is", goal)

    while True:
        roll = roll_dice()
        print("Next roll:", roll)

        if roll == 7:
            print("You lose!")
            return
        elif roll == goal:
            print("You win!")
            return


play_game()
