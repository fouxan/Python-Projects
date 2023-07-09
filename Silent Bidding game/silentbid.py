import os
import time
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
bids={}
def take_input(user_name,user_bid):
    bids[user_name]=user_bid
another=True
highest_bid=0
highest_bidder=""
while another:
    take_input(input("What is your name? "),int(input("What is your bid? ")))
    another=True if input("Is there another bidder? ")=="yes" else False
    os.system('cls')

for key in bids:
    bid=bids[key]
    if bid>highest_bid:
        highest_bid=bid
        highest_bidder=key

print(f"The highest bidder was {highest_bidder} with a bid of ${highest_bid}")
time.sleep(5)