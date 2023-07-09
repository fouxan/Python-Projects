import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
final = {row.letter: row.code for (index, row) in data.iterrows()}

word = input("Enter a word: ").upper()

result = [final[letter] for letter in word]
print(result)
