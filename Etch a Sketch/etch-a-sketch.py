from turtle import Turtle, Screen

t = Turtle()
s = Screen()


def move_forward():
    t.forward(10)


def move_backward():
    t.backward(10)


def move_leftward():
    t.left(10)


def move_rightward():
    t.right(10)


def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


s.listen()
s.onkey(move_forward, "w")
s.onkey(move_backward, "s")
s.onkey(move_leftward, "a")
s.onkey(move_rightward, "d")
s.onkey(clear, "c")
s.exitonclick()
