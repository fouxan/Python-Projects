from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import string
import json
import pyperclip

LB_FONT = ("Inter", 15, "normal")
BTN_FONT = ("Inter", 10, "bold")
WHITE = "#DDE6ED"
GREENISH = "#9DB2BF"
DARKER = "#526D82"
DARKEST = "#27374D"
LETTERS = list(string.ascii_letters)
DIGITS = list(string.digits)
SYMBOLS = ['!', '@', '#', '$', '%', '^', '&', '*', '-', '_', '+', '(', ')']

# --------------------------------------------------------Functionality----------------------------------------------------------


def save_pw():
    web = website_entry.get().title()
    id = email_entry.get()
    pw = pw_entry.get()
    pwd = {
        web:{
            "id": id,
            "password": pw
        }
    }
    
    if len(web) == 0 or len(pw) == 0 or len(id) == 0:
        messagebox.askretrycancel(title="Empty Fields", message="Do not leave any fields empty")
    else:
        try:
            with open(file="passwords.json", mode="r") as pw_file:
                data = json.load(pw_file)
        except:
            with open(file="passwords.json", mode="w") as pw_file:
                json.dump(pwd, pw_file, indent=4)      
        else:     
            data.update(pwd)
            with open(file="passwords.json", mode="w") as pw_file:
                json.dump(data, pw_file, indent=4)
        finally:
            website_entry.delete(0, END)
            pw_entry.delete(0, END)


def generate_pw():
    pw_l = [choice(LETTERS) for _ in range(randint(8, 10))]
    pw_n = [choice(DIGITS) for _ in range(randint(2, 4))]
    pw_s = [choice(SYMBOLS) for _ in range(randint(2, 4))]

    pw_list = pw_l + pw_n + pw_s
    shuffle(pw_list)

    password = ''.join(pw_list)
    pw_entry.insert(0, password)
    pyperclip.copy(password)
    
    
def get_pw():
    ws = website_entry.get().title()
    try:
        with open("passwords.json", "r") as pw_file:
            data = json.load(pw_file)
    except:
        msg = "No password exists.\n"
    else:   
        msg = "No password exists.\n"
        if ws in data:
            details = data[ws]
            msg = f'ID: {details["id"]}\nPassword: {details["password"]}\n'
    finally:
        messagebox.showinfo(title=f"{ws}", message=msg)
#-----------------------------------------------------------UI Design-----------------------------------------------------------
window = Tk()
window.title("PaS$w0rd M@9agEr")
window.config(padx=40, pady=40, bg=GREENISH)

canvas = Canvas(height=200, width=200, bg=GREENISH, highlightthickness=0)
pw_img = PhotoImage(file="/home/fouxan/pwman-removebg-preview.png")
canvas.create_image(100, 100, image=pw_img)
canvas.grid(row=0, column=1, padx=30, pady=30)

# Labels:
website_label = Label(text="Website: ", font=LB_FONT, bg=GREENISH)
website_label.grid(row=1, column=0, padx=25, pady=20) 

email_label = Label(text="Email/UserID: ", font=LB_FONT, bg=GREENISH)
email_label.grid(row=2, column=0) 

pw_label = Label(text="Password:", font=LB_FONT, bg=GREENISH)
pw_label.grid(row=3, column=0, padx=25, pady=20)

# Entries:
website_entry = Entry(width=22)
website_entry.grid(row=1, column=1, padx=15, pady=20)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, padx=20, pady=20)
email_entry.insert(0, "fouzanfouzan1310@gmail.com")

pw_entry = Entry(width=22)
pw_entry.grid(row=3, column=1, padx=15, pady=20)

#Buttons:
gen = Button(text="Generate", highlightthickness=0, font=BTN_FONT, bg=DARKER, activebackground=WHITE, 
             activeforeground=DARKEST, fg=WHITE, command=generate_pw)
gen.grid(row=3, column=2, padx=15, pady=20)

save = Button(text="Save", highlightthickness=0, width=20, font=BTN_FONT, bg=DARKER,
              activebackground=WHITE, activeforeground=DARKEST, fg=WHITE, command=save_pw)
save.grid(row=4, column=1, pady=20)
                  
srch = Button(text="Search", highlightthickness=0, font=BTN_FONT, bg=DARKER, activebackground=WHITE, 
             activeforeground=DARKEST, fg=WHITE, command=get_pw)
srch.grid(row=1, column=2, padx=15, pady=20)

window.mainloop()