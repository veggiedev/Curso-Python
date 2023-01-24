from turtle import Turtle




class Car(Turtle):
    def __init__(self):
        super().__init__()       
        # self.hideturtle()
        self.shape('square')
        self.penup()
        self.shapesize(1, 2)        
        # self.showturtle()        
        self.setheading(-180)


