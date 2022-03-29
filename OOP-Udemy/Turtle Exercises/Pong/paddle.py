from turtle import Turtle
rgo = 0
lgo = 0
class Paddle(Turtle):
    def __init__(self, coords):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')
        self.shape('square')
        self.shapesize(5, 1)
        self.goto(coords)
        self.showturtle()        
    def up(self):
        global lgo
        lgo += 20
        self.setpos(-350, lgo)
    def down(self):
        global lgo
        lgo -= 20
        self.setpos(-350, lgo)
    def rup(self):
        global rgo
        rgo += 20
        self.setpos(350, rgo)
    def rdown(self):
        global rgo
        rgo -= 20
        self.setpos(350, rgo)