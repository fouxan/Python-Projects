with open("Input/Letters/starting_letter.txt") as letter:
    content = letter.read()

with open("Input/Names/invited_names.txt") as names:
    name = names.readlines()
    for n in name:
        new = n.strip()
        con = content.replace("[name]", new)
        with open(f"Output/ReadyToSend/letter_to_{n}.txt", "w") as final:
            final.write(con)




    
