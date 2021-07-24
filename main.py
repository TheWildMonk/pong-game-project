from turtle import Screen
from paddle import Paddle
import time


# Screen object definition
screen = Screen()
screen.bgcolor("Slateblue4")
screen.title("The Pong Game")
screen.setup(width=800, height=600)
screen.tracer(0)

# Paddle object definition
user_paddle = Paddle()
user_paddle.goto(-350, 0)

# Computer paddle object definition
computer_paddle = user_paddle.clone()
computer_paddle.speed("slowest")
computer_paddle.goto(350, 0)

# Handling paddle movement
screen.listen()
screen.onkey(user_paddle.up, "w")
screen.onkey(user_paddle.down, "s")
# screen.onkey(computer_paddle.up, "Up")
# screen.onkey(computer_paddle.down, "Down")


end_game = False
while not end_game:
    screen.update()
    time.sleep(0.01)
    if computer_paddle.ycor() >= 250 or computer_paddle.ycor() <= -250:
        computer_paddle.left(180)
        computer_paddle.forward(1)
    else:
        computer_paddle.forward(1)



















# Screen exit
screen.exitonclick()
