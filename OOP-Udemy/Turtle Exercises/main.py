# import turtle as t
# import random
# from turtle import colormode
# timmy = t.Turtle()
# colormode(255)

# number_of_loops = 3
# timmy = t.Turtle()    
# pen_size = 1
# def draw():
#     timmy.right(random.randint(0, 3)*90)
#     timmy.left(random.randint(0,3)*90)
#     timmy.forward(random.randint(5, 125))
#     timmy.speed(0) 
# for _ in range(200):
#     timmy.pencolor((random.randint(0, 255)), (random.randint(0, 255)), (random.randint(0, 255)))
#     timmy.pensize(pen_size)
#     pen_size += 0.25
#     draw()

    
    
    

import turtle as t
import random
from turtle import colormode
timmy = t.Turtle()
colormode(255)

timmy = t.Turtle()    
pen_size = 1
def draw_circle():
    timmy.speed(0)    
    timmy.circle(100)

left = 5

for _ in range(72):
    timmy.pencolor((random.randint(0, 255)), (random.randint(0, 255)), (random.randint(0, 255)))
    print(left)
    timmy.left(left)
    draw_circle()
    
    

    
    
    



























# # screen.canvheight(500)
# # screen.canvwidth(500)



screen = t.Screen()
screen.exitonclick()
