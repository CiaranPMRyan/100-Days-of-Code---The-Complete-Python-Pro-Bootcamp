import random


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


#cards = [11, 11, 11, 11, 10, 10, 10, 10]


# Function for dealing cards.
def deal(player):
   """Feeds in the list of each player and picks a random cards from the card list"""
   card_selection = random.choice(cards)
   player.append(card_selection)
   return player

# Function to print the current score
def print_score():
   print(f"    Your cards: {user_cards}, current score: {current_score}")
   print(f"    Computer's first card: {dealer_cards[0]}")

# Function to print the final score
def final_score():
    print(f"    Your final hand: {user_cards}, final score: {current_score}")
    print(f"    Computer's final hand: {dealer_cards}, final score: {dealer_score}")

# Function to print winning statement if player hits 21 exactly
def blackjack(user_hand, computer_hand):
    if user_hand == 21 and computer_hand == 21:
        print(final_score())
        print(f"    You both have Blackjack. The dealer wins")
    elif user_hand == 21:
        print(final_score())
        print(f"You have Blackjack. You win!")
    elif computer_hand == 21:
        print(final_score())
        print(f"Dealer has Blackjack. You lose!")


# Function for checking for an Ace and changing it to 1 if 11 brings the player over 21
def check_ace(current_hand):
   """Checks the hand that is over 21 if it has an ace. If so, it changes the 11 to a 1"""
   for card in range(len(current_hand)):
       if current_hand[card] == 11:
           current_hand[card] = 1
       else:
           current_hand = current_hand
   return current_hand


# Ask user to play

play_again = True

while play_again:
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

    # Loop for drawing new cards
    #draw = True

    # Create the empty lists to hold each players cards
    user_cards = []
    dealer_cards = []

    # Call the deal function and print out what is returned
    for i in range(0, 2):
        deal(user_cards)
    current_score = sum(user_cards)

    # Select 2 cards from the list but only display one for the computers cards
    for i in range(0, 2):
        deal(dealer_cards)
    dealer_score = sum(dealer_cards)

    print_score()

    # Check for Blackjack at the start

    blackjack(current_score, dealer_score)

    if current_score == 21 or dealer_score == 21:
        draw = False
    else:
        draw = True

    while draw:
        # Check for an ace
        check_ace(user_cards)

        # Ask if user wants another card
        choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()

        if choice == "y":
            deal(user_cards)
            current_score = sum(user_cards)
            if current_score == 21:
                blackjack(current_score, 0)
                draw = False
            elif current_score > 21:
                check_ace(user_cards)
                current_score = sum(user_cards)
                if current_score > 21:
                    final_score()
                    print(f"You went over. You lose!")
                    draw = False
                else: print_score()
            else:
                print_score()
                continue
        else:
            draw = False

    print("End")
   #
   #
   #     else:
   #         dealer_plays = True
   #         while dealer_plays:
   #             if dealer_score == 21:
   #                 blackjack(dealer_score)
   #                 dealer_plays = False
   #             elif dealer_score == current_score:
   #                 print("It's a tie!")
   #                 dealer_plays = False
   #             elif dealer_score <16:
   #                 print("PRINT 1")
   #                 score_check = True
   #                 while dealer_score < 16:
   #                     deal(dealer_cards)
   #                     if dealer_score > 16:
   #                         score_check = False
   #                         print(f"{dealer_cards}")
   #
   #
   #         print("Get the computer to get some cards and check against mine")
   #         draw = False
   #
   #
   # print("End")
   #
