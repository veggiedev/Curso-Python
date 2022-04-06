from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0    
        with open('OOP-Udemy/Turtle Exercises/day 21/data.txt') as data:
            self.highscore = int(data.read())
            

        self.penup()
        self.hideturtle()
        self.pencolor("white")
        self.goto(0, 270)
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"SCORE: {self.score} High Score: {self.highscore}", align="center", font=("Courier", 20, "normal"))           
    
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
                
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('/Users/veggiedev/Curso-Python/OOP-Udemy/Turtle Exercises/day 21/data.txt', 'w') as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()        

        