import turtle as t
import random
timmy = t.Turtle()
number_of_loops = 3
colors = ['yellow', 'gold', 'orange', 'red', 'maroon', 'violet', 
        'magenta', 'purple', 'navy', 'blue', 'skyblue', 'cyan', 
        'turquoise', 'lightgreen', 'green', 'darkgreen', 'chocolate', 
        'brown', 'black', 'gray',
          ]
timmy = t.Turtle()    
pen_size = 1
def draw():
    timmy.right(random.randint(0, 3)*90)
    timmy.left(random.randint(0,3)*90)
    timmy.forward(20)  
    timmy.speed(0) 
for _ in range(200):
    timmy.color("white")
    random_color = random.choice(colors)
    timmy.pencolor(random_color)
    timmy.pensize(pen_size)
    pen_size += 0.25
    draw()

    
    
    






























# # screen.canvheight(500)
# # screen.canvwidth(500)




screen = t.Screen()
screen.exitonclick()
