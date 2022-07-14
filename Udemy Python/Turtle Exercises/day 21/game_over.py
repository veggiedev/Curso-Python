from turtle import Turtle


class gameover(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.pencolor("white")
        self.goto(0, 0)
        
    def game_over(self):
        self.write(f"GAME OVER", align="center", font=("Courier", 20, "normal"))           
    
    # def increase_score(self):
    #     self.score += 1
    #     self.clear()
    #     self.update_scoreboard()