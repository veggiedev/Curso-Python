from turtle import Turtle


class Gameover(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.pencolor("black")
        self.goto(0, 0)
        
    def game_over(self):
        self.write(f"GAME OVER", align="center", font=("Courier", 50, "normal"))           
