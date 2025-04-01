from turtle import Turtle, Screen
from turtle import *
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):

        self.segments = []
        self.create_a_snake()
        self.head = self.segments[0]

    def create_a_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def add_segment(self, position1):
        # creating a new turtle as our snake, the snake is made of three squares
            new_segment = Turtle("square")
            self.segments.append(new_segment)
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position1)

    def create_a_segment(self):
        self.add_segment(self.segments[-1].position())

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_a_snake()
        self.head = self.segments[0]


    # setting up event listeners to move in all four direction

    def north(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def east(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def west(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def south(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)



    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x_position = self.segments[seg_num - 1].xcor()
            y_position = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x_position, y_position)
        self.head.forward(20)







