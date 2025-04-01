from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_wid=0.6, stretch_len=0.6)
        self.speed("fastest")
        self.refresh_position()



    def refresh_position(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 260)
        self.goto(x=random_x, y=random_y)