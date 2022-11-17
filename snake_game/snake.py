from turtle import Turtle

MOVE_DISTANCE = 20
STARTING_POSITION = ((0, 0), (-20, 0), (-40, 0))


class Snake:
    def __init__(self):
        self.body_snake = []
        self.create_snake()
        self.head_snake = self.body_snake[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape='square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.body_snake.append(new_segment)

    def extend(self):
        self.add_segment(self.body_snake[-1].position())

    def move(self):
        for segment in range(len(self.body_snake) - 1, 0, -1):
            new_x = self.body_snake[segment - 1].xcor()
            new_y = self.body_snake[segment - 1].ycor()
            self.body_snake[segment].goto(x=new_x, y=new_y)
        self.body_snake[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head_snake.heading() != 270:
            self.head_snake.setheading(90)

    def down(self):
        if self.head_snake.heading() != 90:
            self.head_snake.setheading(270)

    def left(self):
        if self.head_snake.heading() != 0:
            self.head_snake.setheading(180)

    def right(self):
        if self.head_snake.heading() != 180:
            self.head_snake.setheading(0)
