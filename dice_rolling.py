#Dice rolling
import random

print("Let's roll the dice!")

while True:
    dice_roll = [random.randint(1,6) for i in range (6)]
    randomer_number = random.choice(dice_roll)
    print("You rolled a {0}!".format(randomer_number))
    response = (input("Would you like to roll again?  Enter 'Yes' or 'No'\n"))
    if response == "Yes" or response == "yes" or response == "Y" or response == "y":
        print("Rolling again...")
        continue
    else:
        break


