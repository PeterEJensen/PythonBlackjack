import random

dealer_cards = []
card_face = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
player_cards = []
player_money = []


#setup game with money
action_taken = str(input("Hello and welcome to Blackjack. Would you like to be a player or a dealer?  "))
if action_taken == "player":
    pass
elif action_taken == "dealer":
    pass

# deal cards 
#dealer cards
while len(dealer_cards) != 2:
    dealer_cards.append(random.randint(1,11))
    if len(dealer_cards) == 2:
        print("Dealer has X and", dealer_cards[1]) #take index 1, to hide the first card


#player cards
while len(player_cards) != 2:
    player_cards.append(random.randint(1,11))
    if len(player_cards) == 2:
        print("Your cards are: ", player_cards) 


#sum the dealer cards
while sum(dealer_cards) < 16:
    dealer_cards.append(random.randint(1,11))
if sum(dealer_cards) == 21:
    print("Dealer has 21. House wins")
elif sum(dealer_cards) > 21:
    print("Dealer has busted")




#sum the player cards
while sum(player_cards) < 21:
    action_taken = str(input("Do you want to stay or hit?  " ))
    if action_taken == "hit":
        player_cards.append(random.randint(1,11))
        print("You now have a total of " +str(sum(player_cards)) + " from these cards ", player_cards)
    else:
        print("The dealer has a total of " + str(sum(dealer_cards)) + " with ", dealer_cards)
        print("You have a total of " +str(sum(player_cards)) + " with ", player_cards)
        if sum(dealer_cards) > sum(player_cards):
            print("Dealer wins")

        else:
            print("You win!")
            break
            


if sum(player_cards) > 21:
    print("You busted! Dealer wins")

elif sum(player_cards) == 21:
    print("You have blackjack! You win!")