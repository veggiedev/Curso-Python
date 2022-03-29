from turtle import Turtle



class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.setpos(0, 0)
        self.shape('circle')
        self.penup()
        self.x_move = 10
        self.y_move = 10
        
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        
    def bounce(self):
        self.y_move *= -1
        
    def hit_y(self):
        self.y_move *= -0.90
    
    def hit_x(self):
        self.x_move *= -0.9
    
    def new_move(self):
        self.x_move *= -1
        new_x = self.xcor() + self.x_move *-1
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        
    