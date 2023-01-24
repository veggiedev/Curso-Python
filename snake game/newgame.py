from turtle import Turtle


class Newgame(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.pencolor("white")
        self.goto(0, 0)
        
    def start_new_game(self):
        self.write(f"NEW GAME?", align="center", font=("Courier", 20, "normal"))
          