from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.paddle_object = []
        self.shape("square")
        self.color("white")
        self.penup()
        self.left(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.speed("fastest")

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)
