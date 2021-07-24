from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.user1_score = 0
        self.user2_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-100, 200)
        self.write(self.user1_score, align="center", font=("raleway", 80, "bold"))
        self.goto(100, 200)
        self.write(self.user2_score, align="center", font=("raleway", 80, "bold"))

    def increase_user1_score(self):
        self.clear()
        self.user1_score += 1
        self.update_scoreboard()

    def increase_user2_score(self):
        self.clear()
        self.user2_score += 1
        self.update_scoreboard()


