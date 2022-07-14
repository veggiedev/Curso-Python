from turtle import Turtle, Screen
import time
import random
from animal import Animal
from car import Car
import names
from gameover import Gameover
from youwin import Youwin
from score import Score


screen = Screen()
screen.setup(600,600)
screen.tracer(0)
list_of_names = []
cars = []
bg_colors = ['gold', 'maroon', 'violet', 'magenta', 'purple', 'navy', 'skyblue', 'cyan', 'lightgreen', 'darkgreen', 'chocolate', 'gray', 'white']
car_colors = ('blue', 'yellow', 'green', 'purple', 'orange', 'pink', 'brown', 'black', 'beige', 'turquoise')
car_speed = 0.05
for i in range(150):
    list_of_names.append(names.get_first_name(gender='male'))

print(list_of_names)

speed_list = [5, 6, 7, 8, 9, 10]    
game_is_on = True

turtle = Animal('turtle')
scoreboard = 0
screen.listen()
screen.onkeypress(fun=turtle.up, key="w")

for i in list_of_names:
    i = Car()
    cars.append(i)

for i in cars:
    i.color(random.choice(car_colors))
    i.goto(random.randint(270, 4090), random.randint(-270, 270))

sleeping_times = (0.0035, 0.0040, 0.0045, 0.0050, 0.0055, 0.0060, 0.0065, 0.0070, 0.0075, 0.0080, 0.0085, 0.0090, 0.0095, 0.01, 0.015, 0.020, 0.025, 0.030, 0.035, 0.040, 0.1, 0.2)
    
while game_is_on:
    score = Score(scoreboard)
    # score.score()
    random_time = random.choice(sleeping_times)
    for i in range(400): 
          
        random.choice(cars).speed(random.choice(speed_list))
        for car in cars:
            random.choice(cars).forward(random.randint(1, 3))
            if turtle.ycor() > 280:
                turtle.hideturtle()
                score.increase_score()
                car_speed *= 0.9
                turtle.goto(0, -290)
                turtle.showturtle()
                screen.bgcolor(random.choice(bg_colors))
                
            else:
                if car.distance(turtle) < 25: #and car.ycor() + 10 < turtle.ycor() and car.ycor() - 10 > turtle.ycor():
                    screen.onkeypress(fun=None, key="w")
                    gameover = Gameover()
                    gameover.game_over()
                    game_is_on = False
        screen.update()  

        time.sleep(car_speed)

screen.exitonclick()