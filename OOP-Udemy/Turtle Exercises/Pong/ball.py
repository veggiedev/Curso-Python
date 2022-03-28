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
    def hit(self, paddle_surface):
        self.y_move *= -1 + paddle_surface
    