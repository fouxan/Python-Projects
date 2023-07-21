from tkinter import *

def show():
    my_label.config(text=input.get())
    my_label.pack(side = "top")


# This will be the main screen. To keep this screen running until we press close use .mainloop()
# See docs for Tcl and other attributes of the window.
window = Tk()
window.title("First window")
window.minsize(width=500, height=500) 
# the minsize initializes the window, if the components added take up more 
# space it will automatically expand to the required size but never shrinks to less than the specified size

# all components which are being additionally displayed need to be called with the .pack() method, side can be left, right, top, bottom
# Labels are text boxes which can only display
my_label = Label(font=("Arial", 20, "bold"))

# Buttons can be used to perform functionality, the command argument takes in just the name of the function to be called on a press
btn = Button(text="Click Me!", command = show)
btn.pack()

# Entry class can be used to take inputs from a dialog box 
input = Entry(width=15)
input.pack()

window.mainloop()