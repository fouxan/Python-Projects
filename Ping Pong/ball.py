from turtle import Turtle
from random import randint


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.setheading(randint(20, 40))

    def move(self):
        self.forward(7)

    def refresh(self, mode):
        self.goto(0, 0)
        self.setheading(mode*randint(27, 45))

    def bounce_y(self):
        self.setheading(360 - self.heading())

    def bounce_x(self):
        self.setheading(180 - self.heading())
