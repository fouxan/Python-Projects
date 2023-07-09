import time
from turtle import Screen
from display import Display
from paddle import Paddle
from score import Score
from ball import Ball

game_on = True


def game():
    global game_on
    game_on = True


screen = Screen()
screen.setup(height=1000, width=1000)
screen.bgcolor("black")
screen.tracer(0)


display = Display()
pl = Paddle("left")
pr = Paddle("right")
sl = Score("left")
sr = Score("right")
ball = Ball()

screen.listen()
screen.onkey(pl.up, "Up")
screen.onkey(pl.down, "Down")
screen.onkey(pr.up, "w")
screen.onkey(pr.down, "s")
screen.onkey(game, "space")

while game_on:
    screen.update()
    time.sleep(0.02)
    ball.move()
    ply = pl.ycor()
    pry = pr.ycor()

    if ball.ycor() >= 450 or ball.ycor() <= -450:
        ball.bounce_y()

    if ball.xcor() <= -430:
        if ball.distance(pl) < 50:
            ball.bounce_x()
        else:
            sr.increment()
            ball.refresh(5)

    if ball.xcor() >= 430:
        if ball.distance(pr) < 60:
            ball.bounce_x()
        else:
            sl.increment()
            ball.refresh(1)

    if sl.score == 10:
        sl.game_end("left")
        break
    elif sr.score == 10:
        sr.game_end("right")
        break


screen.exitonclick()
