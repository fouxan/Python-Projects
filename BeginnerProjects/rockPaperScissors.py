import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
num=random.randint(0,2)
while True:
    user = input("Enter 0 for rock, 1 for paper, 2 for scissors or -1 to quit: ")
    if num==0:
        if int(user)==0:
            print(f"The computer chose:\n{rock}\nYou chose:\n{rock}\nIt's a draw.")
        elif int(user)==1:
            print(f"The computer chose:\n{rock}\nYou chose:\n{paper}\nYou win.")
        elif int(user) == 2:
            print(f"The computer chose:\n{rock}\nYou chose:\n{scissors}\nYou lose.")
        else: break
    elif num==1:
        if int(user)==0:
            print(f"The computer chose:\n{paper}\nYou chose:\n{rock}\nYou lose.")
        elif int(user)==1:
            print(f"The computer chose:\n{paper}\nYou chose:\n{paper}\nIt's a draw.")
        elif int(user)==2:
            print(f"The computer chose:\n{paper}\nYou chose:\n{scissors}\nYou win.")
        else:
            break
    else:
        if int(user)==0:
            print(f"The computer chose:\n{scissors}\nYou chose:\n{rock}\nYou win.")
        elif int(user)==1:
            print(f"The computer chose:\n{scissors}\nYou chose:\n{paper}\nYou lose.")
        elif int(user) == 2:
            print(f"The computer chose:\n{scissors}\nYou chose:\n{scissors}\nIt's a draw.")
        else:
            break