from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.pencolor("white")
        self.goto(0, 270)
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.write(f"SCORE: {self.score}", align="center", font=("Courier", 20, "normal"))           
    
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()