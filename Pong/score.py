from turtle import Turtle




class Score(Turtle):
    def __init__(self, coords):
        super(). __init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.setpos(coords)
        self.color('white')        
        self.get_score()
        
    
    def get_score(self):
        self.write(self.score, font=("Courier", 40, "normal"))
        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.get_score()
        
    def score_count(self):
        return self.score