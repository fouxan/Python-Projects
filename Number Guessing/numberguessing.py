import random
print("Number Guessing game:")

target=random.randint(1,100)
level=input("What level do you want to play? Easy(10 attempts)('e') or Hard(5 attempts)('h'): ")

if level=="e":
    print("10 guesses remaining.")
    user_input = int(input("Guess a number: "))
    print("9 guesses remaining.")
    lives=10
    while user_input != target and lives >= 1:
        if user_input < target:
            user_input = int(input("Guess higher: "))
        else:
            user_input = int(input("Guess lower: "))
        lives -= 1
        if lives==1:
            print(f"Game over. You ran out of lives, the number was {target}.")
            break
        if user_input==target: print(f"You got it. The number is {target}.")
        else: print(f"{lives-1} guesses remaining.")
else:
    print("5 guesses remaining.")
    user_input = int(input("Guess a number: "))
    print("4 guesses remaining.")
    lives = 5
    while user_input != target and lives > 1:
        if user_input < target:
            user_input = int(input("Guess higher: "))
        else:
            user_input = int(input("Guess lower: "))
        lives -= 1
        if lives == 1:
            print(f"Game over. You ran out of lives, the number was {target}.")
            break
        if user_input == target:
            print(f"You got it. The number is {target}.")
        else:
            print(f"{lives - 1} guesses remaining.")

