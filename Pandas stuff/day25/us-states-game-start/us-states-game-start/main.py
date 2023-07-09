import turtle
import pandas as pd


def write(x, y, name):
    t = turtle.Turtle()
    t.penup()
    t.hideturtle()
    t.goto(x, y)
    t.write(name, align="center", )


image = "blank_states_img.gif"
screen = turtle.Screen()
screen.title("US States Quiz")
screen.setup(height=425, width=725)
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv").to_dict()
guessed_states = []
score = len(guessed_states)
flag = 0
index = 0

while True:
    guess = screen.textinput(f"{score}/50 Guessed!", "What is another State?").title()
    if guess in guessed_states:
        continue
    if guess == "Exit":
        break

    for s in data["state"]:
        if data["state"][s] == guess:
            flag = 1
            index = s
            guessed_states.append(guess)
            break
    if flag == 1:
        flag = 0
        score += 1
        write(data["x"][index], data["y"][index], data["state"][index])

    if score == 50:
        break
