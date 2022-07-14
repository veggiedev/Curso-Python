from logging import makeLogRecord
import colorgram
import turtle as t
import random
from turtle import colormode

colors = colorgram.extract('/Users/veggiedev/Curso-Python/OOP-Udemy/Turtle Exercises/hirst_painting/spots.gif', 20)
all_colors = [(246, 241, 244), (222, 152, 103), (233, 237, 240), (128, 172, 199), 
              (221, 130, 149), (221, 73, 90), (243, 208, 99), (17, 121, 157), (118, 176, 147), 
              (34, 120, 82), (18, 165, 204), (230, 74, 70), (142, 86, 60), (116, 85, 102), 
              (162, 209, 162), (13, 169, 120), (171, 183, 219), (177, 154, 75), (213, 222, 213)]


# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     all_colors.append(new_color)

print(all_colors)
timmy = t.Turtle()
timmy.pensize(30)
timmy.hideturtle()
colormode(255)

paint_color = 0

def make_dot():    
    timmy.color(random.choice(all_colors))
    timmy.pendown()     
    timmy.forward(1)    # Dot
    timmy.penup()
    
def move_fw():
    timmy.forward(60)
       
def turn_left():
    timmy.left(90)
    
move = 1   

while move <= 99:
    if move == 1:
        make_dot()
        paint_color += 1
        move_fw()
        turn_left()
        move += 1
        make_dot()
        paint_color += 1
        move_fw()
    else:
        if move == 2 or move == 4 or move == 6 or move == 9 or move == 12: 
            turn_left()
            make_dot()
            paint_color += 1
            move_fw()
            move += 1
        elif move == 16 or move == 20 or move == 25 or move == 30 or move == 36:
            turn_left()
            make_dot()
            paint_color += 1
            move_fw()
            move += 1 
        elif move == 42 or move == 49 or move == 56 or move == 64 or move == 72 or move == 81 or move == 90 or move == 100:
            turn_left()
            make_dot()
            paint_color += 1
            move_fw()
            move += 1                            
        else:
            make_dot()
            paint_color += 1
            move_fw()
            move += 1
    print(move)
        


screen = t.Screen()
screen.exitonclick()