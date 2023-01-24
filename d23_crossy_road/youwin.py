from turtle import Turtle



class Youwin(Turtle):
    def __init__(self):
        super().__init__()
        self.color('red')
        self.hideturtle()
        self.winner_banner()
        
        
    def winner_banner(self):
        self.write('YOU WIN!!!', align='center', font=('bold', 15))