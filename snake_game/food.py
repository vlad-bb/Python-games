from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('blue')
        self.speed(0)
        self.refresh()

    def refresh(self):
        cor_x = random.randint(-280,  280)
        cor_y = random.randint(-280, 280)
        return self.goto(cor_x, cor_y)
