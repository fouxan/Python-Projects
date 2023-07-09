from turtle import Turtle, Screen
from random import randint

s = Screen()
race = False
s.setup(height=500, width=500)
user_input = s.textinput("Turtle Race", "Which turtle do you think will win:(enter a color)")
if user_input:
    race = True
colors = ["red", "blue", "orange", "black", "purple"]
turtles = []

for i in range(0, 5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.setposition(x=-230, y=-200+(i*100))
    turtles.append(new_turtle)

while race:
    for t in turtles:
        if t.xcor() >= 210:
            race = False
            if t.pencolor() == user_input:
                print("You win.")
            else:
                print("You lose.")
        t.forward(randint(10, 20))


s.exitonclick()
