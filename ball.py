from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_pos = 0
        self.y_pos = 0

    def move(self):
        self.goto(self.x_pos, self.y_pos)
        self.x_pos += 10
        self.y_pos += 10
