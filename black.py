import random
import time


#card_face = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King'] unused for now

player_money = 100
player_bet = 0
current_money = player_money - player_bet 



game_select = str(input("Hello and welcome to Blackjack. Would you like to be a player or a dealer?  "))
while True: #while loop to restart game on loss


    #setup game with money
    dealer_cards = []
    player_cards = []
    
    if game_select == "player":
    
        while True:
            try:

                player_bet = int(input("Your current money is $ {}".format(current_money)+ " How much would you like to bet? "))
        
                if player_bet > current_money:
                    print("Insufficient money")
                    continue
                elif current_money == 0:
                    print("You are out of money. Time to go home")
                    exit()

            except ValueError:
                print("Not a number")
            else:
                current_money = current_money - player_bet 
                print("Your bet is $", player_bet )
                print("Your new total $",current_money)
                break

    elif game_select == ("dealer"):
        print("Dont be silly.\n***************")
        break
     #       dealer_game = input("Hi Mr. Dealer! You have a player ready! Press 1 to deal cards")
      #      if dealer_game == ('1'):
       #          while len(dealer_cards) != 2:
        #            dealer_cards.append(random.randint(1,11))
         #           if len(dealer_cards) == 2:
          #              print("You have:", dealer_cards)

          
        

    # deal cards 
    #dealer cards
    while len(dealer_cards) != 2:
        dealer_cards.append(random.randint(1,11))
        if len(dealer_cards) == 2:
            print("Dealer has X and", dealer_cards[1]) #take index 1, to hide the first card

            if sum(dealer_cards) > 21:
                print("Dealer busted. You win!")
                break

     #   elif len(dealer_cards) >1:
      #      dealer_cards = []
       #     dealer_cards.append(random.randint(1,11))
        #    print("The dealer has a total of " + str(sum(dealer_cards)) + " with ", dealer_cards)
         #   break
            


    #player cards
    while len(player_cards) != 2:
        player_cards.append(random.randint(1,11))

        if len(player_cards) == 2:
           # print("Your cards are: ", player_cards) 
            if(player_cards[0] == player_cards[1]):
                 player_split = str(input("You have 2 identical cards. Would you like to split them?"))
                 if(player_split == "yes"):
                     print("split worked")
                 else:
                    continue

        
        elif len(player_cards) >2:
            player_cards = []
            player_cards.append(random.randint(1,11)) 
            player_cards.append(random.randint(1,11)) 
          #  print("You now have a total of " +str(sum(player_cards)) + " from these cards ", player_cards)
            break



    #sum the dealer cards
    while sum(dealer_cards) <= 16:
        dealer_cards.append(random.randint(1,11)) # if the card total is 16 points or lower, the dealer will always draw another card from the deck.  


        


    #sum the player cards
    while sum(player_cards) < 21:
        print("You have a total of " +str(sum(player_cards)) + " from these cards ", player_cards)
        action_taken = str(input("Do you want to stay or hit?  " ))
    
        
        if action_taken == "hit":
            player_cards.append(random.randint(1,11))
         #   print("You now have a total of " +str(sum(player_cards)) + " from these cards ", player_cards)
            
        else:
            time.sleep(1)
            print("You have a total of " +str(sum(player_cards)) + " with ", player_cards)
            time.sleep(2)
            print("The dealer has a total of " + str(sum(dealer_cards)) + " with ", dealer_cards)
            time.sleep(2)
            


            if sum(dealer_cards) > sum(player_cards) and sum(dealer_cards) <22:
                print("Dealer wins")
                break
            elif sum(player_cards) > sum(dealer_cards) and sum (player_cards) <22:
                print("You win $", player_bet*2)
                current_money = player_bet*2 + current_money
                break
                

            elif sum(dealer_cards) == sum(player_cards):
                print("You have equal amount. Dealer wins!")
                break

            elif sum(dealer_cards) >21:
                print("Congratulations! You win ", player_bet*2)
                current_money = player_bet*2 + current_money
                break
                



    if sum(player_cards) > 21:
      #  print("The dealer has a total of " + str(sum(dealer_cards)) + " with ", dealer_cards)
        print("You have a total of " +str(sum(player_cards)) + " with ", player_cards)
        print("You busted! Dealer wins") #possibly find better way to deal with all these checks..
        





    elif sum(player_cards) == 21:
        print("The dealer has a total of " + str(sum(dealer_cards)) + " with ", dealer_cards)
        print("You have a total of " +str(sum(player_cards)) + " with ", player_cards)
        print("You have blackjack! You win! ", player_bet*3)
        current_money = player_bet*3 + current_money #triple money from winning with blackjack

    elif sum(dealer_cards) == 21:
        print("Dealer has 21. House wins")
        

    def player_win():
        sum(dealer_cards) >21 #unused for now
        

    print("***************")
    print("You now have $",current_money)
    restart = input("GO AGANE? Y/N ")
    if restart == 'n':
        print("You left with $",current_money)
        exit()
    elif restart == 'y':
        continue
