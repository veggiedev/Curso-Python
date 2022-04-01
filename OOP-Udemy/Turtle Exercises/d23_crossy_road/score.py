from turtle import Turtle






class Score(Turtle):
    def __init__(self, score):
        super().__init__()
        self.score = 0
        self.color('black')
        self.hideturtle()
        self.penup()
        self.goto(250, 270)
        self.update_scoreboard()
        
        
    def update_scoreboard(self):
        self.write(f'Score: {self.score}', align = 'center', font = ('Courier', 15))
        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()