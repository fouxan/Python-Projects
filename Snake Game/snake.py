from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.speed = 20
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.tail = self.segments[-1]

    def create_snake(self):
        for s in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(s)
            self.segments.append(new_segment)

    def add_segment(self):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(self.tail.position())
        self.tail = new_segment
        self.segments.append(new_segment)

    def move(self):
        for s in range(len(self.segments)-1, 0, -1):
            self.segments[s].goto(self.segments[s-1].xcor(), self.segments[s-1].ycor())
        self.head.forward(self.speed)

    def up(self):
        if self.head.heading != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading != RIGHT:
            self.head.setheading(LEFT)
