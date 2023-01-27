import random
from tkinter import Y
from turtle import Turtle, Screen
import time
import turtle
from snake import Snake, MOVING_DISTANCE
from score import Scoreboard
from food import Food
from game_over import gameover
from newgame import Newgame


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)
speed = 0.150
outside_coords = (300, 300)
coords = [0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280,
          -20, -40, -60, -80, -100, -120, -140, -160, -180, -200, -220, -240, -260, -280]
game_is_on = True
def up():   
        if snake.heading() == 270:
            print ("You can't go up")
        else:
            snake.setheading(90)        
def left():    
        if snake.heading() == 0:
            print("You can't go left")
        else:   
            snake.setheading(180)         
def right():    
        if snake.heading() == 180:
            print("You can't go right")
        else:    
            snake.setheading(0)            
def down():    
        if snake.heading() == 90:
            print("You can't go down")
        else:
            snake.setheading(-90) 
           

game_over = gameover()
food = Food()
scoreboard = Scoreboard()
food.random_spawn()
snake = Snake()
while game_is_on:
    

    play_game = screen.textinput('Play a New Game?', 'Do you want to play? y or n')    
    turtle.listen()
    turtle.onkeypress(fun=up, key="w")
    turtle.onkeypress(fun=left, key="a")
    turtle.onkeypress(fun=right, key="d")
    turtle.onkeypress(fun=down, key="s")
    if play_game == 'y':
        no_crash = True
        game_over.clear()
        snake.move()
        while no_crash: 
            snake.move()              

            if snake.xcor() > 290 or snake.ycor() > 290 or snake.xcor() < -290 or snake.ycor() < -290:
                print("You crashed!")
                scoreboard.reset()
                snake.new_snake()
                snake.move()
                speed = 0.150                
                no_crash = False  
            if int(food.xcor()) < int(snake.xcor()) + 2 and int(food.xcor()) > int(snake.xcor()) - 2 and int(food.ycor()) < int(snake.ycor()) + 2 and int(food.ycor()) > int(snake.ycor()) - 2:   
                scoreboard.increase_score()
                food.random_spawn()
                snake.grow()
                if speed > 0.100:
                    speed -= 0.005
                elif speed > 0.050:
                    speed -= 0.001
                elif speed < 0.050:
                    speed = 0.050              
            #Detect collion tail
            for segment in snake.segments[1:]:
                if snake.head.distance(segment) < 10:
                    game_over.game_over()
                    speed = 0.150
                    no_crash = False    
            if scoreboard.score >= 100:
                game_over.game_over()
                speed = 0.150
                game_is_on = False        
            screen.update()
            time.sleep(speed)
    else:
        game_is_on = False   
screen.exitonclick()
