# -----------
# User Instructions
#
# Write a function, deal(numhands, n=5, deck), that
# deals numhands hands with n cards each.
#

import random # this will be a useful library for shuffling

# This builds a deck of 52 cards. If you are unfamiliar
# with this notation, check out Andy's supplemental video
# on list comprehensions (you can find the link in the
# Instructor Comments box below).

deck = [r+s for r in '23456789TJQKA' for s in 'SHDC']

def pull_random_card(deck):
    card = deck[random.randint(0, 51)]
    return card

def deal(numhands, num_cards, deck=deck):
    #this only will deal with up to 10 players
    current_hands_index = 0
    hands=[]
    pulled_cards = []
    if numhands > 10:
        print("There aren't enough cards for that many people.  Please choose fewer players.")
    else:
        while current_hands_index < numhands:
            current_hands_index = current_hands_index + 1
            working_hand = []
            while int(len(working_hand)) < num_cards:
                card = pull_random_card(deck)
                if card not in pulled_cards:
                    working_hand.append(card)
                    pulled_cards.append(card)

            hands.append(working_hand)
        print (hands)






deal(2, 5, deck)
