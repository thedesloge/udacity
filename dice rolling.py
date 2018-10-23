#Dice rolling
import random

print("Let's roll the dice!")

dice_roll = [random.randint(1,6) for i in range (6)]
randomer_number = random.choice(dice_roll)
print("You rolled a {0}!".format(randomer_number))
#print(input"How many dice do you want to roll?")
