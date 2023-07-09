from turtle import Turtle

class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.level = 1
        for c in range(10, 10 + self.level * 10):
            new_car = Turtle()