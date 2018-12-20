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
    card = deck[random.randint(0, 51)] #picks a random number from 0 to 51 and finds that index location and pulls the value (card) at that location
    return card #returns the card string "KH" for use later

def deal(numhands, num_cards, deck=deck): #this is dealing the number of hands, number of cards, and whichever deck you want to use
    #this only will deal with up to 10 players
    current_hands_index = 0 #this is to keep track of how many hands we have made, so we can count to numhands
    hands=[]
    pulled_cards = []
    if (numhands * num_cards) > 52: #if we have more hands than cards available, print out the following statement
        print("There aren't enough cards for that many people.  Please choose fewer players.")
    else:
        while current_hands_index < numhands: #this checks to see if we have made the number of hands requested
            current_hands_index = current_hands_index + 1 #we add one to the current_hand_index since we are making a new hand
            working_hand = [] #resetting our working_hand to empty
            while int(len(working_hand)) < num_cards: #drawing cards, so long as the number of cards in working_hand is less than num_cards that should be in a hand
                card = pull_random_card(deck) #pulling random cards from the deck
                if card not in pulled_cards: #checking if the card has already been pulled
                    working_hand.append(card) #add the card to our working hand
                    pulled_cards.append(card) #add the card to our pulled_card list, so we can't pull the exact card a second time

            hands.append(working_hand) #add the working hand to the hands list and return that at the end
        print (hands)
        return hands






deal(2, 5, deck)
