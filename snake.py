from turtle import Turtle

MOVING_DISTANCE = 20

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(3):
            new_turtle = Turtle("square")
            new_turtle.penup()
            new_turtle.color("green")
            new_turtle.setx(-i * 20)
            self.segments.append(new_turtle)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("green")
        new_segment.setposition(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move(self):
        for segment_index in range(len(self.segments) - 1, 0, -1):
            self.segments[segment_index].goto(self.segments[segment_index - 1].position())
        self.segments[0].forward(MOVING_DISTANCE)
