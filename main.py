from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


# Screen object definition
screen = Screen()
screen.bgcolor("#192a56")
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

# Scoreboard object definition
score = Scoreboard()

# Handling paddle movement
screen.listen()
screen.onkey(user1_paddle.up, "w")
screen.onkey(user1_paddle.down, "s")
screen.onkey(user2_paddle.up, "Up")
screen.onkey(user2_paddle.down, "Down")


end_game = False
while not end_game:
    time.sleep(pong_ball.move_speed)
    screen.update()
    pong_ball.move()
    # Detect collision with the wall
    if pong_ball.ycor() > 280 or pong_ball.ycor() < -280:
        pong_ball.wall_bounce()
    # Detect collision with the paddle
    if pong_ball.distance(user2_paddle) < 50 and pong_ball.xcor() > 320:
        pong_ball.paddle_bounce()
        score.increase_user2_score()
    elif pong_ball.distance(user1_paddle) < 50 and pong_ball.xcor() < -320:
        pong_ball.paddle_bounce()
        score.increase_user1_score()
    # Detect if the ball goes past the right or left wall
    if pong_ball.xcor() > 380:
        pong_ball.home()
        pong_ball.paddle_bounce()
        score.increase_user1_score()
    elif pong_ball.xcor() < -380:
        pong_ball.home()
        pong_ball.paddle_bounce()
        score.increase_user2_score()

# Screen exit
screen.exitonclick()
