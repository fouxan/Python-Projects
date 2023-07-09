from tkinter import *

# -----------------------CONSTANTS------------------------

bg_img = PhotoImage(file="pomo_back.jpg")


#-----------------------UI Design-------------------------

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg="#000000")

canvas = Canvas(height=600, width=600)
canvas.create_image(300, 300, image=bg_img)

canvas.grid()








window.mainloop()