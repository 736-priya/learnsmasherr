import random

def roll_dice():
    dice1 = random.randint (1,6)
    dice2 = random.randint (1,6)
    return dice1,dice2

dice1_result,dice2_result = roll_dice()
print("Dice 1:", dice1_result)
print("Dice 2:", dice2_result)
print(":Dotal", dice1_result+dice2_result)

    
