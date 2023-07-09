import turtle
import random

turtle.colormode(255)
t=turtle.Turtle()
t.shape("classic")
t.speed(0)


def draw_dashed_line(size,length):
    for n in range(length):
        t.fd(size)
        t.pu()
        t.fd(size)
        t.pd()


def draw_polygon(sides,length):
    t.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    angle_bw_sides=(sides-2)*180/sides
    for n in range(sides):
        t.fd(length)
        t.right(180 - angle_bw_sides)


def random_walk(size,length):
    t.pensize(10)
    for n in range(length):
        angle = random.randint(0,3)*90
        t.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        t.fd(size)
        t.right(angle)


def draw_spirograph(radius,amount):
    for n in range(amount):
        t.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        t.circle(radius)
        t.pu()
        t.right(360/amount)
        t.pd()


draw_spirograph(100,100)

screen = turtle.Screen()
screen.exitonclick()