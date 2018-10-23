import random

print("Can you guess my number?")
random_list = [random.randint(1,21) for i in range (21)]
randomer_number = random.choice(random_list)
#print(randomer_number)

while True:
    user_choice = (input("What is your guess?\n"))
    try:
        val = int(user_choice)
        if int(user_choice) > randomer_number:
            print("That's not right!  My number is smaller than {0}!".format(user_choice))
        elif int(user_choice) < randomer_number:
            print("That's not right!  My number is bigger than {0}!".format(user_choice))
        else:
            print("That's right!  You guessed my number {0}!".format(user_choice))
            break
    except ValueError:
        print("Please enter a integer for your guess!")
            
    
    
