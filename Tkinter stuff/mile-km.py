from tkinter import *
FONT = font=("Inter", 10, "normal")

def convert():
    m = miles.get()
    km_label.config(text=f"{1.609344 * float(m)} Kilometers")

window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=30, pady=30)

miles_label = Label()
miles_label.config(text="Miles: ", font=FONT)
miles_label.grid(row=0, column=1)

km_label = Label()
km_label.config(text="Kilometers: ", font=FONT) 
km_label.grid(row=1, column=1)

miles = Entry()
miles.config(width=10)
miles.grid(row = 0, column=2)

con = Button(text="Convert", command=convert)
con.grid(row=2, column=2)










window.mainloop()