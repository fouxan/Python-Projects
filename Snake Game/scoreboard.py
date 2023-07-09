from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hi_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=450)
        self.write(f"Score : {self.score}, High Score: {self.hi_score}", move=False, align="Center", font=('Courier', 20, 'bold'))

    def increment(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score}", move=False, align="Center", font=('Courier', 20, 'bold'))

    def end_game(self):
        self.color("red")
        self.hideturtle()
        self.goto(0, 0)
        self.write("GAME OVER", align='center', font=('Courier', 20, 'bold'))
