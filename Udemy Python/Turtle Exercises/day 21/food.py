from turtle import Turtle
import random
COORDS = [0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280,
          -20, -40, -60, -80, -100, -120, -140, -160, -180, -200, -220, -240, -260, -280]
class Food:
    
    def __init__(self):
        self.food = Turtle("circle")
        self.food.penup()
        self.food.turtlesize(0.4)
        self.food.color("yellow")
        self.food.hideturtle()
    
    def random_spawn(self):
        self.food.goto(random.choice(COORDS), random.choice(COORDS))
        self.food.showturtle()
    def xcor(self):
        return self.food.xcor()
    def ycor(self):
        return self.food.ycor() 
    
    
    

