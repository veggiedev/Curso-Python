import random
from turtle import Turtle, Screen
import time
import turtle
from snake import Snake, MOVING_DISTANCE
from score import Score
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)
score = 0
speed = 0.150

outside_coords = (300, 300)
coords = [0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280,
          -20, -40, -60, -80, -100, -120, -140, -160, -180, -200, -220, -240, -260, -280]
score_turtle = Turtle()

turtle_one = Turtle()
turtle_two = Turtle()
turtle_three = Turtle()
turtle_four = Turtle() 
turtle_five = Turtle()
turtle_six = Turtle()
turtle_seven = Turtle()
turtle_eight = Turtle()
turtle_nine = Turtle()
turtle_zero = Turtle()
def score_drawing():
    score_turtle.setheading(0)
    score_turtle.hideturtle()
    score_turtle.penup()
    score_turtle.pensize(3)
    score_turtle.color("white")
    score_turtle.goto(-55, 270)
    score_turtle.pendown()
    # "S"
    score_turtle.back(10)
    score_turtle.right(90)
    score_turtle.forward(5)
    score_turtle.left(90)
    score_turtle.forward(10)
    score_turtle.right(90)
    score_turtle.forward(5)
    score_turtle.right(90)
    score_turtle.forward(10)
    score_turtle.penup()
    score_turtle.setheading(0)
    score_turtle.forward(15)
    # "C"
    score_turtle.left(90)
    score_turtle.forward(10)
    score_turtle.right(90)
    score_turtle.pendown()
    score_turtle.forward(8)
    score_turtle.back(8)
    score_turtle.right(90)
    score_turtle.forward(10)
    score_turtle.left(90)
    score_turtle.forward(8)
    score_turtle.penup()
    score_turtle.forward(5)
    # "O"
    score_turtle.pendown()
    score_turtle.forward(8)
    score_turtle.left(90)
    score_turtle.forward(10)
    score_turtle.left(90)
    score_turtle.forward(8)
    score_turtle.left(90)
    score_turtle.forward(10)
    score_turtle.setheading(0)
    score_turtle.penup()
    score_turtle.forward(15)
    score_turtle.pendown()
    score_turtle.left(90)
    score_turtle.forward(5)
    score_turtle.right(90)
    score_turtle.forward(6)
    score_turtle.right(60)
    score_turtle.forward(6)
    score_turtle.back(6)
    score_turtle.setheading(90)
    score_turtle.forward(5)
    score_turtle.left(90)
    score_turtle.forward(6)
    score_turtle.setheading(0)
    score_turtle.penup()
    score_turtle.forward(14)
    score_turtle.pendown()
    score_turtle.forward(7)
    score_turtle.back(7)
    score_turtle.right(90)
    score_turtle.forward(5)
    score_turtle.left(90)
    score_turtle.forward(6)
    score_turtle.back(6)
    score_turtle.right(90)
    score_turtle.forward(5)
    score_turtle.left(90)
    score_turtle.forward(7)
def draw_score():
    
    
        
    def number_one(coords_score):
        turtle_one.setheading(0)
        turtle_one.hideturtle()
        turtle_one.penup()
        turtle_one.pensize(3)
        turtle_one.color("white")
        turtle_one.goto(coords_score)
        turtle_one.pendown()
        turtle_one.right(90)
        turtle_one.forward(10)
        turtle_one.penup()
        turtle_one.goto(coords_score)   

    def number_two(coords_score):
        turtle_two.setheading(0)
        turtle_two.hideturtle()
        turtle_two.penup()
        turtle_two.pensize(3)
        turtle_two.color("white")
        turtle_two.goto(coords_score)
        turtle_two.pendown()
        turtle_two.forward(10)
        turtle_two.right(90)
        turtle_two.forward(5)
        turtle_two.right(90)
        turtle_two.forward(10)
        turtle_two.left(90)
        turtle_two.forward(5)
        turtle_two.left(90)
        turtle_two.forward(10)
        turtle_two.penup()
        turtle_two.goto(coords_score)         

    def number_three(coords_score):
        turtle_three.setheading(0)
        turtle_three.hideturtle()
        turtle_three.penup()
        turtle_three.pensize(3)
        turtle_three.color("white")
        turtle_three.goto(coords_score)
        turtle_three.pendown()
        turtle_three.forward(10)
        turtle_three.right(90)
        turtle_three.forward(5)
        turtle_three.right(90)
        turtle_three.forward(5)
        turtle_three.back(5)
        turtle_three.left(90)
        turtle_three.forward(5)
        turtle_three.left(90)
        turtle_three.back(10)
        turtle_three.penup()    
        turtle_three.goto(coords_score)    
        
    def number_four(coords_score):
        turtle_four.setheading(0)
        turtle_four.hideturtle()
        turtle_four.penup()
        turtle_four.pensize(3)
        turtle_four.color("white")
        turtle_four.goto(coords_score)
        turtle_four.pendown()
        turtle_four.right(90)
        turtle_four.forward(5)
        turtle_four.left(90)
        turtle_four.forward(5)
        turtle_four.left(90)
        turtle_four.forward(5)
        turtle_four.back(10)
        turtle_four.penup()
        turtle_four.goto(coords_score)  
    
    def number_five(coords_score):
        turtle_five.setheading(0)
        turtle_five.hideturtle()
        turtle_five.penup()
        turtle_five.pensize(3)
        turtle_five.color("white")
        turtle_five.goto(coords_score)
        turtle_five.pendown()
        turtle_five.forward(5)
        turtle_five.back(5)
        turtle_five.right(90)
        turtle_five.forward(5)
        turtle_five.left(90)
        turtle_five.forward(5)
        turtle_five.right(90)
        turtle_five.forward(5)
        turtle_five.right(90)
        turtle_five.forward(5)
        turtle_five.penup()
        turtle_five.goto(coords_score) 
        
    def number_six(coords_score):
        turtle_six.setheading(0)
        turtle_six.hideturtle()
        turtle_six.penup()
        turtle_six.pensize(3)
        turtle_six.color("white")
        turtle_six.goto(coords_score)
        turtle_six.pendown()
        turtle_six.forward(5)
        turtle_six.back(5)
        turtle_six.right(90)
        turtle_six.forward(5)
        turtle_six.left(90)
        turtle_six.forward(5)
        turtle_six.right(90)
        turtle_six.forward(5)
        turtle_six.right(90)
        turtle_six.forward(5)
        turtle_six.right(90)
        turtle_six.forward(5)
        turtle_six.penup()
        turtle_six.goto(coords_score)   

    def number_seven(coords_score):
        turtle_seven.setheading(0)
        turtle_seven.hideturtle()
        turtle_seven.penup()
        turtle_seven.pensize(3)
        turtle_seven.color("white")
        turtle_seven.goto(coords_score)
        turtle_seven.pendown()
        turtle_seven.forward(5)
        turtle_seven.right(90)
        turtle_seven.forward(10)
        turtle_seven.penup()
        turtle_seven.goto(coords_score)    

    def number_eight(coords_score):
        turtle_eight.setheading(0)
        turtle_eight.hideturtle()
        turtle_eight.penup()
        turtle_eight.pensize(3)
        turtle_eight.color("white")
        turtle_eight.goto(coords_score)
        turtle_eight.pendown()
        turtle_eight.forward(5)
        turtle_eight.right(90)
        turtle_eight.forward(10)
        turtle_eight.right(90)
        turtle_eight.forward(5)
        turtle_eight.right(90)
        turtle_eight.forward(5)
        turtle_eight.right(90)
        turtle_eight.forward(5)
        turtle_eight.back(5)
        turtle_eight.left(90)
        turtle_eight.forward(5)
        turtle_eight.penup()
        turtle_eight.goto(coords_score)
        
    def number_nine(coords_score):
        turtle_nine.setheading(0)
        turtle_nine.hideturtle()
        turtle_nine.penup()
        turtle_nine.pensize(3)
        turtle_nine.color("white")
        turtle_nine.goto(coords_score)
        turtle_nine.pendown()
        turtle_nine.forward(5)
        turtle_nine.right(90)
        turtle_nine.forward(10)
        turtle_nine.right(90)
        turtle_nine.forward(5)
        turtle_nine.right(90)
        turtle_nine.penup()
        turtle_nine.forward(5)
        turtle_nine.pendown()
        turtle_nine.right(90)
        turtle_nine.forward(5)
        turtle_nine.back(5)
        turtle_nine.left(90)
        turtle_nine.forward(5)
        turtle_nine.penup()
        turtle_nine.goto(coords_score)
            
    def number_zero(coords_score):
        turtle_zero.setheading(0)
        turtle_zero.hideturtle()
        turtle_zero.penup()
        turtle_zero.pensize(3)
        turtle_zero.color("white")
        turtle_zero.goto(coords_score)
        turtle_zero.pendown()
        turtle_zero.forward(5)
        turtle_zero.right(90)
        turtle_zero.forward(10)
        turtle_zero.right(90)
        turtle_zero.forward(5)
        turtle_zero.right(90)
        turtle_zero.forward(10)    

    if numbers[0] == 0: 
        # non_dec_bg()           
        number_zero(decimal)
        
    elif numbers[0] == 1:
        # non_dec_bg()
        turtle_zero.reset()
        number_one(decimal)
        
    elif numbers[0] == 2:
        # non_dec_bg()
        turtle_one.reset()
        number_two(decimal)
    elif numbers[0] == 3:
        # non_dec_bg()
        turtle_two.reset()
        number_three(decimal)
    elif numbers[0] == 4:
        turtle_three.reset()
        # non_dec_bg()
        number_four(decimal)
    elif numbers[0] == 5:
        # non_dec_bg()
        turtle_four.reset()
        number_five(decimal)
    elif numbers[0] == 6:
        # non_dec_bg()
        turtle_five.reset()
        number_six(decimal)
    elif numbers[0] == 7:
        # non_dec_bg()
        turtle_six.reset()
        number_seven(decimal)
    elif numbers[0] == 8:
        # non_dec_bg()
        turtle_seven.reset()
        number_eight(decimal)
    elif numbers[0] == 9:
        # non_dec_bg()
        turtle_eight.reset()
        number_nine(decimal)
    elif numbers[0] == 0:
        # non_dec_bg()
        turtle_nine.reset()
        number_zero(decimal)
    if score > 9:
        if numbers[1] == 1:
            turtle_zero.reset()
            number_one(non_decimal)
        elif numbers[1] == 2:
            turtle_one.reset()
            number_two(non_decimal)
        elif numbers[1] == 3:
            turtle_two.reset()
            number_three(non_decimal)
        elif numbers[1] == 4:
            turtle_three.reset()
            number_four(non_decimal)
        elif numbers[1] == 5:
            turtle_four.reset()
            number_five(non_decimal)
        elif numbers[1] == 6:
            turtle_five.reset()
            number_six(non_decimal)
        elif numbers[1] == 7:
            turtle_six.reset()
            number_seven(non_decimal)
        elif numbers[1] == 8:
            turtle_seven.reset()
            number_eight(non_decimal)
        elif numbers[1] == 9:
            turtle_eight.reset()
            number_nine(non_decimal)
        elif numbers[1] == 0:
            turtle_nine.reset()
            number_zero(non_decimal)    

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
def pause(): 
    if snake.move() == True:
        snake.stop()
    else: 
        return snake.heading()
        
turtle.listen()
turtle.onkeypress(fun=up, key="w")
turtle.onkeypress(fun=left, key="a")
turtle.onkeypress(fun=right, key="d")
turtle.onkeypress(fun=down, key="s")
turtle.onkeypress(fun=pause, key="space")

food = Food()
food.random_spawn()
snake = Snake()
snake.create_snake() 
total_score = 0

def food_and_wall():  
    global game_is_on 
    global speed
    global total_score
    if int(food.xcor()) < int(snake.xcor()) + 2 and int(food.xcor()) > int(snake.xcor()) - 2 and int(food.ycor()) < int(snake.ycor()) + 2 and int(food.ycor()) > int(snake.ycor()) - 2:   
        total_score += 1
        print(total_score)
        
        points.reset()
        points.get_score(total_score)
        
        if speed > 0.100:
            speed -= 0.010
        elif speed > 0.050:
            speed -= 0.005
        elif speed < 0.050 and speed >= 0.020:
            speed = 0.020 
        print(speed)
        food.random_spawn()
        snake.grow()
    elif snake.xcor() > 290 or snake.ycor() > 290 or snake.xcor() < -290 or snake.ycor() < -290:
        print("You crashed!")
        print(f"You scored {score} points!")
        game_is_on = False 
    else:
        points = Score()
        points.get_score(score)               
while game_is_on:
    
    
    x_coord = random.choice(coords)
    y_coord = random.choice(coords) 
    # numbers = [int(a) for a in str(score)]
    if score > 100:
        print("Game Over")
        print("Your score is 100")  
    screen.update()
    time.sleep(speed)
    snake.move()
    food_and_wall() 
    points = Score()
    # score_object.score_drawing()  
screen.exitonclick()
