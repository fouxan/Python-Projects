import random
import time
import os
import resources

play_again=True

def allot_cards(list,n):
    for i in range(n):
        list.append(random.choice(resources.names))

def hand_value(list):
    sum=0
    for card in list:
        sum+=resources.cards[card]
    if sum==21 and len(list)==2:
        return 21
    elif "Ace" in list and sum>21:
        return sum-10
    else:
        return sum

#Main
while play_again:
    dealer_cards = []
    user_cards = []
    game_over = False
    print(resources.logo)
    allot_cards(user_cards,2)
    allot_cards(dealer_cards, 2)

    while not game_over:
        print(f"Your cards are {', '.join(user_cards)}, and the sum is {hand_value(user_cards)}")
        print(f"My card is {dealer_cards[0]}")
        if hand_value(user_cards)>=21 or hand_value(dealer_cards)>=21:
            game_over=True
        else:
            choice = input("Do you want to 'Hit' or 'Stand'(Type 'h' or 's'): ")
            if choice == 'h':
                 allot_cards(user_cards,1)
            else:
                game_over=True

    while hand_value(dealer_cards) < 17:
        allot_cards(dealer_cards,1)

    print(f"Your final cards are {', '.join(user_cards)}, with a value of {hand_value(user_cards)}")
    print(f"My final cards are {', '.join(dealer_cards)}, with a value of {hand_value(dealer_cards)}")
    us=hand_value(user_cards)
    ds=hand_value(dealer_cards)

    if us==ds: print("It's a Draw.")
    elif ds==21: print("I have Black Jack, You lose.")
    elif us==21: print("You have Black Jack, You win.")
    elif us>21: print("BUST, You lose. I win.")
    elif ds>21: print("BUST, You win.")
    elif us>ds: print("You win.")
    else: print("You lose. I win.")

    play_again=True if input("Do you want to play again? ('y' or 'n'): ")=="y" else False
    os.system('cls')
print("Fun playing with you, Bye.")
time.sleep(3)
















