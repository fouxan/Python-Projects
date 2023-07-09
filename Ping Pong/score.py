from turtle import Turtle
POS = {"left": (-250, 360), "right": (250, 360)}
FONT = ("Minecrafter", 30, "normal")
FONT1 = ("Minecrafter", 20, "normal")


class Score(Turtle):
    def __init__(self, side):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(POS[side])
        self.write(f"{self.score}", align="center", font=FONT)

    def increment(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}", align="center", font=FONT)

    def game_end(self, side):
        self.color("gold")
        self.hideturtle()
        self.goto(POS[side][0]/2)
        self.write("You win.", align="center", font=FONT1)
