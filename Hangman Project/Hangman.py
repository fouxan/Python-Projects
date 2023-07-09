import random
import resourcesforhangman
print(resourcesforhangman.logo)
randWord=random.choice(resourcesforhangman.words)
guess_string=[]
guess_made=[]
hasWon=False
lives=6

for n in randWord:
    guess_string.append("_")

print(f"{' '.join(guess_string)}")

def fill_blanks(letter):
    for n in range(0,len(randWord)):
        if randWord[n]==letter:
            guess_string[n]=letter
    return guess_string

while not hasWon:
    if "_" in guess_string:
        char=input("Enter a letter: ").lower()
        if char not in randWord:
            lives -= 1
            print(f"{char} is not in the word")
            if lives == 0:
                hasWon = True
                print(f"You lose. The word was {randWord}")
        print(f"You have {lives} lives left.")
        if char in guess_made:
            print("You already guessed this letter")
        else:
            guess_made += char
        print(f"Guesses made: {' '.join(guess_made)}")
        print(resourcesforhangman.stages[lives])
        print(f"{' '.join(fill_blanks(char))}")
    else:
        hasWon = True
        print("You won!")







