from turtle import Turtle

class Game_over(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.end()
        
        
        
    def end(self):
        self.write("GAME OVER", align="center", font=("Courier", 20, "normal"))