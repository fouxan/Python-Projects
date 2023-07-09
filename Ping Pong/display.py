from turtle import Turtle
FONT = ("Minecrafter", 30, "normal")


class Display:
    def __init__(self):
        ping = Turtle()
        ping.penup()
        ping.hideturtle()
        ping.speed("fastest")
        ping.color("white")
        ping.goto(y=420, x=-100)
        ping.write("PING ", align="center", font=FONT)

        pong = Turtle()
        pong.penup()
        pong.hideturtle()
        pong.speed("fastest")
        pong.color("white")
        pong.goto(y=420, x=100)
        pong.write("PONG ", align="center", font=FONT)

        line = Turtle()
        line.hideturtle()
        line.speed("fastest")
        line.color("white")
        line.penup()
        line.goto(-20, 500)
        line.right(90)
        line.pendown()
        line.pensize(20)
        line.forward(1000)
