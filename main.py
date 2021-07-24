from turtle import Screen
from paddle import Paddle
from ball import Ball
import time


# Screen object definition
screen = Screen()
screen.bgcolor("Slateblue4")
screen.title("The Pong Game")
screen.setup(width=800, height=600)
screen.tracer(0)

# Paddle object definition
user1_paddle = Paddle()
user1_paddle.goto(-350, 0)

# Computer paddle object definition
user2_paddle = user1_paddle.clone()
user2_paddle.speed("slowest")
user2_paddle.goto(350, 0)

# Ball object definition
pong_ball = Ball()

# Handling paddle movement
screen.listen()
screen.onkey(user1_paddle.up, "w")
screen.onkey(user1_paddle.down, "s")
screen.onkey(user2_paddle.up, "Up")
screen.onkey(user2_paddle.down, "Down")


end_game = False
while not end_game:
    screen.update()
    time.sleep(0.01)
    


















# Screen exit
screen.exitonclick()
