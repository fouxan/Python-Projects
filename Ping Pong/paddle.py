from turtle import Turtle
SP = {"left": (-450, 0),
      "right": (450, 0)}


class Paddle(Turtle):
    def __init__(self, side):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.setheading(90)
        self.goto(SP[side])

    def up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        self.goto(self.xcor(), self.ycor() - 20)
