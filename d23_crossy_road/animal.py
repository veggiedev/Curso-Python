from turtle import Turtle



class Animal(Turtle):
    def __init__(self, animal):
        super(). __init__()
        self.shape(animal)
        self.penup()
        self.hideturtle()
        self.goto(0, -290)
        self.seth(90)
        self.showturtle()
        
    def up(self):
        self.forward(10)
        
    def new_animal(self, animal):
        self.clear()
        self.shape(animal)
        self.penup()
        self.hideturtle()
        self.goto(0, -290)
        self.seth(90)
        self.showturtle()