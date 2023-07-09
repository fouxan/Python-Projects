import pandas as pd
from tkinter import *

BG = "#acd6c0"

# ---------------------------------------Functions----------------------------------------




# ----------------------------------------UI-----------------------------------------------

window = Tk()
window.title("French Flashy")
window.config(padx=30, pady=30, bg=BG)

card_front = PhotoImage(file="files/card_front.png")
card_back = PhotoImage(file="files/card_back.png")
right_img = PhotoImage(file="files/right.png")
wrong_img = PhotoImage(file="files/wrong.png")

# Card:
canvas = Canvas(width=800, height=526, highlightthickness=0)
canvas.create_image(400, 263, image=card_front)
canvas.grid(row=0, column=0, columnspan=2)


right = Button(width=100, height=100, image=right_img)
right.grid(row=1, column=1)

wrong = Button(width=100, height=100, image=wrong_img)
wrong.grid(row=1, column=0)

data = pd.read_csv("files/french_words.csv").to_dict()


window.mainloop()
